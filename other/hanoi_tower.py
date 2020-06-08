"""
汉诺塔
@author : qiyubing
@date : 2020-06-08
"""
towers = {
    1: ['大', '中', '小'],
    2: [],
    3: []
}
print(towers)


def hanoi(n, move_from, move_to, temp):
    if n is 1:
        item = towers[move_from].pop()
        towers[move_to].append(item)
        print("将 %s盘 从 %s号塔 移到 %s号塔" % (item, move_from, move_to))
    else:
        hanoi(n - 1, move_from, temp, move_to)
        hanoi(1, move_from, move_to, temp)
        hanoi(n - 1, temp, move_to, move_from)


hanoi(3, 1, 2, 3)
print(towers)
