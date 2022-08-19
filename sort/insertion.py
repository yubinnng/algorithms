"""
插入排序
@author : yubing
@date : 2022-08-18
"""
# 111 5 7 1 4 3 2 1
arr = list(map(int, input("请输入要排序的数，空格分隔：").split(" ")))
n = len(arr)
for i in range(1, n): 
    cur_idx = i # 选取待插入数
    for j in range(i - 1, -1, -1): # 从后向前查找已排序数，不断将待插入数向前移动，直到前方的数小于等于它
        if arr[j] > arr[cur_idx]:
            arr[j], arr[cur_idx] = arr[cur_idx], arr[j]
            cur_idx -= 1
        else:
            break
print(arr)
    