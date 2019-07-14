from os import path

from pygame import image

PLAYER = image.load(path.join('img', 'player.png'))
PLAYER_N = image.load(path.join('img', 'player_N.png'))
PLAYER_S = image.load(path.join('img', 'player_S.png'))
PLAYER_W = image.load(path.join('img', 'player_W.png'))
PLAYER_E = image.load(path.join('img', 'player_E.png'))


PLATE_DARK = image.load(path.join('img', 'black.png'))
PLATE_ROAD = image.load(path.join('img', 'yellow.png'))
PLATE_WALL = image.load(path.join('img', 'rock.png'))

BACKGROUND = image.load(path.join('img', 're_maze.png'))
BUTTON_EXIT = image.load(path.join('img', 'quit.png'))
BUTTON_NEW_GAME = image.load(path.join('img', 'play_again.png'))

TITLE_SIZE = 60, 60
WIDTH = 13
HEIGHT = 5
SCREEN_WIDTH = 20
SCREEN_HEIGHT = 11
BOARD_SHIFT_X = (SCREEN_WIDTH - WIDTH) / 2
BOARD_SHIFT_Y = (SCREEN_HEIGHT - HEIGHT) / 2 - 1
SCREEN_SIZE = SCREEN_WIDTH * TITLE_SIZE[0], SCREEN_HEIGHT * TITLE_SIZE[1]

WIDGET_BG = BUTTON_FG = '#222'
WIDGET_ABG = '#444'
WIDGET_FG = '#888'

BUTTON_BG = '#aaa'
BUTTON_ABG = '#777'

FONT_SMALL = ("Helvetica", "10", 'bold')
FONT_BASE = ("Helvetica", "12", 'bold')
FONT_BIG = ("Helvetica", "15", 'bold')
