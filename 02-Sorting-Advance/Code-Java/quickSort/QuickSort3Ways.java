package sortingAdvance.quickSort;

import edu.princeton.cs.algs4.StdRandom;

/**
 * 三路快速排序算法
 */
public class QuickSort3Ways {
    public static void newSort(Comparable[] arr) {
        //对序列所有元素进行随机排序
        StdRandom.shuffle(arr);

        newSort(arr, 0, arr.length - 1);
    }

    public static void newSort(Comparable[] arr, int l, int r) {
        if (l >= r) return;
        int lt = l, i = l + 1, gt = r + 1;
        Comparable v = arr[l];

        while (i < gt) {
            int cmp = arr[i].compareTo(v);
            if (cmp < 0) swap(arr, ++lt, i++);
            else if (cmp > 0) swap(arr, --gt, i);
            else i++;
        }
        swap(arr, l, lt);
        newSort(arr, l, lt - 1); //将左半部分 arr[l...p-1] 排序
        newSort(arr, gt, r); //将右半部分 arr[p+1...r] 排序
    }

    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
