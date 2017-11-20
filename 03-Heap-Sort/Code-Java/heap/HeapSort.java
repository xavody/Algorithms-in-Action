package heap;

import java.util.Arrays;

/**
 * 原地堆排序，版本三（最优）
 */
public class HeapSort {
    // 不使用额外的堆排序，直接对数组进行原地堆排序
    public static void newSort(Comparable[] arr) {
        // 对数组进行原地堆排序的索引从0开始索引的
        // 最后一个非叶子节点的索引 = (最后一个元素的索引-1)/2
        // 最后一个元素的索引 = n-1
        int n = arr.length;

        for (int i = (n - 1 - 1) / 2; i >= 0; i--)
            shiftDown(arr, n, i);

        for (int i = n - 1; i >= 0; i--) {
            swap(arr, i, 0);
            shiftDown(arr, i, 0);
        }
    }

    // 由上至下的堆有序化，保证最大堆的性质
    private static void shiftDown(Comparable[] arr, int n, int k) {
        Comparable e = arr[k];

        while (k * 2 + 1 < n) {
            int j = k * 2 + 1;
            if (j + 1 < n && arr[j + 1].compareTo(arr[j]) > 0)
                j++;

            if (e.compareTo(arr[j]) > 0)
                break;
            arr[k] = arr[j];
            k = j;
        }

        arr[k] = e;
    }

    //交换堆中两个元素
    private static void swap(Comparable[] arr, int i, int j) {
        Comparable temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
