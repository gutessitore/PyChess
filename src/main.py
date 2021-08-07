from pygame.locals import MOUSEBUTTONDOWN
from objects.game import Game
from utils.utils import *
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
clock = pygame.time.Clock()
print(game.display_on_console)
# game.board.move_piece((3, 7), (2, 6))

while True:

    for event in pygame.event.get():
        event_type = event.type

        if event_type == pygame.QUIT:
            sys.exit()

        elif event_type == MOUSEBUTTONDOWN:

            reset_square_colors = False
            if clock.tick() < DOUBLE_CLICK_TIME:
                reset_square_colors = True

            mouse_rect.center = pygame.mouse.get_pos()
            for square in game.board.squares:
                if event.button == RIGHT_CLICK:
                    if square.rect.colliderect(mouse_rect):
                        toggle_red_square(square)
                        print(square.pos)

                if event.button == LEFT_CLICK:
                    if square.rect.colliderect(mouse_rect):
                        if square.is_occupied:
                            for square_to_check in game.board.squares:

                                if square_to_check.pos in square.current_piece.possible_moves:
                                    path_is_clear = game.board.move_path_is_clear(square.pos, square_to_check.pos)
                                    can_jump = square.current_piece._piece_rules.get("movement").get("canJump")
                                    if (path_is_clear or can_jump) and not square_to_check.is_occupied:
                                        # print(square_to_check.pos)
                                        toggle_red_gray(square_to_check)

                if reset_square_colors:
                    square.temp_color = None

    update_game(game, surface)
