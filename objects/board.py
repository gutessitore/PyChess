from objects.square import Square
from utils.utils import *


class Board:
    ranks = [rank for rank in range(8)]
    files = [file for file in range(8)]

    def __init__(self):
        base_grid = [Square((rank, file)) for rank in self.ranks for file in self.files]
        self.grid = base_grid

    @property
    def occupied_squares_pos(self) -> list:
        return [square.pos for square in self.grid if square.is_occupied]

    @property
    def occupied_squares(self) -> list:
        return [square for square in self.grid if square.is_occupied]

    @property
    def squares(self) -> list:
        return [square for square in self.grid]

    def move_piece(self, from_pos: tuple, to_pos: tuple) -> None:
        source_square = next(square for square in self.grid if square.pos == from_pos)
        target_square = next(square for square in self.grid if square.pos == to_pos)

        if not target_square.is_occupied:

            if to_pos in source_square.current_piece.possible_moves:

                if self.move_path_is_clear(from_pos, to_pos):
                    target_square.current_piece = source_square.current_piece
                    source_square.current_piece = None

                else:
                    raise ValueError(f"Piece can't move {source_square} to {target_square}, path blocked")
            else:
                raise ValueError(f"Piece can't move {source_square} to {target_square}, move not allowed")
        else:
            raise ValueError(f"Piece can't move {source_square} to {target_square}, square is occupied")

    def move_path_is_clear(self, from_pos: tuple, to_pos: tuple) -> bool:
        movement_vector = subtract_vectors(to_pos, from_pos)
        simplified_movement_vector = simplify_vector(movement_vector)
        distance = calculate_position_distance(to_pos, from_pos)

        for multiplier in range(1, distance + 1):
            pos_to_check = add_vectors(from_pos, resize_vector(simplified_movement_vector, multiplier))
            if pos_to_check in self.occupied_squares_pos:
                return False

        return True
