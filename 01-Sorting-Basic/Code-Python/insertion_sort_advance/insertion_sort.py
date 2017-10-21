"""
优化后插入排序算法（升序）
"""


def sort(arr):
    for i in range(1, len(arr)):
        e = arr[i]
        j = i
        while j > 0 and e < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = e
