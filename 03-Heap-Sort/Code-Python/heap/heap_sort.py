"""
原地堆排序，索引从0开始
"""
from random import randint


def sort(lst):
    """
    不使用额外的堆排序，直接对 lst 进行原地堆排序
    最后一个非叶子节点的索引 = (最后一个元素的索引-1)/2
    最后一个元素的索引 = n-1
    """
    n = len(lst)
    for i in range((n - 1) // 2, -1, -1):
        shift_down(lst, n, i)

    for i in range(n - 1, -1, -1):
        lst[0], lst[i] = lst[i], lst[0]
        shift_down(lst, i, 0)


def shift_down(lst, n, k):
    """
    由上至下的堆有序化，保证最大堆的性质
    """
    e = lst[k]
    while k * 2 + 1 < n:
        j = k * 2 + 1
        if j + 1 < n and lst[j] < lst[j + 1]:
            j += 1
        if e > lst[j]:
            break
        lst[k] = lst[j]
        k = j
    lst[k] = e


if __name__ == '__main__':
    lst = [randint(10, 100) for _ in range(0, 30)]
    print(lst)
    sort(lst)
    print(lst)
