"""
冒泡排序（升序）
"""


def sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        flag = True
        for j in range(0, i):
            if arr[j + 1] < arr[j]:
                flag = False
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
        if flag:
            break
