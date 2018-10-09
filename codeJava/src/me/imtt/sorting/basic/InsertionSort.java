package me.imtt.sorting.basic;

/**
 * 插入排序（升序）
 */
public class InsertionSort {
    public static void sort(Comparable[] arr) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0 && arr[j].compareTo(arr[j - 1]) < 0; j--) {
                swap(arr, j, j - 1);
            }
        }
    }

    /**
     * 交换数组中两个数
     */
    private static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
