from dataclasses import dataclass
from objects.piece import Piece
from utils.utils import *


@dataclass
class Square:
    pos: tuple
    color: int = None
    current_piece: Piece = None

    def __post_init__(self):
        self.color = self._define_color()
        if isinstance(self.current_piece, str):
            self.current_piece = Piece(self.current_piece, self.pos, 1)

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

    @property
    def is_occupied(self) -> bool:
        return True if self.current_piece is not None else False

