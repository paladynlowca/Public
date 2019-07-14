import pygame

from Constants import *
from GameConfig import GameConfig as gc


class Title(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

        self.image = PLATE_WALL
        self.rect = self.image.get_rect()
        self.rect.x = x * TITLE_SIZE[0]
        self.rect.y = y * TITLE_SIZE[1]
        self.to_explore = False
        self.visitable = False
        self.visible = False
        return

    def draw(self):
        cur_x = self.x - gc.board_move[0]
        cur_y = self.y - gc.board_move[1]
        if 0 <= cur_x < WIDTH and 0 <= cur_y < HEIGHT:
            self.rect.x = (cur_x + BOARD_SHIFT_X) * TITLE_SIZE[0]
            self.rect.y = (cur_y + BOARD_SHIFT_Y) * TITLE_SIZE[1]
            if self.visible:
                gc.surface.blit(self.image, self.rect)
                pass
            else:
                gc.surface.blit(PLATE_DARK, self.rect)
            pass
        return
    pass


class Road(Title):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = PLATE_ROAD
        self.visitable = True
        self.last_visited = False
        return

    def visit(self):
        return
    pass
