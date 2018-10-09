package me.imtt.sorting.basic;

/**
 * 优化后插入排序（升序）
 */
public class InsertionSortAdvance {
    public static void sort(Comparable[] arr) {
        for (int i = 1; i < arr.length; i++) {
            Comparable e = arr[i];
            int j = i;
            for (; j > 0 && e.compareTo(arr[j - 1]) < 0; j--) {
                arr[j] = arr[j - 1];
            }
            arr[j] = e;
        }
    }
}
