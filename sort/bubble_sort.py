"""
冒泡排序
@author : qiyubing
@date : 2020-06-08
"""
# 111 5 7 1 4 3 2 1
arr = list(map(int, input("请输入要排序的数，空格分隔：").split(" ")))
n = len(arr)
for i in range(n):
    for j in range(n - i - 1): # 低位，从0至倒数第二位
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j] # swap
print(arr)
