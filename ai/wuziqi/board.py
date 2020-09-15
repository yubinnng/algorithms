import numpy as np
import time
from common import *


class Board():
    def __init__(self, player_color: PieceColor, data=[]):
        assert isinstance(player_color, PieceColor)
        super().__init__()
        self.board_size = 15
        self.steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.player_color = player_color
        self.ai_color = player_color.reverse()

        if len(data):
            self.data = data
        else:
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)

    def copy(self):
        new_board = Board(self.player_color, data=self.data.copy())
        return new_board

    def empty_indexes(self) -> np.ndarray:
        """
        获取空位置列表
        :return: [[x1,y1], [x2,y2], ...]
        """
        return np.argwhere(self.data == EMPTY_VALUE)

    def in_range(self, row, col) -> bool:
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def can_put(self, row, col) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(row, col) and self.data[row, col] == EMPTY_VALUE

    def put(self, row, col, color):
        assert self.can_put(row, col)
        self.data[row, col] = color.value

    def cal_score(self, piece_list, color: PieceColor) -> int:
        if color == BLACK:
            score_map = score_map_black
        else:
            score_map = score_map_white

        score_sum = 0
        piece_str = ''.join(map(str, piece_list))
        for k, v in score_map.items():
            count = piece_str.count(k)
            score_sum += count * v
        return score_sum

    def evaluate(self, color) -> int:
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

        if color == self.ai_color:
            ai_ratio = 1
            player_ratio = 0.1
        else:
            ai_ratio = 0.1
            player_ratio = 1

        score_sum = 0
        for line in line_list:
            score_sum += self.cal_score(line, self.ai_color) * ai_ratio
            score_sum -= self.cal_score(line, self.player_color) * player_ratio
        return score_sum

    def max(self, depth):
        max = {
            'score': MIN,
            'row': None,
            'col': None
        }

        for row, col in self.empty_indexes():
            temp_board = self.copy()
            temp_board.put(row, col, self.ai_color)

            if depth <= 0:
                temp_score = temp_board.evaluate(self.ai_color)
            else:
                temp_score, _, _ = temp_board.min(depth - 1)

            if temp_score > max['score']:
                max['score'] = temp_score
                max['row'] = row
                max['col'] = col

        return max['score'], max['row'], max['col']

    def min(self, depth):
        max = {
            'score': MIN,
            'row': None,
            'col': None
        }

        for row, col in self.empty_indexes():
            temp_board = self.copy()
            temp_board.put(row, col, self.player_color)
            if depth <= 0:
                temp_score = temp_board.evaluate(self.player_color)
            else:
                temp_score, _, _ = temp_board.max(depth - 1)

            if temp_score > max['score']:
                max['score'] = temp_score
                max['row'] = row
                max['col'] = col

        return 0 - max['score'], max['row'], max['col']

    def min_max(self, depth, color: PieceColor):

        if depth <= 0:
            return self.evaluate(color.reverse()), None, None

        max = {
            'score': MIN,
            'row': None,
            'col': None
        }

        for row, col in self.empty_indexes():
            temp_board = self.copy()
            temp_board.put(row, col, color)
            temp_score, _, _ = temp_board.min_max(depth - 1, color.reverse())

            if temp_score > max['score']:
                max['score'] = temp_score
                max['row'] = row
                max['col'] = col
            #
            # if color == self.ai_color:
            #     alpha = max['score']
            #     beta = beta
            #     if temp_score > beta:
            #         break
            # else:
            #     beta = -max['score']
            #     alpha = alpha
            #     if temp_score < alpha:
            #         break

        return max['score'], max['row'], max['col']

    def proceed(self, player_row, player_col):
        start = time.time()
        if not self.can_put(player_row, player_col):
            return STATUS_CANNOT_PUT, None, None

        self.put(player_row, player_col, self.player_color)
        player_score = self.evaluate(self.player_color)
        if player_score <= -WIN_THRESHOLD:
            return STATUS_PLAYER_WIN, None, None

        ai_score, ai_row, ai_col = self.max(1)
        self.put(ai_row, ai_col, self.ai_color)

        end = time.time()
        print('time cost:', (end - start))

        if ai_score >= WIN_THRESHOLD:
            return STATUS_AI_WIN, int(ai_row), int(ai_col)
        else:
            return STATUS_PLAYING, int(ai_row), int(ai_col)
