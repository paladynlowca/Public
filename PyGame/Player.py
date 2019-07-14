import pygame

from Constants import *
from GameConfig import GameConfig as gc


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = PLAYER
        self.rect = self.image.get_rect()
        self.img_offset_x = (TITLE_SIZE[0] - self.rect.right) / 2
        self.img_offset_y = (TITLE_SIZE[1] - self.rect.bottom) / 2
        self.to_explore = False
        return

    def draw(self):
        self.rect.x = (gc.player_pos[0] - gc.board_move[0] + (SCREEN_WIDTH - WIDTH) / 2) * TITLE_SIZE[0] + self.img_offset_x
        self.rect.y = (gc.player_pos[1] - gc.board_move[1] + (SCREEN_HEIGHT - HEIGHT) / 2 - 1) * TITLE_SIZE[1] + self.img_offset_y
        gc.surface.blit(self.image, self.rect)
        return

    pass
