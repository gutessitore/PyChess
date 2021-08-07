from pygame.locals import MOUSEBUTTONDOWN
from objects.game import Game
from elements import *
from config import *
import pygame
import time
import sys


def init_game() -> Game:
    game = Game()
    game.load_from_fen("rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2")
    return game


def init_pygame() -> pygame.Surface:
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return surface


def update_game(game: Game, surface: pygame.Surface) -> None:
    game.display_board(surface)
    pygame.display.flip()


mouse_rect = pygame.Rect(0, 0, 1, 1)


game = init_game()
surface = init_pygame()
while True:
    for event in pygame.event.get():
        event_type = event.type

        if event_type == pygame.QUIT:
            sys.exit()

        elif event_type == MOUSEBUTTONDOWN:
            mouse_rect.center = pygame.mouse.get_pos()
    update_game(game, surface)