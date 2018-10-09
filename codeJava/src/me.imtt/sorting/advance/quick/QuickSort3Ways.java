package me.imtt.sorting.advance.quick;

/**
 * 三路快速排序算法
 */
public class QuickSort3Ways {
    public static void sort(Comparable[] arr) {
        sort(arr, 0, arr.length - 1);
    }

    private static void sort(Comparable[] arr, int l, int r) {
        if (l >= r) {
            return;
        }

        int lt = l, i = l + 1, gt = r + 1;
        Comparable v = arr[l];

        while (i < gt) {
            int cmp = arr[i].compareTo(v);
            if (cmp < 0) {
                swap(arr, ++lt, i++);
            } else if (cmp > 0) {
                swap(arr, --gt, i);
            } else {
                i++;
            }
        }
        swap(arr, l, lt);

        //将左半部分 arr[l...p-1] 排序
        sort(arr, l, lt - 1); 

        //将右半部分 arr[p+1...r] 排序
        sort(arr, gt, r); 
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
