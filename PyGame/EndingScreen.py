import pygame
from GameConfig import GameConfig as gc


class EndingButton(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        return

    def draw(self):
        gc.surface.blit(self.image, self.rect)
        return
    pass
