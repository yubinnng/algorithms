import numpy as np


class Board():
    def __init__(self):
        super().__init__()
        self.data = np.zeros((15, 15), dtype=int)

    def get_empty_psts(self) -> np.ndarray:
        """
        获取空位置列表
        :return: [[x1,y1], [x2,y2], ...]
        """
        return np.argwhere(self.data == 1)

    def is_empty(self, x, y) -> bool:
        """
        此处为空可以放置棋子
        """
        return self.data[x, y] == 0

    def put(self, x, y, type):
        assert self.is_empty(x, y)
        assert type == 1 or type == 2
        self.data[x, y] = type


board = Board()
board.put(1,1,1)
print(board.data)
print(board.get_empty_psts())
print(board.is_empty(1,1))