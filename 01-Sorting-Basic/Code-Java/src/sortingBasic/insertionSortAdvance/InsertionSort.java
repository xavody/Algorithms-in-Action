package sortingBasic.insertionSortAdvance;

import java.util.Arrays;

/**
 * 优化后插入排序（升序）
 */
public class InsertionSort {
    public static void newSort(Comparable[] arr) {
        for (int i = 1; i < arr.length; i++) {
            Comparable e = arr[i];
            int j = i;
            for (; j > 0 && e.compareTo(arr[j - 1]) < 0; j--)
                arr[j] = arr[j - 1];
            arr[j] = e;
        }
    }
}
