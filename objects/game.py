from objects.square import Square
from objects.board import Board
from utils.utils import *
import pygame


class Game:

    def __init__(self):
        self.board = None
        self.current_player = None

    def load_from_fen(self, fen: str = INITIAL_FEN) -> None:
        fen_info = fen_to_squares(fen, full_info=True)
        squares_from_fen = fen_info.get("squares")

        self.current_player = fen_info.get("activeColor")

        squares = list()
        for square_dict in squares_from_fen:
            square = Square(**square_dict)
            squares.append(square)

        board = Board()
        board.grid = squares

        self.board = board

    @property
    def display_on_console(self):
        current_row = 7
        board_string = "|"
        for square in self.board.grid:
            if square.pos[1] < current_row:
                board_string = board_string[:-1]
                board_string += "\n|"
                current_row -= 1
            if square.current_piece is None:
                board_string += " " + "|\t|"
            else:
                board_string += str(square.current_piece) + "|\t|"
            pass
        return board_string[:-2]

    def display_board(self, surface: pygame.Surface):
        for square in self.board.grid:
            self.display_square(surface, square)
            if square.is_occupied:
                self.display_piece(surface, square)

    @staticmethod
    def display_piece(surface: pygame.Surface, square: Square):

        piece = square.current_piece
        piece_image_name = IMAGE_MAP.get(piece.name)
        image_path = "/home/tessitore/PyChess/images/Sprites/" + piece_image_name
        image = pygame.image.load(image_path).convert_alpha()
        scaled_image = pygame.transform.scale(image, piece.size)

        image_rect = piece.rect

        surface.blit(scaled_image, image_rect)

    @staticmethod
    def display_square(surface: pygame.Surface, square: Square):
        pygame.draw.rect(surface, square.get_rect_color, square.rect)
