import pygame
import re
from os import listdir
from random import Random

from Constants import *


class GameConfig:
    grid = None
    board_name = None
    surface = None
    player = None
    new_game_button = None
    quit_button = None
    player_pos = [0, 1]
    board_size = (0, 0)
    board_move = (0, 0)
    moves_counter = 1
    player_won = False

    @staticmethod
    def set_grid(grid):
        GameConfig.grid = grid
        GameConfig.board_size = (grid.width, grid.height)
        return

    @staticmethod
    def set_surface(surface):
        GameConfig.surface = surface
        from EndingScreen import EndingButton
        GameConfig.new_game_button = EndingButton(300, 300, BUTTON_NEW_GAME)
        GameConfig.quit_button = EndingButton(620, 300, BUTTON_EXIT)
        return

    @staticmethod
    def set_player(player):
        GameConfig.player = player
        return

    @staticmethod
    def move_player(mov, dir):
        if not GameConfig.check_correct_move(mov, dir):
            GameConfig.reset()
            return
            pass
        if dir == 'x' and 0 <= GameConfig.player_pos[0] + mov < GameConfig.board_size[0] and GameConfig.grid[
           GameConfig.player_pos[0] + mov, GameConfig.player_pos[1]].visitable:
            GameConfig.player_pos[0] += mov
            pass
        if dir == 'y' and 0 <= GameConfig.player_pos[1] + mov < GameConfig.board_size[1] and GameConfig.grid[
           GameConfig.player_pos[0], GameConfig.player_pos[1] + mov].visitable:
            GameConfig.player_pos[1] += mov
            pass
        GameConfig.show_titles()
        GameConfig.moves_counter += 1
        GameConfig.grid[GameConfig.player_pos[0], GameConfig.player_pos[1]].last_visited = GameConfig.moves_counter
        if GameConfig.player_pos == [GameConfig.board_size[0] - 1, GameConfig.board_size[1] - 2]:
            GameConfig.player_won = True
            print('wygrana')
        return

    @staticmethod
    def board_move_calc():
        if GameConfig.board_size[0] <= WIDTH:
            mov_x = (WIDTH - GameConfig.board_size[0]) / 2
            pass
        else:
            center_x = WIDTH / 2
            if GameConfig.player_pos[0] < center_x:
                mov_x = 0
                pass
            elif GameConfig.player_pos[0] > (GameConfig.board_size[0] - center_x):
                mov_x = GameConfig.board_size[0] - WIDTH
                pass
            else:
                mov_x = GameConfig.player_pos[0] - (WIDTH - 1) / 2
                pass
            pass

        if GameConfig.board_size[1] <= HEIGHT:
            mov_y = HEIGHT - GameConfig.board_size[1] / 2
            pass
        else:
            center_y = HEIGHT / 2
            if GameConfig.player_pos[1] < center_y:
                mov_y = 0
                pass
            elif GameConfig.player_pos[1] > (GameConfig.board_size[1] - center_y):
                mov_y = GameConfig.board_size[1] - HEIGHT
                pass
            else:
                mov_y = GameConfig.player_pos[1] - (HEIGHT - 1) / 2
                pass
            pass
        GameConfig.board_move = (mov_x, mov_y)
        return

    @staticmethod
    def move_player_event(event):
        if event.type == pygame.KEYDOWN and not GameConfig.player_won:
            if event.key == pygame.K_UP:
                GameConfig.move_player(-1, 'y')
                GameConfig.player.image = PLAYER_N
                pass
            elif event.key == pygame.K_DOWN:
                GameConfig.move_player(1, 'y')
                GameConfig.player.image = PLAYER_S
                pass
            elif event.key == pygame.K_LEFT:
                GameConfig.move_player(-1, 'x')
                GameConfig.player.image = PLAYER_W
                pass
            elif event.key == pygame.K_RIGHT:
                GameConfig.move_player(1, 'x')
                GameConfig.player.image = PLAYER_E
                pass
            pass
        return

    @staticmethod
    def player_won_event(event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if 300 < pos[1] < 440:
                if 300 < pos[0] < 580:
                    print('nowa gra')
                    GameConfig.rand_cake()
                    GameConfig.reset()
                    pass
                elif 620 < pos[0] < 900:
                    print('wyjście')
                    return False
                    pass
                pass
            pass
        return True

    @staticmethod
    def show_titles():
        for i in range(GameConfig.player_pos[0] - 1, GameConfig.player_pos[0] + 2):
            for j in range(GameConfig.player_pos[1] - 1, GameConfig.player_pos[1] + 2):
                try:
                    GameConfig.grid[i, j].visible = True
                    pass
                except KeyError:
                    pass
                pass
            pass
        return

    @staticmethod
    def check_correct_move(mov, dir):
        try:
            east = (GameConfig.grid[GameConfig.player_pos[0] + 1, GameConfig.player_pos[1]], 1, 'x')
            pass
        except KeyError:
            east = None
            pass
        try:
            south = (GameConfig.grid[GameConfig.player_pos[0], GameConfig.player_pos[1] + 1], 1, 'y')
            pass
        except KeyError:
            south = None
            pass
        try:
            west = (GameConfig.grid[GameConfig.player_pos[0] - 1, GameConfig.player_pos[1]], -1, 'x')
            pass
        except KeyError:
            west = None
            pass
        try:
            north = (GameConfig.grid[GameConfig.player_pos[0], GameConfig.player_pos[1] - 1], -1, 'y')
            pass
        except KeyError:
            north = None
            pass
        dirs = [east, south, west, north]
        for i in dirs:
            if i and i[0].visitable and not i[0].last_visited:
                if mov == i[1] and dir == i[2]:
                    return True
                else:
                    return False
                pass
            pass

        cor_dir = None
        for i in dirs:
            if not i:
                pass
            elif not i[0].visitable:
                pass
            elif not cor_dir:
                cor_dir = i
                pass
            elif cor_dir[0].last_visited > i[0].last_visited:
                cor_dir = i
                pass
            pass

        if mov == cor_dir[1] and dir == cor_dir[2]:
            return True
        else:
            return False
        pass

    @staticmethod
    def reset():
        GameConfig.moves_counter = 1
        GameConfig.player_pos = [0, 1]
        from Player import Player
        GameConfig.set_player(Player())
        from GameGrid import GameGrid
        GameConfig.set_grid(GameGrid(GameConfig.board_name))
        GameConfig.show_titles()
        GameConfig.player_won = False
        return

    @staticmethod
    def rand_cake():
        file_list = []
        for file in listdir('boards'):
            name = re.search('.cake', file)
            if name:
                file_list.append(file.replace('.cake', ''))
                pass
            pass
        GameConfig.board_name = file_list[Random.randint(Random(), 0, file_list.__len__() - 1)]
        return

    @staticmethod
    def draw():
        GameConfig.board_move_calc()
        GameConfig.grid.draw()
        GameConfig.player.draw()
        if GameConfig.player_won:
            GameConfig.quit_button.draw()
            GameConfig.new_game_button.draw()
            pass
        pygame.display.flip()
        return
    pass
