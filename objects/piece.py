from dataclasses import dataclass
from utils.utils import *
import json


@dataclass
class Piece:
    name: str
    pos: tuple
    color: int

    def __post_init__(self):
        file = open("/home/tessitore/PyChess/objects/piecesInfo.json")
        name = self.name.lower()
        self._piece_rules = json.load(file).get(name)

    def __repr__(self):
        return str(self.name)

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

            all_possible_moves.extend(possible_moves)

        # set function remove duplicates
        return list(set(all_possible_moves))

    def calculate_next_valid_move(self, move: tuple) -> tuple:
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
