"""
极大极小值算法 井字棋对弈
参考资料：https://blog.csdn.net/qq_36336522/article/details/79408922
@author : qiyubing
@date : 2020-05-27
"""
import copy

# 最大最小常量
MAX = 9999
MIN = -9999

# AI棋子类型
chess_ai = 'x'
# 玩家棋子类型
chess_player = 'o'


# 选择另一个棋子
def the_other(chess_type):
    if chess_type is chess_ai:
        return chess_player
    else:
        return chess_ai


class Chessboard:
    # 棋局数据
    data = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]

    border = '|-|-|-|'
    line_template = '|{0}|{1}|{2}|\n'

    def print(self):
        """
        打印棋盘
        """
        line_template = '| {0} | {1} | {2} |\n'
        print_str = '当前棋盘：\n'
        for line in self.data:
            print_str += line_template.format(line[0], line[1], line[2])
        print(print_str)

    def get_empty_psts(self):
        """
        获取空位置列表
        :return: [(x1,y1), (x2,y2)]
        """
        empty_pst = []
        for row in range(3):
            for col in range(3):
                if self.data[row][col] is ' ':
                    empty_pst.append((row, col))
        return empty_pst

    def copy_new(self):
        """
        深拷贝一个新的棋盘
        :return:
        """
        new_board = Chessboard()
        new_board.data = copy.deepcopy(self.data)
        return new_board

    def can_put(self, row, col) -> bool:
        """
        此处为空可以放置棋子
        :return:
        """
        return self.data[row][col] is ' '

    def put_chess(self, chess_type, row, col):
        """
        放置棋子
        :param chess_type
        :param row: 行数，如0 1 2
        :param col: 列数，如0 1 2
        """
        if not self.can_put(row, col):
            raise RuntimeError("{0},{1}不可放置棋子".format(row, col))
        self.data[row][col] = chess_type

    def can_win(self):
        """
        判断获胜
        :return: 是否有人获胜, 获胜棋子类型
        """

        def check_row(chess_type):
            """
            检查横向是否获胜
            """
            for row in range(3):
                row_status = True
                for col in range(3):
                    if self.data[row][col] is not chess_type:
                        row_status = False
                if row_status is True:
                    # print("横向 '%s' 棋子获胜" % chess_type)
                    return True
            return False

        def check_col(chess_type):
            """
            检查纵向是否获胜
            """
            for col in range(3):
                col_status = True
                for row in range(3):
                    if self.data[row][col] is not chess_type:
                        col_status = False
                if col_status is True:
                    # print("纵向 '%s' 棋子获胜" % chess_type)
                    return True
            return False

        def check_diag(chess_type):
            """
            检查对角是否获胜
            """
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

        # 两种棋子类型都需要判断
        ai_can_win = check_row(chess_ai) or check_col(chess_ai) or check_diag(chess_ai)
        player_can_win = check_row(chess_player) or check_col(chess_player) or check_diag(chess_player)
        if ai_can_win:
            return True, chess_ai
        elif player_can_win:
            return True, chess_player

        empty_num = 0
        for row in range(3):
            for col in range(3):
                if self.data[row][col] is ' ':
                    empty_num += 1
        # 若棋盘已经满了，则平局
        if empty_num is 0:
            return False, 'both'
        else:
            return False, None


def cal_win_value(chessboard: Chessboard):
    """
    计算当前棋盘AI的得分（AI能赢解个数减去玩家能赢的解个数）
    :param chess_type 要判断的棋子种类
    """
    # 如果用户直接可以赢，则得分无穷小，采取防守策略
    win, winner_chess = chessboard.can_win()
    if not win and winner_chess is 'both':
        print("游戏结束！平局")
        exit()
    elif win and winner_chess is chess_player:
        return MIN

    num_map = {
        chess_ai: 0,
        chess_player: 0
    }

    # 分别计算当前棋局AI以及玩家能赢的解有多少种
    for chess_type in [chess_ai, chess_player]:
        temp_board = chessboard.copy_new()

        # 将空位全部填充为某一类型的棋子
        for row in range(3):
            for col in range(3):
                if temp_board.data[row][col] is not the_other(chess_type):
                    temp_board.data[row][col] = chess_type
        # 计算横向可以赢的个数
        for row in range(3):
            row_status = True
            for col in range(3):
                if temp_board.data[row][col] is not chess_type:
                    row_status = False
            if row_status is True:
                num_map[chess_type] += 1
        # 计算纵向可以赢的个数
        for col in range(3):
            col_status = True
            for row in range(3):
                if temp_board.data[row][col] is not chess_type:
                    col_status = False
            if col_status is True:
                num_map[chess_type] += 1
        # 检查主对角线可以赢的个数
        main_diag_status = True
        for i in range(3):
            if temp_board.data[i][i] is not chess_type:
                main_diag_status = False
        if main_diag_status is True:
            num_map[chess_type] += 1
        # 检查副对角线可以赢的个数
        para_diag_status = True
        for i in range(3):
            if temp_board.data[2 - i][i] is not chess_type:
                para_diag_status = False
        if para_diag_status is True:
            num_map[chess_type] += 1
    return num_map[chess_ai] - num_map[chess_player]


def cal_total_value(chessboard: Chessboard, x_ai, y_ai):
    """
    计算将要进行的一步棋的总得分
    """
    total_value = 0
    # win, winner_chess = chessboard.can_win()
    # if win and winner_chess is chess_ai:
    #     return MAX
    # elif win and winner_chess is chess_player:
    #     return -MIN

    # 新建一个临时的棋盘，模拟之后的两步
    temp_board = chessboard.copy_new()

    if temp_board.can_put(x_ai, y_ai):
        # AI走一步
        temp_board.put_chess(chess_ai, x_ai, y_ai)
        # AI可以绝杀
        win, winner_chess = temp_board.can_win()
        if win:
            return MAX
        # 若不能绝杀，则需要预测玩家，计算最大得分的解
        empty_psts = chessboard.get_empty_psts()
        # 遍历所有空位置，模拟玩家走一步
        for x_player, y_player in empty_psts:
            inner_temp_board = temp_board.copy_new()

            if inner_temp_board.can_put(x_player, y_player):
                # 玩家走一步
                inner_temp_board.put_chess(chess_player, x_player, y_player)
                # 计算当前棋盘的得分
                value = cal_win_value(inner_temp_board)
                total_value += value
    return total_value


def ai_put(chessboard: Chessboard):
    """
    AI放置一枚棋子
    :param chessboard:
    :return:
    """
    empty_psts = chessboard.get_empty_psts()
    max_value = MIN
    for row, col in empty_psts:
        value = cal_total_value(chessboard, row, col)
        if value > max_value:
            max_value = value
            determined_x = row
            determined_y = col
    chessboard.put_chess(chess_ai, determined_x, determined_y)


def player_put(chessboard: Chessboard):
    """
    用户放置一枚棋子
    :param chessboard:
    :return:
    """
    while True:
        try:
            row, col = map(int, input("请输入要放置棋的坐标：").split(','))
            chessboard.put_chess(chess_player, row, col)
            break
        except:
            print("输入有误!")
            pass


def play():
    """
    井字棋主程序
    :return:
    """
    chessboard = Chessboard()
    chessboard.print()
    print("AI为 'o' 棋，玩家为 'x' 棋，玩家先")
    print("放置棋子输入格式：行号,列号（数值为0/1/2）")
    while True:
        # 用户走一步
        player_put(chessboard)
        chessboard.print()
        win, winner_chess = chessboard.can_win()
        if win:
            break

        # AI走一步
        print("AI进行下一步...")
        ai_put(chessboard)
        chessboard.print()
        win, winner_chess = chessboard.can_win()
        if win:
            break
    print("游戏结束！%s棋 胜利" % winner_chess)


if __name__ == '__main__':
    play()
