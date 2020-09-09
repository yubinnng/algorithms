import numpy as np
from config import *


class Board():
    def __init__(self, player_type=None, data=None):
        super().__init__()
        self.board_size = 15
        self.piece_types = [1, 2]
        self.steps = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        if data == None:
            assert player_type != None
            self.data = np.zeros((self.board_size, self.board_size), dtype=int)
            self.player_type = player_type
            self.ai_type = self.another(player_type)
        else:
            self.data = data

    def another(self, type):
        assert type == BLACK_PIECE or type == WHITE_PIECE
        if type == BLACK_PIECE:
            return WHITE_PIECE
        else:
            return BLACK_PIECE

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
        new_board.player_type = self.player_type
        new_board.ai_type = self.ai_type
        return new_board

    def can_put(self, x, y) -> bool:
        """
        可以放置棋子
        """
        return self.in_range(x, y) and self.data[x, y] == 0

    def put(self, x, y, type):
        assert self.can_put(x, y)
        assert type == 1 or type == 2
        self.data[x, y] = type

    def check_row(self):
        """
        检查横向是否获胜
        :returns: can win, winner type
        """
        for type in self.piece_types:
            for line in self.data:
                for x in range(11):
                    if (line[x:x + 5] == type).all():
                        return True, type
        return False, None

    def check_col(self):
        """
        检查纵向是否获胜
        :returns: can win, winner type
        """
        for type in self.piece_types:
            for line in self.data.T:
                for y in range(11):
                    if (line[y:y + 5] == type).all():
                        return True, type
        return False, None

    def check_diag(self):
        """
        检查对角是否获胜
        """
        for type in self.piece_types:
            # 主对角线
            status = True
            for i in range(3):
                if self.data[i][i] is not chess_type:
                    status = False
            if status is True:
                # print("主对角线 '%s' 棋子获胜" % chess_type)
                return True
            # 副对角线
            status = True
            for i in range(3):
                if self.data[2 - i][i] is not chess_type:
                    status = False
            if status is True:
                # print("副对角线 '%s' 棋子获胜" % chess_type)
                return True
            return False

    def check_win(self, x, y, type):
        """
        判断获胜
        :return: True: win, False: loss, None: not sure
        """
        assert self.can_put(x, y)
        for step_x, step_y in self.steps:
            temp = [type]
            for n in range(1, 6):
                next_x = x + n * step_x
                next_y = y + n * step_y
                if self.in_range(next_x, next_y):
                    temp.append(self.data[next_x, next_y])

            if len(temp) == 5 and (np.array(temp) == type).all():
                return True, type
            if len(temp) > 5:
                if (np.array(temp[:-1]) == type).all():
                    return True
                elif (np.array(temp) == type).all():
                    return False
        return None

    def evaluate(self, color):
        score = 0



    def cal_score(self, x, y):
        """
        AI的得分（AI能赢解个数减去玩家能赢的解个数）
        :param chess_type 要判断的棋子种类
        """
        winner = self.check_win(x, y, self.ai_type)
        if winner != None:
            if winner == self.player_type:
                # 如果用户直接可以赢，则得分无穷小，采取防守策略
                return MIN
            elif winner == self.ai_type:
                return MAX

        score_map = {
            'ai': 0,
            'player': 0
        }

        # 分别计算当前棋局AI以及玩家能赢的解有多少种
        for type in [self.ai_type, self.player_type]:
            temp_board = self.copy_new()

            # 将空位全部填充为某一类型的棋子
            for row in range(3):
                for col in range(3):
                    if temp_board.data[row][col] is not the_other(type):
                        temp_board.data[row][col] = type
            # 计算横向可以赢的个数
            for row in range(3):
                row_status = True
                for col in range(3):
                    if temp_board.data[row][col] is not type:
                        row_status = False
                if row_status is True:
                    num_map[type] += 1
            # 计算纵向可以赢的个数
            for col in range(3):
                col_status = True
                for row in range(3):
                    if temp_board.data[row][col] is not type:
                        col_status = False
                if col_status is True:
                    num_map[type] += 1
            # 检查主对角线可以赢的个数
            main_diag_status = True
            for i in range(3):
                if temp_board.data[i][i] is not type:
                    main_diag_status = False
            if main_diag_status is True:
                num_map[type] += 1
            # 检查副对角线可以赢的个数
            para_diag_status = True
            for i in range(3):
                if temp_board.data[2 - i][i] is not type:
                    para_diag_status = False
            if para_diag_status is True:
                num_map[type] += 1
        return num_map[chess_ai] - num_map[chess_player]

    # # 两种棋子类型都需要判断
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
