"""
自顶向下进行归并排序
"""
import copy


def sort(lst):
    """
    初始化，使归并排序边界正确
    """
    sort_next(lst, 0, len(lst) - 1)


def sort_next(lst, l, r):
    """
    使用自顶向下、递归进行归并排序,对 lst[l...r] 的范围进行排序
    """
    if l >= r:
        return
    mid = (l + r) // 2
    sort_next(lst, l, mid)  #将左半部分排序
    sort_next(lst, mid + 1, r)  #将右半部分排序

    # 对于 lst[mid] <= lst[mid + 1]的情况, 不进行merge
    if lst[mid] > lst[mid + 1]:
        merge(lst, l, mid, r)  #归并


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

