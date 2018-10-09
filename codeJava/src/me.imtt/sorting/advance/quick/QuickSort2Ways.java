package me.imtt.sorting.advance.quick;

/**
 * 双路快速排序算法
 */
public class QuickSort2Ways {
    public static void sort(Comparable[] arr) {
        sort(arr, 0, arr.length - 1);
    }

    private static void sort(Comparable[] arr, int l, int r) {
        if (l >= r) {
            return;
        }

        //切分
        int p = partition(arr, l, r); 

        //将左半部分 arr[l...p-1] 排序
        sort(arr, l, p - 1);
        
        //将右半部分 arr[p+1...r] 排序
        sort(arr, p + 1, r); 
    }

    /**
     * 将序列切分为 arr[l...p-1], arr[p], arr[p+1, r]
     */
    private static int partition(Comparable[] arr, int l, int r) {
        Comparable v = arr[l];
        int i = l, j = r + 1;
        while (true) {
            while (arr[++i].compareTo(v) < 0 && i <= r);
            while (arr[--j].compareTo(v) > 0 && j >= l);
            if (i >= j) {
                break;
            }
            swap(arr, i, j);
        }
        swap(arr, l, j);
        return j;
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
