def cal_score(self, piece_num, empty_num):
    if piece_num == 5:
        return 100000  # 成五
    elif piece_num == 4:
        if empty_num == 2:
            return 10000  # 活四
        elif empty_num == 1:
            return 1000  # 死四
    elif piece_num == 3:
        if empty_num == 2:
            return 1000  # 活三
        elif empty_num == 1:
            return 100
    elif piece_num == 2:
        if empty_num == 2:
            return 100
        elif empty_num == 1:
            return 10
    elif piece_num == 1 and empty_num == 2:
        return 10
    else:
        return 0










#
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

            if len(temp) == 5 and (np.array(temp) == color.value).all():
                return True, color
            if len(temp) > 5:
                if (np.array(temp[:-1]) == color.value).all():
                    return True
                elif (np.array(temp) == color.value).all():
                    return False
        return None