"""
选择排序算法测试
"""

from sorting_basic.selection_sort.sort_test_helper import new_array, test_sort

arr = new_array(10, 3, 11)
print("选择排序初始数组：" + str(arr))
test_sort(arr)
