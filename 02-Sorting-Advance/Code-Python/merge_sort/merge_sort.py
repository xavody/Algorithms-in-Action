"""
使用递归进行归并排序
"""
import copy
from random import randint


def merge_sort(lst):
    """
    初始化，使归并排序边界正确
    """
    sort(lst, 0, len(lst) - 1)


def sort(lst, l, r):
    """
    使用递归进行归并排序,对 lst[l...r] 的范围进行排序
    """
    if l >= r:
        return
    mid = (l + r) // 2
    sort(lst, l, mid)
    sort(lst, mid + 1, r)
    merge(lst, l, mid, r)


def merge(lst, l, mid, r):
    """
    将 lst[l...mid] 和 lst[mid+1...r] 两部分进行归并
    """
    aux = copy.deepcopy(lst[l:r + 1])
    i, j = l, mid + 1
    for k in range(l, r + 1):
        if i > mid:  # 左半部分元素已经处理完毕
            lst[k] = aux[j - l]
            j += 1
        elif j > r:  # 右半部分元素已经处理完毕
            lst[k] = aux[i - l]
            i += 1
        elif aux[i - l] < aux[j - l]:
            lst[k] = aux[i - l]
            i += 1
        else:
            lst[k] = aux[j - l]
            j += 1


lst = [randint(10, 60) for _ in range(100)]
print(lst)
merge_sort(lst)
print(lst)
