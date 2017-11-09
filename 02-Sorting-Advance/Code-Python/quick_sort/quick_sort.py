"""
快速排序算法
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
    j = l
    for i in range(l + 1, r + 1):
        if lst[i] < v:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]
    lst[l], lst[j] = lst[j], lst[l]
    return j

