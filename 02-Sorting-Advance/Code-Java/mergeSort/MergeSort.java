package sortingAdvance.mergeSort;

import sortingAdvance.sortTestHelper.SortTestHelper;

import java.util.Arrays;

/**
 * 使用递归实现归并排序
 */
public class MergeSort {
    public static void newSort(Comparable[] arr) {
        int n = arr.length;
        newSort(arr, 0, n - 1);
    }

    // 使用递归进行归并排序,对 arr[l...r] 的范围进行排序
    public static void newSort(Comparable[] arr, int l, int r) {
        if (l >= r)
            return;

        int mid = (l + r) / 2;
        newSort(arr, l, mid);
        newSort(arr, mid + 1, r);
        merge(arr, l, mid, r);

    }

    // 将 arr[l...mid] 和 arr[mid+1...r] 两部分进行归并
    public static void merge(Comparable[] arr, int l, int mid, int r) {
        Comparable[] aux = Arrays.copyOfRange(arr, l, r + 1);

        int i = l;
        int j = mid + 1;
        for (int k = l; k <= r; k++) {
            if (i > mid) { //左半部分元素已经处理完毕
                arr[k] = aux[j - l];
                j++;
            } else if (j > r) { //右半部分元素已经处理完毕
                arr[k] = aux[i - l];
                i++;
            } else if (aux[i - l].compareTo(aux[j - l]) < 0) {
                arr[k] = aux[i - l];
                i++;
            } else {
                arr[k] = aux[j - l];
                j++;
            }
        }

    }

    public static void main(String[] args) {
        Integer[] integers = SortTestHelper.generateRandomArray(100, 10, 60);
        System.out.println(Arrays.toString(integers));
        newSort(integers);
        System.out.println(Arrays.toString(integers));
    }
}
