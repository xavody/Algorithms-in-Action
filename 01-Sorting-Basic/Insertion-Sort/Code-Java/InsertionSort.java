package sortingBasic.insertionSort;

import java.util.Arrays;

/**
 * 插入排序（升序）
 */
public class InsertionSort {
    public static void newSort(Comparable[] arr) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0 && arr[j].compareTo(arr[j - 1]) < 0; j--)
                swap(arr, j, j - 1);
        }
    }
    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    //选择排序算法测试
    public static void main(String[] args) {
        Integer[] integers = SortTestHelper
                .generateRandomArray(10, 0, 1000);
        newSort(integers);
        System.out.println(Arrays.toString(integers));
    }
}
