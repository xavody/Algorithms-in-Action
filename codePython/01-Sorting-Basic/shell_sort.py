"""
希尔排序（升序）
"""


def sort(arr):
    n = len(arr)
    h = n // 2

    while h > 0:
        for i in range(h, n):
            temp = arr[i]
            j = i
            while j >= h and temp < arr[j - h]:
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h //= 2
