package sortingBasic.insertionSortAdvance;

import sortingBasic.insertionSort.SortTestHelper;

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

    //插入排序算法测试
    public static void main(String[] args) {
        Integer[] integers = SortTestHelper
                .generateRandomArray(10, 0, 1000);
        newSort(integers);
        System.out.println(Arrays.toString(integers));
    }
}
