"""
双路快速排序算法
"""


def sort(lst):
    """
    对序列所有元素进行随机排序
    """
    random.shuffle(lst)
    sort_next(lst, 0, len(lst) - 1)


def sort_next(lst, l, r):
    """
    快速排序
    """
    if r <= l:
        return
    p = partition(lst, l, r)  #切分
    sort_next(lst, l, p - 1)  #将左半部分 lst[l...p-1] 排序
    sort_next(lst, p + 1, r)  #将右半部分 lst[p+1...r] 排序


def partition(lst, l, r):
    """
    将序列切分为 lst[l...p-1], lst[p], lst[p+1, r]
    """
    v = lst[l]
    i, j = l, r + 1
    while True:
        i += 1
        j -= 1
        while i <= r and lst[i] < v:
            i += 1
        while j >= l and lst[j] > v:
            j -= 1
        if i >= j:
            break
        lst[i], lst[j] = lst[j], lst[i]
    lst[l], lst[j] = lst[j], lst[l]
    return j

