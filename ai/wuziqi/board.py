import numpy as np
import time
import math
from common import *

class Board():
    num = 0
    def __init__(self, player_color: PieceColor, data=[]):
        assert isinstance(player_color, PieceColor)
        super().__init__()
        self.board_size = 15
        self.steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.player_color = player_color
        self.ai_color = player_color.reverse()
        self.prev_step_player = None
        self.prev_step_ai = None
        self.history = []

        if len(data):
            self.data = data
        else:
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)

        self.empty_idx = [(i, j) for i in range(self.board_size) for j in range(self.board_size)]

    def copy(self):
        new_board = Board(self.player_color, data=self.data.copy())
        new_board.empty_idx = self.empty_idx.copy()
        new_board.history = self.history.copy()
        return new_board

    def in_range(self, row, col) -> bool:
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def can_put(self, row, col) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(row, col) and self.data[row, col] == EMPTY_VALUE

    def put(self, row, col, color, record_history=False):
        assert self.can_put(row, col)
        self.data[row, col] = color.value
        self.empty_idx.remove((row, col))
        if record_history:
            self.history.append((row, col, color))

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
            score_sum += self.cal_score(line, self.ai_color)
            score_sum -= self.cal_score(line, self.player_color)
        return score_sum

    @staticmethod
    def l2_distance(v1:tuple, v2:tuple) -> float:
        return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def get_candidates(self) -> list:
        results = {}
        for emp_idx in self.empty_idx:
            for hist_row, hist_col, _ in self.history:
                dist = Board.l2_distance(emp_idx, (hist_row, hist_col))
                if dist == 1 or dist == 2 or dist == 3 or abs(dist - 1.41) < 0.1 or abs(dist - 2.82) < 0.1 or abs(dist - 4.24) < 0.1:
                    results[emp_idx] = dist
        return sorted(results.keys(), key=lambda x: results[x])

    def max(self, depth, beta):
        assert depth % 2 == 0
        max = {
            'score': MIN,
            'row': None,
            'col': None
        }

        for row, col in self.get_candidates():
            temp_board = self.copy()
            temp_board.put(row, col, self.ai_color)

            temp_score, _, _ = temp_board.min(depth - 1, max['score'])

            if temp_score > max['score']:
                max['score'] = temp_score
                max['row'] = row
                max['col'] = col

                if beta <= temp_score:
                    return temp_score, row, col
        return max['score'], max['row'], max['col']

    def min(self, depth, alpha):
        min = {
            'score': MAX,
            'row': None,
            'col': None
        }

        for row, col in self.get_candidates():
            temp_board = self.copy()
            temp_board.put(row, col, self.player_color)
            if depth <= 1:
                temp_score = temp_board.evaluate(self.player_color)
                Board.num += 1
            else:
                temp_score, _, _ = temp_board.max(depth - 1, min['score'])

            if temp_score < min['score']:
                min['score'] = temp_score
                min['row'] = row
                min['col'] = col

                if alpha >= temp_score:
                    return temp_score, row, col

        return min['score'], min['row'], min['col']

    def proceed(self, player_row, player_col):
        start = time.time()
        if not self.can_put(player_row, player_col):
            return STATUS_CANNOT_PUT, None, None

        self.put(player_row, player_col, self.player_color, record_history=True)

        score = self.evaluate(self.player_color)
        if score <= LOSS_THRESHOLD:
            return STATUS_PLAYER_WIN, None, None

        score, ai_row, ai_col = self.max(4, MAX)

        if score <= LOSS_THRESHOLD:
            return STATUS_PLAYER_WIN, None, None

        self.put(ai_row, ai_col, self.ai_color, record_history=True)

        end = time.time()
        score = self.evaluate(self.ai_color)

        print('time cost: %.1f s, score: %d' % (end - start, score))
        print(Board.num)

        if score >= WIN_THRESHOLD:
            return STATUS_AI_WIN, int(ai_row), int(ai_col)
        else:
            return STATUS_PLAYING, int(ai_row), int(ai_col)
