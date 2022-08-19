"""
归并排序
@author : yubing
@date : 2022-08-18
"""
def merge(left, right):
    left_idx = 0
    left_n = len(left)
    right_idx = 0
    right_n = len(right)
    result = []
    while left_idx < left_n and right_idx < right_n: # 当左右都有剩余元素时，将较小的移入result
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result = result + left[left_idx:] + right[right_idx:] # 将剩余元素移入result
    return result
    
def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# 111 5 7 1 4 3 2 1
arr = list(map(int, input("请输入要排序的数，空格分隔：").split(" ")))
arr = merge_sort(arr)
print(arr)
    