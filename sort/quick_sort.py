"""
快速排序
@author : yubing
@date : 2022-08-17
"""

"""
快速排序，不包括right
"""
def quick_sort(arr, left, right):
    if left < right:
        p = partiion(arr, left, right)
        quick_sort(arr, left, p)
        quick_sort(arr, p + 1, right) # p + 1 是为了保证当p为最小时，每次划分都一样导致无限递归

"""
基于支点划分，边界包括left和right
"""
def partiion(arr, left, right):
    p = left # 第一位设为支点
    first_max = p + 1 # 第一位比支点大的元素
    for i in range(p, right + 1): # 从第二位起搜索
        # 如果遇到小于支点的值，则将其与第一位大于支点的值互换位置，这样小的值会在支点左侧，大的值会在支点右侧
        if arr[i] < arr[p]:
            arr[i], arr[first_max] = arr[first_max], arr[i]
            first_max += 1
    # 最后将支点与最后一个小值交换
    arr[p], arr[first_max - 1] = arr[first_max - 1], arr[p]
    return first_max - 1

# 111 5 7 1 4 3 2 1
arr = list(map(int, input("请输入要排序的数，空格分隔：").split(" ")))
quick_sort(arr, 0, len(arr) - 1)
print(arr)