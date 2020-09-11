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