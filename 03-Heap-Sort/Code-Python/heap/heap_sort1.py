"""
堆排序，版本一
"""
from random import randint

from .max_heap import MaxHeap


def sort(lst):
    """
    使用最大堆，将所有的元素依次添加到堆中,
    再将所有元素从堆中依次取出来, 即完成了排序（由小到大）
    堆排序的整体时间复杂度为O(nlogn)
    """
    n = len(lst)
    max_heap = MaxHeap(n)
    for i in range(n):
        max_heap.insert(lst[i])
    for i in range(n - 1, -1, -1):
        lst[i] = max_heap.extract_max()


if __name__ == '__main__':
    lst = [randint(10, 100) for _ in range(30)]
    print(lst)
    sort(lst)
    print(lst)
