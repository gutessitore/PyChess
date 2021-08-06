from config import *
import numpy


def is_inside_the_board(position: tuple) -> bool:
    rank = position[0]
    file = position[1]
    return not any([rank >= BOARD_SIZE, file >= BOARD_SIZE, rank < 0, file < 0])


# Vector operations
def dict_to_tuple(dct: dict) -> tuple:
    return tuple(dct.values())


def subtract_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.subtract(v1, v2))


def add_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.add(v1, v2))


def multiply_vectors(v1: tuple, v2: tuple) -> tuple:
    return tuple(numpy.multiply(v1, v2))
