import numpy as np
from config import *


class PieceColor():
    def __init__(self, value):
        self.value = value

    def reverse(self):
        if self.value == WHITE_VALUE:
            return BLACK_VALUE
        elif self.value == BLACK_VALUE:
            return WHITE_VALUE
        else:
            raise ValueError('illegal color')

    def is_black(self):
        return self.value == BLACK_VALUE

    def __eq__(self, other):
        if isinstance(other, str):
            return self.value == other
        elif isinstance(other, PieceColor):
            return self.value == other.value
        else:
            raise ValueError('illegal type')

    def __str__(self) -> str:
        return self.value


class Board():
    def __init__(self, player_color, data=[]):
        super().__init__()
        self.board_size = 15
        self.steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        assert isinstance(player_color, PieceColor)
        self.now_color = player_color

        if len(data):
            self.data = data
        else:
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)

    def copy(self):
        new_board = Board(self.now_color, data=self.data.copy())
        return new_board

    def empty_indexes(self) -> np.ndarray:
        """
        获取空位置列表
        :return: [[x1,y1], [x2,y2], ...]
        """
        return np.argwhere(self.data == EMPTY_VALUE)

    def in_range(self, x, y) -> bool:
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def can_put(self, x, y) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(x, y) and self.data[x, y] == EMPTY_VALUE

    def put(self, x, y, color: PieceColor):
        assert isinstance(color, PieceColor)
        assert self.can_put(x, y)
        self.data[x, y] = color.value

    def cal_score(self, piece_list):
        if self.now_color.is_black():
            score_map = score_map_black
        else:
            score_map = score_map_white

        score_sum = 0
        piece_str = ''.join(map(str, piece_list))
        for k, v in score_map.items():
            count = piece_str.count(k)
            score_sum += count * v
        return score_sum

    def evaluate(self):
        line_list = []
        # heng
        line_list.extend(self.data.tolist())

        # shu
        line_list.extend(self.data.T.tolist())

        # zhu dui jiao xian shang
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j, j + i])
            line_list.append(temp)

        # zhu dui jiao xian xia
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j + i, j])
            line_list.append(temp)

        # fu dui jiao xian shang
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j, -(j + i + 1)])
            line_list.append(temp)

        # fu dui jiao xian xia
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j + i, -(j + 1)])
            line_list.append(temp)

        score_sum = 0
        for line in line_list:
            score_sum += self.cal_score(line)
        return score_sum

    def min_max(self, depth):

        if depth <= 0:
            return {
                'score': self.evaluate()
            }

        max = {
            'score': MIN,
            'x': None,
            'y': None
        }
        for x, y in self.empty_indexes():
            temp_board = self.copy()
            temp_board.put(x, y, self.now_color)
            temp_max = temp_board.evaluate()

            # reverse color
            temp_board.now_color = self.now_color.reverse()
            temp_min = self.min_max(depth - 1)

            temp_score = temp_max - temp_min['score']

            if temp_score > max['score']:
                max['score'] = temp_score
                max['x'] = x
                max['y'] = y
        return max


b = Board(PieceColor(BLACK_VALUE))
# for i in range(15):
#     b.data[:, i] = i
# b.data[0,0] = 99

# print(b.cal_score([1, 1, 1, 1, 1, 1, 1]))
b.data[0:3, 0] = WHITE_VALUE
# print(b.evaluate(BLACK))
print(b.min_max(1))
# ai_can_win = check_row(chess_ai) or check_col(chess_ai) or check_diag(chess_ai)
# player_can_win = check_row(chess_player) or check_col(chess_player) or check_diag(chess_player)
# if ai_can_win:
#     return True, chess_ai
# elif player_can_win:
#     return True, chess_player
#
# empty_num = 0
# for row in range(3):
#     for col in range(3):
#         if self.data[row][col] is ' ':
#             empty_num += 1
# # 若棋盘已经满了，则平局
# if empty_num is 0:
#     return False, 'both'
# else:
#     return False, None
