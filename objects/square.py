from dataclasses import dataclass
from objects.piece import Piece
from utils.utils import *
import pygame


@dataclass
class Square:
    pos: tuple
    color: int = None
    current_piece: Piece = None
    temp_color: str = None
    temp_size: int = None

    def __post_init__(self):
        self.color = self._define_color()
        if isinstance(self.current_piece, str):
            self.current_piece = self.define_piece_object(self.current_piece, self.pos)

    def _define_color(self):
        rank = self.pos[0]
        file = self.pos[1]

        if is_even(rank):
            if is_even(file):
                color = BLACK
            else:
                color = WHITE
        elif is_even(file):
            color = WHITE
        else:
            color = BLACK

        return color

    @staticmethod
    def define_piece_object(name, pos):
        color = WHITE if name.islower() else BLACK
        return Piece(name, pos, color)

    @property
    def is_occupied(self) -> bool:
        return True if self.current_piece is not None else False

    @property
    def get_piece(self) -> Piece:
        return self.current_piece

    @property
    def get_rect_color(self) -> str:
        if self.temp_color is not None:
            return self.temp_color
        return WHITE_SQUARE_COLOR if self.color == WHITE else BLACK_SQUARE_COLOR

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(*position_to_rect_cords(self.pos, self.size))

    @property
    def size(self) -> int:
        if self.temp_size is not None:
            return tuple([self.temp_size, self.temp_size])
        return tuple([SQUARE_PIXEL_SIZE, SQUARE_PIXEL_SIZE])

