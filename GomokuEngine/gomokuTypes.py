from enum import IntEnum

class Player(IntEnum):
    WHITE = -1
    EMPTY = 0
    BLACK = 1

    @property
    def other(self):
        return Player.BLACK if self == Player.WHITE else Player.WHITE

DIM = 15
MAX_TURNS = DIM**2