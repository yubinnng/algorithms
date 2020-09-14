from config import *

class PieceColor():
    def __init__(self, value, text):
        self.value = value
        self.text = text

    def reverse(self):
        if self.value == WHITE_VALUE:
            return BLACK
        elif self.value == BLACK_VALUE:
            return WHITE
        else:
            raise ValueError('illegal color')

    @staticmethod
    def parse(value):
        if not isinstance(value, int):
            value = int(value)

        if value == WHITE_VALUE:
            return WHITE
        elif value == BLACK_VALUE:
            return BLACK
        else:
            raise ValueError('illegal color')

    def __str__(self) -> str:
        return self.text

WHITE = PieceColor(WHITE_VALUE, WHITE_TEXT)
BLACK = PieceColor(BLACK_VALUE, BLACK_TEXT)