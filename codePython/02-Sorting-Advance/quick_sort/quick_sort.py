"""
快速排序算法（升序）
"""
import random


def sort(lst):
    """
    对序列所有元素进行随机排序
    """
    random.shuffle(lst)
    _sort(lst, 0, len(lst) - 1)


def _sort(lst, l, r):
    """
    快速排序
    """
    if r <= l:
        return
    p = _partition(lst, l, r)  # 切分
    _sort(lst, l, p - 1)  # 将左半部分 lst[l...p-1] 排序
    _sort(lst, p + 1, r)  # 将右半部分 lst[p+1...r] 排序


def _partition(lst, l, r):
    """
    将序列切分为 lst[l...p-1], lst[p], lst[p+1, r]
    """
    v = lst[l]
    j = l
    for i in range(l + 1, r + 1):
        if lst[i] < v:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[l], lst[j] = lst[j], lst[l]
    return j

