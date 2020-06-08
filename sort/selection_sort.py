"""
选择排序
@author : qiyubing
@date : 2020-06-08
"""
result = []
num_list = [int(n) for n in input("请输入要排序的数，空格分隔：").split(" ")]

while len(num_list) is not 0:
    min = 99999
    for i in range(len(num_list)):
        if num_list[i] < min:
            min = num_list[i]
            min_index = i
    result.append(min)
    num_list.pop(min_index)

print(result)
