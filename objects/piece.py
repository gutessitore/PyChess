from dataclasses import dataclass
from utils.utils import *
import pygame
import json


@dataclass
class Piece:
    name: str
    pos: tuple
    color: int
    temp_size: int = None
    can_jump: bool = None

    def __post_init__(self):
        file = open("/home/tessitore/PyChess/objects/piecesInfo.json")
        name = self.name.lower()
        self._piece_rules = json.load(file).get(name)
        self.can_jump = self._piece_rules.get("movement").get("canJump")

    def __repr__(self):
        return str(self.name)

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(*position_to_rect_cords(self.pos, self.size))

    @property
    def size(self) -> int:
        if self.temp_size is not None:
            return tuple([self.temp_size, self.temp_size])
        return tuple([SQUARE_PIXEL_SIZE, SQUARE_PIXEL_SIZE])

    @property
    def possible_moves(self) -> list:

        # get piece attributes
        movement_rules = self._piece_rules.get("movement")
        can_move_backwards = movement_rules.get("canMoveBackwards")
        moves = list(map(dict_to_tuple, movement_rules.get("possibilities")))
        is_ranged = movement_rules.get("ranged")

        if can_move_backwards:
            moves = self.add_backward_move_pattern(moves)

        all_possible_moves = list()
        for move in moves:

            valid_move = self.calculate_next_valid_move(move)
            possible_moves = [valid_move]
            if is_ranged:

                # this vector is used to calculate ranged moves
                if valid_move is None:
                    continue
                direction_vector = subtract_vectors(valid_move, self.pos)

                for multiplier in range(1, BOARD_SIZE):
                    distance = multiply_vectors(direction_vector, multiplier)
                    initial_move_plus_distance = add_vectors(valid_move, distance)

                    if is_inside_the_board(initial_move_plus_distance):
                        possible_moves.append(initial_move_plus_distance)

            # if self.color == WHITE:
            #     inverted_moves = [(m[0], -1 * m[1]) for m in possible_moves]
            #     possible_moves = inverted_moves

            all_possible_moves.extend(possible_moves)

        # set function remove duplicates
        return list(set(filter(None, all_possible_moves)))

    def calculate_next_valid_move(self, move: tuple) -> tuple:
        if self.color == WHITE:
            move = (move[0], -1 * move[1])
        next_pos = add_vectors(self.pos, move)
        return next_pos if is_inside_the_board(next_pos) else None

    @staticmethod
    def add_backward_move_pattern(moves: list) -> list:
        move_patterns = list()
        for move in moves:
            backward_move = (move[0], -1 * move[1])
            move_patterns.append(move)
            move_patterns.append(backward_move)
        return move_patterns

    @staticmethod
    def is_able_to_move(current_pos: tuple, future_pos: tuple) -> bool:
        pass
