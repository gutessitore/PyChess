from config import *
import numpy
import math

numpy.seterr(divide='ignore', invalid='ignore')


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


def fen_to_squares(fen: str, full_info: bool = False) -> list or dict:
    fen_components = fen.split(" ")
    piece_placement = fen_components[0]
    active_color = fen_components[1]
    castling_availability = fen_components[2]
    en_passant = fen_components[3]
    halfmove_clock = fen_components[4]
    fullmove_number = fen_components[5]

    rows = piece_placement.split("/")

    squares = list()
    current_file = 7
    for row in rows:
        current_rank = 0
        for piece in row:
            if not is_int(piece):
                pos = (current_rank, current_file)
                piece_name = piece
                color = WHITE if piece_name.islower() else BLACK
                square = dict(pos=pos, color=color, current_piece=piece_name)
                squares.append(square)
                current_rank += 1
            else:
                for _ in range(int(piece)):
                    pos = (current_rank, current_file)
                    color = None
                    piece_name = None
                    square = dict(pos=pos, color=color, current_piece=piece_name)
                    squares.append(square)
                    current_rank += 1
        current_file -= 1

    if full_info:
        info_dict = {
            "activeColor": active_color,
            "castlingAvailability": castling_availability,
            "enPassant": en_passant,
            "halfmoveClock": halfmove_clock,
            "fullmoveNumber": fullmove_number,
            "squares": squares
        }

        return info_dict

    return squares


def squares_to_fen(squares: [dict]) -> str:
    fen = ""

    empty_squares_on_row = 0
    for square in squares:
        current_rank = square.get("pos")[0]
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


def position_to_rect_cords(pos: tuple, size: tuple) -> list:
    height_width = size
    x_y = multiply_vectors(pos, height_width)
    x_y = [x_y[0], SCREEN_HEIGHT - x_y[1] - SQUARE_PIXEL_SIZE]
    return [*x_y, *height_width]


def toggle_square_temp_color(square, color):
    if square.temp_color is None:
        square.temp_color = color
    else:
        square.temp_color = None


def toggle_red_square(square):
    toggle_square_temp_color(square, RED_SQUARE_COLOR)


def toggle_red_gray(square):
    toggle_square_temp_color(square, GRAY_SQUARE_COLOR)


def toggle_piece_temp_size(piece):
    if piece.temp_size is None:
        piece.temp_size = 220
    else:
        piece.temp_size = None


# Vector operations
def dict_to_tuple(dct: dict) -> tuple:
    return tuple(dct.values())


def subtract_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.subtract(v1, v2))


def add_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.add(v1, v2))


def multiply_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.multiply(v1, v2))


def resize_vector(v1: tuple, multiplier: int) -> tuple:
    return tuple([component * multiplier for component in v1])


def invert_vector(vector: tuple) -> tuple:
    return multiply_vectors(vector, (-1, -1))


def _convert_true_and_false_to_direction(condition: bool) -> int:
    return -1 if condition else 1


def simplify_vector(vector: tuple) -> tuple:
    original_direction = [_convert_true_and_false_to_direction(num < 0) for num in vector]

    simplified_vector = numpy.divide(vector, vector)
    # Convert NaN to 0
    simplified_vector[numpy.isnan(simplified_vector)] = 0
    # Restore vector direction
    simplified_vector = multiply_vectors(simplified_vector, original_direction)
    return tuple([int(val) for val in simplified_vector])


def calculate_position_distance(v1: tuple, v2: tuple) -> int:
    distance_vector = subtract_vectors(v1, v2)
    return int(math.hypot(*distance_vector))
