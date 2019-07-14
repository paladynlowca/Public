from os import path, mkdir


class Stats:
    win = 0
    lose = 0
    draw = 0

    @staticmethod
    def load():
        if not path.exists(path.expandvars(r'%LOCALAPPDATA%\OX\stats.bin')):
            Stats.save()
            pass
        with open(path.expandvars(r'%LOCALAPPDATA%\OX\stats.bin'), 'rb') as file:
            Stats.win = int.from_bytes(file.read(4), byteorder='big', signed=True)
            Stats.lose = int.from_bytes(file.read(4), byteorder='big', signed=True)
            Stats.draw = int.from_bytes(file.read(4), byteorder='big', signed=True)
            pass
        return

    @staticmethod
    def save():
        if not path.exists(path.expandvars(r'%LOCALAPPDATA%\OX')):
            mkdir(path.expandvars(r'%LOCALAPPDATA%\OX'))
            pass
        with open(path.expandvars(r'%LOCALAPPDATA%\OX\stats.bin'), 'wb') as file:
            file.write(Stats.win.to_bytes(4, byteorder='big', signed=True))
            file.write(Stats.lose.to_bytes(4, byteorder='big', signed=True))
            file.write(Stats.draw.to_bytes(4, byteorder='big', signed=True))
            pass
        return

    @staticmethod
    def add(result):
        if result == 'win':
            Stats.win += 1
            pass
        elif result == 'lose':
            Stats.lose += 1
            pass
        elif result == 'draw':
            Stats.draw += 1
            pass
        Stats.save()
        return
    pass
