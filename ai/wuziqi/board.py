import numpy as np
from config import *


class Board():
    def __init__(self, player_color=None, data=None):
        super().__init__()
        self.board_size = 15
        self.piece_colors = [1, 2]
        self.steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        if data == None:
            assert player_color != None
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)
            self.player_color = player_color
            self.ai_color = self.another(player_color)
        else:
            self.data = data

    def another(self, color):
        assert color == BLACK or color == WHITE
        if color == BLACK:
            return WHITE
        else:
            return BLACK

    def empty_indexes(self) -> np.ndarray:
        """
        获取空位置列表
        :return: [[x1,y1], [x2,y2], ...]
        """
        return np.argwhere(self.data == 1)

    def in_range(self, x, y) -> bool:
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def copy_new(self):
        new_board = Board(self.data.copy())
        new_board.player_color = self.player_color
        new_board.ai_color = self.ai_color
        return new_board

    def can_put(self, x, y) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(x, y) and self.data[x, y] == 0

    def put(self, x, y, color):
        assert self.can_put(x, y)
        assert color == 1 or color == 2
        self.data[x, y] = color

    def check_row(self):
        """
        检查横向是否获胜
        :returns: can win, winner color
        """
        for color in self.piece_colors:
            for line in self.data:
                for x in range(11):
                    if (line[x:x + 5] == color).all():
                        return True, color
        return False, None

    def check_col(self):
        """
        检查纵向是否获胜
        :returns: can win, winner color
        """
        for color in self.piece_colors:
            for line in self.data.T:
                for y in range(11):
                    if (line[y:y + 5] == color).all():
                        return True, color
        return False, None

    def check_diag(self):
        """
        检查对角是否获胜
        """
        for color in self.piece_colors:
            # 主对角线
            status = True
            for i in range(3):
                if self.data[i][i] is not chess_color:
                    status = False
            if status is True:
                # print("主对角线 '%s' 棋子获胜" % chess_color)
                return True
            # 副对角线
            status = True
            for i in range(3):
                if self.data[2 - i][i] is not chess_color:
                    status = False
            if status is True:
                # print("副对角线 '%s' 棋子获胜" % chess_color)
                return True
            return False

    def check_win(self, x, y, color):
        """
        判断获胜
        :return: True: win, False: loss, None: not sure
        """
        assert self.can_put(x, y)
        for step_x, step_y in self.steps:
            temp = [color]
            for n in range(1, 6):
                next_x = x + n * step_x
                next_y = y + n * step_y
                if self.in_range(next_x, next_y):
                    temp.append(self.data[next_x, next_y])

            if len(temp) == 5 and (np.array(temp) == color).all():
                return True, color
            if len(temp) > 5:
                if (np.array(temp[:-1]) == color).all():
                    return True
                elif (np.array(temp) == color).all():
                    return False
        return None

    def cal_score(self, piece_list):
        score_sum = 0
        piece_str = ''.join(map(str, piece_list))
        for k, v in score_map.items():
            count = piece_str.count(k)
            score_sum += count * v
        return score_sum

    def evaluate(self, color):
        line_list = []
        # line_list.extend(self.data.tolist())
        # line_list.extend(self.data.T.tolist())

        # zhu dui jiao xian shang
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j, j + i])
            # line_list.append(temp)

        # zhu dui jiao xian xia
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j + i, j])
            # line_list.append(temp)

        # fu dui jiao xian shang
        for i in reversed(range(self.board_size)):
            temp = []
            for j in range(i + 1):
                temp.append(self.data[j, i - j])
            # line_list.append(temp)

        # fu dui jiao xian xia
        for i in range(self.board_size):
            temp = []
            for j in range(self.board_size - i):
                temp.append(self.data[j + i, -(j + 1)])
            line_list.append(temp)
        return line_list


b = Board(WHITE)
for i in range(15):
    b.data[:, i] = i
# print(b.cal_score([1, 1, 1, 1, 1, 1, 1]))
print(b.evaluate(WHITE))

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
