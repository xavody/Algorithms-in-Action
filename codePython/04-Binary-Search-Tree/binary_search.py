"""
二分查找算法
"""


def find1(lst, target):
    """
    在有序序列 lst 中, 查找 target
    如果找到 target, 返回相应的索引 index，否则返回 -1
    非递归方法
    """
    l, r = 0, len(lst) - 1
    while l <= r:
        # 防止整形溢出，不使用 mid = (l + r) // 2
        mid = l + (r - l) // 2
        if lst[mid] == target:
            return mid
        if lst[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def find2(lst, target, l, r):
    """递归方法"""
    if l > r:
        return -1
    mid = l + (r - l) // 2
    if lst[mid] == target:
        return mid
    elif lst[mid] > target:
        return find2(lst, target, l, mid - 1)
    else:
        return find2(lst, target, mid + 1, r)

