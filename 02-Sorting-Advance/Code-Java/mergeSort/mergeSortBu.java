package sortingAdvance.mergeSort;

import java.util.Arrays;

/**
 * 自底向上进行归并排序
 */
public class mergeSortBu {
    private static Comparable[] aux;

    // 进行 lgN 次两两归并
    public static void newSort(Comparable[] arr) {
        int n = arr.length;
        aux = new Comparable[n];
        for (int sz = 1; sz < n; sz += sz) {
            for (int l = 0; l < n - sz; l += sz + sz) {
                // 对于arr[mid] <= arr[mid+1]的情况,不进行merge
                if (arr[l + sz - 1].compareTo(arr[l + sz]) > 0)
                    merge(arr, l, l + sz - 1,
                            Math.min(l + sz + sz - 1, n - 1));
            }
        }
    }

    // 将 arr[l...mid] 和 arr[mid+1...r] 两部分进行归并
    public static void merge(Comparable[] arr, int l, int mid, int r) {
        int i = l;
        int j = mid + 1;

        System.arraycopy(arr, l, aux, l, r - l + 1);

        for (int k = l; k <= r; k++) {
            if (i > mid) arr[k] = aux[j++]; //左半部分元素已经处理完毕
            else if (j > r) arr[k] = aux[i++]; //右半部分元素已经处理完毕
            else if (aux[i].compareTo(aux[j]) < 0) arr[k] = aux[i++];
            else arr[k] = aux[j++];
        }
    }
}
