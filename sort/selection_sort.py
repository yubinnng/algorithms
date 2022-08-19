"""
选择排序
@author : qiyubing
@date : 2020-06-08
"""
# 111 5 7 1 4 3 2 1
arr = list(map(int, input("请输入要排序的数，空格分隔：").split(" ")))
n = len(arr)
for i in range(n): # 待插入位，从0至倒数第二位
    min_idx = i # 初始化最小为第一个元素
    # find min
    for j in range(i + 1, n): # 查找最小元素
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i] # 将最小值交换到待插入位
print(arr)