"""
测试优化后的插入排序算法并与选择排序算法比较
"""

import copy
from sorting_basic.insertion_sort.sort_test_helper import new_array, test_sort

arr1 = new_array(100, 3, 100000)
arr2 = copy.deepcopy(arr1)
print("插入排序初始数组：" + str(arr1))
test_sort(arr1, arr2)