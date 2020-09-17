import numpy as np
import time
import math
from common import *

class Board():
    leaf_num = 0

    def __init__(self, player_color: PieceColor, data=[]):
        assert isinstance(player_color, PieceColor)
        super().__init__()
        self.board_size = 15
        self.directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1,-1), (1, -1), (-1, 1)]
        self.player_color = player_color
        self.ai_color = player_color.reverse()
        self.candidates = {}

        if len(data):
            self.data = data
        else:
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)

    def copy(self):
        new_board = Board(self.player_color, data=self.data.copy())
        new_board.candidates = self.candidates.copy()
        return new_board

    def in_range(self, row, col) -> bool:
        return 0 <= row < self.board_size and 0 <= col < self.board_size

    def can_put(self, row, col) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(row, col) and self.data[row, col] == EMPTY_VALUE

    def put(self, row, col, color, record=False):
        assert self.can_put(row, col)
        self.data[row, col] = color.value
        self.update_candidates(row, col, record)

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

    def evaluate(self) -> int:
        Board.leaf_num += 1

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
            score_sum += self.cal_score(line, self.ai_color) * 0.5
            score_sum -= self.cal_score(line, self.player_color)
        return score_sum

    @staticmethod
    def l2_distance(v1:tuple, v2:tuple) -> float:
        return math.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def get_candidates(self) -> list:
        return sorted(self.candidates.keys(), key=lambda x: self.candidates[x])

    def update_candidates(self, new_row, new_col, extend):

        if (new_row, new_col) in self.candidates:
            self.candidates.pop((new_row, new_col))
        if extend:
            for i in range(1, 4):
                for dir in self.directions:
                    candi_idx = (new_row + i * dir[0], new_col + i * dir[1])
                    if self.can_put(*candi_idx):
                        self.candidates[candi_idx] = Board.l2_distance(candi_idx, (new_row, new_col))


    def max(self, depth, alpha, beta):
        assert depth % 2 == 0
        max = {
            'score': alpha,
            'row': None,
            'col': None
        }

        for row, col in self.get_candidates():
            temp_board = self.copy()
            temp_board.put(row, col, self.ai_color)

            temp_score, _, _ = temp_board.min(depth - 1, max['score'], beta)

            if temp_score > max['score']:
                max['score'] = temp_score
                max['row'] = row
                max['col'] = col

                if beta <= temp_score:
                    return temp_score, row, col
        return max['score'], max['row'], max['col']

    def min(self, depth, alpha, beta):
        min = {
            'score': beta,
            'row': None,
            'col': None
        }

        for row, col in self.get_candidates():
            temp_board = self.copy()
            temp_board.put(row, col, self.player_color)
            if depth <= 1:
                temp_score = temp_board.evaluate()
            else:
                temp_score, _, _ = temp_board.max(depth - 1, alpha, min['score'])

            if temp_score < min['score']:
                min['score'] = temp_score
                min['row'] = row
                min['col'] = col

                if alpha >= temp_score:
                    return temp_score, row, col

        return min['score'], min['row'], min['col']

    def proceed(self, player_row, player_col):
        start = time.time()
        Board.leaf_num = 0
        if not self.can_put(player_row, player_col):
            return STATUS_CANNOT_PUT, None, None

        self.put(player_row, player_col, self.player_color, record=True)

        score = self.evaluate()
        if score <= LOSS_THRESHOLD:
            return STATUS_PLAYER_WIN, None, None

        score, ai_row, ai_col = self.max(4, MIN, MAX)

        if score <= LOSS_THRESHOLD:
            return STATUS_PLAYER_WIN, None, None

        self.put(ai_row, ai_col, self.ai_color, record=True)

        end = time.time()
        score = self.evaluate()

        print('time cost: %.1f s, score: %d' % (end - start, score))
        print('leaf num: %d' % Board.leaf_num)

        if score >= WIN_THRESHOLD:
            return STATUS_AI_WIN, int(ai_row), int(ai_col)
        else:
            return STATUS_PLAYING, int(ai_row), int(ai_col)
