package sortingAdvance.quickSort;

import edu.princeton.cs.algs4.StdRandom;

/**
 * 快速排序算法
 */
public class QuickSort {
    public static void newSort(Comparable[] arr) {
        //对序列所有元素进行随机排序
        StdRandom.shuffle(arr);

        newSort(arr, 0, arr.length - 1);
    }

    public static void newSort(Comparable[] arr, int l, int r) {
        if (l >= r) return;
        int p = partition(arr, l, r); //切分
        newSort(arr, l, p - 1); //将左半部分 arr[l...p-1] 排序
        newSort(arr, p + 1, r); //将右半部分 arr[p+1...r] 排序
    }

    //将序列切分为 arr[l...p-1], arr[p], arr[p+1, r]
    public static int partition(Comparable[] arr, int l, int r) {
        Comparable v = arr[l];
        int j = l;
        for (int i = l + 1; i <= r; i++) {
            if (arr[i].compareTo(v) < 0) {
                j++;
                swap(arr, i, j);
            }
        }
        swap(arr, l, j);
        return j;
    }

    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
