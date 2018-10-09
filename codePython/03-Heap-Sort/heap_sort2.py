"""
堆排序，版本二
"""

from .max_heap import MaxHeap


def sort(lst1):
    """
    使用最大堆，将 lst 序列通过 MaxHeap 构造函数创建最大堆，
    将所有元素从堆中依次取出来, 即完成了排序（由小到大）
    所有元素依次从堆中取出来的时间复杂度为O(nlogn)
    堆排序的整体时间复杂度为O(nlogn)
    """
    max_heap = MaxHeap(lst=lst1)
    for i in range(len(lst1) - 1, -1, -1):
        lst1[i] = max_heap.extract_max()

