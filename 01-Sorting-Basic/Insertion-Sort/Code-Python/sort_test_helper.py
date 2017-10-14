"""
随机生成数值型数组
"""

from insertion_sort import sort
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


def test_sort(arr):
    """测试排序算法运行的正确性及所用时间"""
    begin_time = time.time()
    sort(arr)
    end_time = time.time()
    assert is_sorted(arr)  # 使用断言检查排序算法运行成功
    print("排序结果: " + str(arr))
    print("排序算法所用时间: " + str(end_time - begin_time) + 's')
