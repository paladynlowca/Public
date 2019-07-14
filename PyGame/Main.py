import datetime
import os
import pygame

from Constants import *
from GameConfig import GameConfig as gc

os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrowanie okna
pygame.init()

## ustawienia ekranu i gry
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Giera')
clock = pygame.time.Clock()

gc.rand_cake()
gc.set_surface(screen)
gc.reset()

window_open = True
gc.show_titles()
while window_open:
    # pętla zdarzeń
    # algorytm
    for event in pygame.event.get():
        # print(event)
        window_open = gc.player_won_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False
                pass
            pass
        elif event.type == pygame.QUIT:
            window_open = False
            pass
        gc.move_player_event(event)
        pass

    # aktualizacja okna pygame
    screen.blit(BACKGROUND, (0, -14))
    gc.draw()
    pass
pygame.quit()
