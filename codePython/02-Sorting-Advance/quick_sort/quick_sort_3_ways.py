"""
三路快速排序算法（升序）
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
    v = lst[l]

    lt = l  # lst[l+1...lt] < v
    i = l + 1  # lst[lt+1...i] = v
    gt = r + 1  # lst[i+1...h] > v

    while i < gt:
        if lst[i] < v:
            lst[lt + 1], lst[i] = lst[i], lst[lt + 1]
            i += 1
            lt += 1
        elif lst[i] > v:
            lst[gt - 1], lst[i] = lst[i], lst[gt - 1]
            gt -= 1
        else:
            i += 1
    lst[l], lst[lt] = lst[lt], lst[l]
    _sort(lst, l, lt - 1)  # 将前半部分 lst[l...lt-1] 排序
    _sort(lst, gt, r)  # 将后半部分 lst[gt...r] 排序

