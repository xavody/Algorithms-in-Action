"""
自底向上进行归并排序（升序）
"""
import copy


def sort(lst):
    """
    进行 lgN 次两两归并
    """
    n = len(lst)
    sz = 1  # sz 子数组大小
    while sz < n:
        l = 0  # l 子数组索引
        while l < n - sz:
            # 对于 lst[mid] <= lst[mid + 1]的情况, 不进行merge
            if lst[l + sz - 1] > lst[l + sz]:
                _merge(lst, l, l + sz - 1, min(l + sz + sz - 1, n - 1))
            l += sz + sz
        sz += sz


def _merge(lst, l, mid, r):
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

