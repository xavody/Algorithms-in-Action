"""
随机生成数值型数组
"""

from .insertion_sort import sort as sort_ins
from .selection_sort import sort as sort_sel
import random
import time


def new_array(n, min_range, max_range):
    """生成 n 个元素的整型（浮点型）数组，每个元素取值范围为 [minRange, maxRange]"""
    assert min_range <= max_range  #使用断言检查 minRange 是否不大于 maxRange
    arr = []
    for i in range(n):
        # 生成一个指定范围内的整数
        temp = random.randint(min_range, max_range)

        # 生成一个指定范围内的浮点数
        # arr[i] = random.uniform(min_range, max_range)

        arr.append(temp)
    return arr


def is_sorted(arr):
    """判断数组排序后是否有序"""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def test_sort(arr1, arr2):
    """测试排序算法运行的正确性及所用时间"""
    begin_time_1 = time.time()
    sort_ins(arr1)
    end_time_1 = time.time()
    assert is_sorted(arr1)  # 使用断言检查排序算法运行成功
    print("插入排序结果: " + str(arr1))
    print("插入排序算法所用时间: " + str(end_time_1 - begin_time_1) + 's')

    print()
    begin_time_2 = time.time()
    sort_sel(arr2)
    end_time_2 = time.time()
    assert is_sorted(arr2)  # 使用断言检查排序算法运行成功
    print("选择排序结果: " + str(arr2))
    print("选择排序算法所用时间: " + str(end_time_2 - begin_time_2) + 's')
