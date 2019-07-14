from os import path, mkdir


class Settings(object):
    _player_sign_char = 'x'
    _difficulty_level = 1

    @property
    def difficulty(self):
        return Settings._difficulty_level

    @difficulty.setter
    def difficulty(self, value):
        if value in [1, 2, 3]:
            Settings._difficulty_level = value
            pass
        else:
            raise ValueError('Difficulty value is not one of [1, 2, 3]')
        return

    @property
    def sign(self):
        return Settings._player_sign_char

    @property
    def sign_opponent(self):
        return 'x' if self.sign == 'o' else 'o'

    @sign.setter
    def sign(self, value):
        if value == 'x' or value == 'X':
            Settings._player_sign_char = 'x'
            pass
        elif value == 'o' or value == 'O':
            Settings._player_sign_char = 'o'
            pass
        else:
            raise ValueError("Sign value is not one of ['x', 'X'] for x, ['o', 'O'] for o.")
        return

    @staticmethod
    def save():
        if not path.exists(path.expandvars(r'%LOCALAPPDATA%\OX')):
            mkdir(path.expandvars(r'%LOCALAPPDATA%\OX'))
            pass
        with open(path.expandvars(r'%LOCALAPPDATA%\OX\settings.bin'), 'wb') as file:
            file.write(Settings._difficulty_level.to_bytes(1, byteorder='big', signed=True))
            file.write(Settings._player_sign_char.encode('ascii'))
            pass
        return

    @staticmethod
    def load():
        if not path.exists(path.expandvars(r'%LOCALAPPDATA%\OX\settings.bin')):
            Settings.save()
            pass
        with open(path.expandvars(r'%LOCALAPPDATA%\OX\settings.bin'), 'rb') as file:
            Settings._difficulty_level = int.from_bytes(file.read(1), byteorder='big', signed=True)
            Settings._player_sign_char = file.read(1).decode('ascii')
            pass
    pass
