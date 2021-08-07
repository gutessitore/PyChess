from pygame.locals import MOUSEBUTTONDOWN
from objects.game import Game
from utils.utils import *
from config import *
import pygame
import time
import sys


def init_game() -> Game:
    game = Game()
    game.load_from_fen("rnb1kbnr/pp1pppp1/1qp5/7p/2B1P1Q1/1P3N2/P1PP1PPP/RNB1K2R w KQkq - 0 1")
    return game


def init_pygame() -> pygame.Surface:
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return surface


def update_game(game: Game, surface: pygame.Surface) -> None:
    game.display_board(surface)
    pygame.display.flip()


def toggle_red_square_on_right_click(sqr, mouse):
    if event.button == RIGHT_CLICK:
        if square.rect.colliderect(mouse):
            toggle_red_square(sqr)
            print(square.pos)


def preview_possible_moves_on_left_click(sqr, mouse):
    if event.button == LEFT_CLICK:
        if sqr.rect.colliderect(mouse):
            if sqr.is_occupied:
                for square_to_check in game.board.squares:

                    if square_to_check.pos in square.current_piece.possible_moves:
                        path_is_clear = game.board.move_path_is_clear(square.pos, square_to_check.pos)
                        can_jump = sqr.current_piece.can_jump
                        is_able_to_move = path_is_clear or can_jump
                        if is_able_to_move and not square_to_check.is_occupied:
                            toggle_red_gray(square_to_check)


mouse_rect = pygame.Rect(0, 0, 1, 1)


game = init_game()
surface = init_pygame()
clock = pygame.time.Clock()
print(game.display_on_console)
# game.board.move_piece((3, 7), (2, 6))

while True:

    for event in pygame.event.get():
        event_type = event.type

        # Exit the game
        if event_type == pygame.QUIT:
            sys.exit()

        elif event_type == MOUSEBUTTONDOWN:

            # Check for doubleclick
            reset_square_colors = False
            if clock.tick() < DOUBLE_CLICK_TIME:
                reset_square_colors = True

            mouse_rect.center = pygame.mouse.get_pos()

            for square in game.board.squares:

                toggle_red_square_on_right_click(square, mouse_rect)
                preview_possible_moves_on_left_click(square, mouse_rect)
                if reset_square_colors:
                    square.temp_color = None

    update_game(game, surface)
