import abc
import random

import Settings


class SI(object):
    def __init__(self, board):
        self._settings = Settings.Settings()
        self._board = board
        return

    @abc.abstractmethod
    def play(self):
        return
    pass


class SIEasy(SI):
    def play(self):
        if self._board.free_count == 0:
            return False
        num = round(random.random() * self._board.free_count - 0.5)
        field = self._board.free_fields[num]
        self._board.set_sign('opponent', field, "#aa2222")
        return True
    pass


class SIMedium(SI):
    def play(self):
        if self._board.free_count == 0:
            return False
        current = False
        for line in self._board.check_lines(2):
            if line:
                if line[1] == self._settings.sign_opponent:
                    for field in line[0]:
                        if self._board[field].value == 0:
                            self._board.set_sign('opponent', self._board[field], "#aa2222")
                            return True
                        pass
                    pass
                elif line[1] == self._settings.sign:
                    current = line
                    pass
                pass
            pass
        if current:
            for field in current[0]:
                if self._board[field].value == 0:
                    self._board.set_sign('opponent', self._board[field], "#aa2222")
                    return True
                pass
            pass
        num = round(random.random() * self._board.free_count - 0.5)
        field = self._board.free_fields[num]
        self._board.set_sign('opponent', field, "#aa2222")
        return True
    pass
