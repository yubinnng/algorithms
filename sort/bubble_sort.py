"""
冒泡排序
@author : qiyubing
@date : 2020-06-08
"""
num_list = [int(n) for n in input("请输入要排序的数，空格分隔：").split(" ")]

for i in range(1, len(num_list)):
    for j in range(len(num_list) - i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

print(num_list)
