package me.imtt.sorting.basic;

/**
 * 希尔排序（升序）
 */
public class ShellSort {
    public static void sort(Comparable[] arr) {
        int length = arr.length;
        int h = 1;
        while (h < length / 3) {
            h = 3 * h + 1;
        }

        for (; h > 0; h /= 3) {
            for (int i = h; i < length; i++) {
                Comparable temp = arr[i];
                int j = i;
                for (; j >= h && temp.compareTo(arr[j - h]) < 0; j -= h) {
                    arr[j] = arr[j - h];
                }

                arr[j] = temp;
            }
        }
    }
}
