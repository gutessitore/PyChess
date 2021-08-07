INITIAL_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

SQUARE_PIXEL_SIZE = 100
BOARD_SIZE = 8
SCREEN_WIDTH = SQUARE_PIXEL_SIZE * BOARD_SIZE
SCREEN_HEIGHT = SQUARE_PIXEL_SIZE * BOARD_SIZE

WHITE = 1
BLACK = 0
WHITE_SQUARE_COLOR = "#EEEED2"
BLACK_SQUARE_COLOR = "#769656"
RED_SQUARE_COLOR = "#EB6150"
GRAY_SQUARE_COLOR = "#CFCFCF"

IMAGE_MAP = {
    "k": "blackKing.png",
    "q": "blackQueen.png",
    "r": "blackRook.png",
    "b": "blackBishop.png",
    "n": "blackKnight.png",
    "p": "blackPawn.png",
    "K": "whiteKing.png",
    "Q": "whiteQueen.png",
    "R": "whiteRook.png",
    "B": "whiteBishop.png",
    "N": "whiteKnight.png",
    "P": "whitePawn.png",
}

LEFT_CLICK = 1
RIGHT_CLICK = 3

DOUBLE_CLICK_TIME = 200