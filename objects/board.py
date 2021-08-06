from objects.square import Square


class Board:
    ranks = [rank for rank in range(8)]
    files = [file for file in range(8)]

    def __init__(self):
        base_grid = [Square((rank, file)) for rank in self.ranks for file in self.files]
        self.grid = base_grid

    @staticmethod
    def move_piece(current_square: Square, to_square: Square) -> None:
        if not to_square.is_occupied:
            to_square.current_piece = current_square.current_piece
            current_square.current_piece = None

