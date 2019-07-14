from Title import *


class GameGrid:
    def __init__(self, name):
        self.width = 13
        self.height = 6

        self._title_list = {}
        self.player_position = (0, 1)

        self.load(name)
        return

    def draw(self):
        for title in self._title_list:
            self[title].draw()
            pass
        return

    def __getitem__(self, key):
        x, y = key
        return self._title_list[(x, y)]

    def __setitem__(self, key, value):
        x, y = key
        self._title_list[(x, y)] = value
        return

    def load(self, name):
        with open(path.expandvars('boards\\' + name + '.cake'), 'rb') as file:
            self.width = int.from_bytes(file.read(1), byteorder='big', signed=True)
            self.height = int.from_bytes(file.read(1), byteorder='big', signed=True)
            for i in range(self.width):
                for j in range(self.height):
                    value = int.from_bytes(file.read(1), byteorder='big', signed=True)
                    self[i, j] = Road(i, j) if value == 1 else Title(i, j)
                    pass
                pass
            pass
        return
    pass
