# from utils.utils import fen_to_squares, squares_to_fen
# from config import BOARD_SIZE
# import unittest
#
#
# class TestFenConversion(unittest.TestCase):
#
#     def test_fen_to_squares(self):
#         fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
#         squares = fen_to_squares(fen)
#         expected_result = [
#             {
#                 "pos": (0, 0),
#                 "color": 1,
#                 "current_piece": "r"
#             },
#             {
#                 "pos": (1, 0),
#                 "color": 1,
#                 "current_piece": "n"
#             },
#             {
#                 "pos": (2, 0),
#                 "color": 1,
#                 "current_piece": "b"
#             },
#             {
#                 "pos": (3, 0),
#                 "color": 1,
#                 "current_piece": "q"
#             },
#             {
#                 "pos": (4, 0),
#                 "color": 1,
#                 "current_piece": "k"
#             },
#             {
#                 "pos": (5, 0),
#                 "color": 1,
#                 "current_piece": "b"
#             },
#             {
#                 "pos": (6, 0),
#                 "color": 1,
#                 "current_piece": "n"
#             },
#             {
#                 "pos": (7, 0),
#                 "color": 1,
#                 "current_piece": "r"
#             },
#             {
#                 "pos": (0, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (1, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (2, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (3, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (4, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (5, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (6, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (7, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (0, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 4),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (5, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (1, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (2, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (3, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (4, 6),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (6, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (7, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (0, 7),
#                 "color": 0,
#                 "current_piece": "R"
#             },
#             {
#                 "pos": (1, 7),
#                 "color": 0,
#                 "current_piece": "N"
#             },
#             {
#                 "pos": (2, 7),
#                 "color": 0,
#                 "current_piece": "B"
#             },
#             {
#                 "pos": (3, 7),
#                 "color": 0,
#                 "current_piece": "Q"
#             },
#             {
#                 "pos": (4, 7),
#                 "color": 0,
#                 "current_piece": "K"
#             },
#             {
#                 "pos": (5, 7),
#                 "color": 0,
#                 "current_piece": "B"
#             },
#             {
#                 "pos": (6, 7),
#                 "color": 0,
#                 "current_piece": "N"
#             },
#             {
#                 "pos": (7, 7),
#                 "color": 0,
#                 "current_piece": "R"
#             }
#         ]
#
#         self.assertTrue(len(squares) == BOARD_SIZE ** 2, msg="square list does not have the same size as the board")
#         self.assertTrue(squares == expected_result, msg="squares do not represent FEN notation correctly")
#
#         # my_fen = squares_to_fen(squares)
#         #
#         # print(fen.split(" ")[0])
#         # print(my_fen)
#         #
#         # if fen.split(" ")[0] == my_fen:
#         #     print(True)
#         # else:
#         #     print(False)
#
#     def test_squares_to_fen(self):
#         squares = [
#             {
#                 "pos": (0, 0),
#                 "color": 1,
#                 "current_piece": "r"
#             },
#             {
#                 "pos": (1, 0),
#                 "color": 1,
#                 "current_piece": "n"
#             },
#             {
#                 "pos": (2, 0),
#                 "color": 1,
#                 "current_piece": "b"
#             },
#             {
#                 "pos": (3, 0),
#                 "color": 1,
#                 "current_piece": "q"
#             },
#             {
#                 "pos": (4, 0),
#                 "color": 1,
#                 "current_piece": "k"
#             },
#             {
#                 "pos": (5, 0),
#                 "color": 1,
#                 "current_piece": "b"
#             },
#             {
#                 "pos": (6, 0),
#                 "color": 1,
#                 "current_piece": "n"
#             },
#             {
#                 "pos": (7, 0),
#                 "color": 1,
#                 "current_piece": "r"
#             },
#             {
#                 "pos": (0, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (1, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (2, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (3, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (4, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (5, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (6, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (7, 1),
#                 "color": 1,
#                 "current_piece": "p"
#             },
#             {
#                 "pos": (0, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 2),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 3),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 4),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (5, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 4),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (1, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (2, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (3, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (4, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (6, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (7, 5),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (0, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (1, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (2, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (3, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (4, 6),
#                 "color": None,
#                 "current_piece": None
#             },
#             {
#                 "pos": (5, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (6, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (7, 6),
#                 "color": 0,
#                 "current_piece": "P"
#             },
#             {
#                 "pos": (0, 7),
#                 "color": 0,
#                 "current_piece": "R"
#             },
#             {
#                 "pos": (1, 7),
#                 "color": 0,
#                 "current_piece": "N"
#             },
#             {
#                 "pos": (2, 7),
#                 "color": 0,
#                 "current_piece": "B"
#             },
#             {
#                 "pos": (3, 7),
#                 "color": 0,
#                 "current_piece": "Q"
#             },
#             {
#                 "pos": (4, 7),
#                 "color": 0,
#                 "current_piece": "K"
#             },
#             {
#                 "pos": (5, 7),
#                 "color": 0,
#                 "current_piece": "B"
#             },
#             {
#                 "pos": (6, 7),
#                 "color": 0,
#                 "current_piece": "N"
#             },
#             {
#                 "pos": (7, 7),
#                 "color": 0,
#                 "current_piece": "R"
#             }
#         ]
#         expected_fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR"
#
#         fen = squares_to_fen(squares)
#         self.assertTrue(fen == expected_fen, msg="Generated FEN is not as expected")
