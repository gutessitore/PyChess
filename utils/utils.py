
from config import *
import numpy


def is_inside_the_board(position: tuple) -> bool:
    rank = position[0]
    file = position[1]
    return not any([rank >= BOARD_SIZE, file >= BOARD_SIZE, rank < 0, file < 0])


def is_even(num: int) -> bool:
    return num % 2 == 0


def is_int(value) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def fen_to_squares(fen: str) -> list:
    fen_components = fen.split(" ")
    piece_placement = fen_components[0]
    active_color = fen_components[1]
    castling_availability = fen_components[2]
    en_passant = fen_components[3]
    halfmove_clock = fen_components[4]
    fullmove_number = fen_components[5]

    rows = piece_placement.split("/")

    squares = list()
    current_rank = 0
    for row in rows:
        current_file = 0
        for piece in row:
            if not is_int(piece):
                pos = (current_rank, current_file)
                piece_name = piece
                color = WHITE if piece_name.islower() else BLACK
                square = dict(pos=pos, color=color, current_piece=piece_name)
                squares.append(square)
                current_file += 1
            else:
                for _ in range(int(piece)):
                    pos = (current_rank, current_file)
                    color = None
                    piece_name = None
                    square = dict(pos=pos, color=color, current_piece=piece_name)
                    squares.append(square)
                    current_file += 1
        current_rank += 1

    return squares


def squares_to_fen(squares: [dict]) -> str:
    fen = ""

    empty_squares_on_row = 0
    for square in squares:
        current_rank = square.get("pos")[1]
        if current_rank == 0:  # Start of each row
            if empty_squares_on_row != 0:
                fen += str(empty_squares_on_row)
            empty_squares_on_row = 0
            fen += "/"

        current_piece = square.get("current_piece")
        if current_piece is None:
            empty_squares_on_row += 1
        else:
            if empty_squares_on_row != 0:
                fen += str(empty_squares_on_row)
                empty_squares_on_row = 0
            fen += current_piece

    return fen[1:]


# Vector operations
def dict_to_tuple(dct: dict) -> tuple:
    return tuple(dct.values())


def subtract_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.subtract(v1, v2))


def add_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.add(v1, v2))


def multiply_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.multiply(v1, v2))
