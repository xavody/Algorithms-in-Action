package me.imtt.sorting.advance.merge;

/**
 * 自顶向下进行归并排序
 */
public class MergeSort {
    /**
     * 辅助数组
     */
    private static Comparable[] aux; 

    public static void sort(Comparable[] arr) {
        int n = arr.length;

        //一次性分配空间
        aux = new Comparable[n]; 
        sort(arr, 0, n - 1);
    }

    /**
     * 使用递归进行归并排序,对 arr[l...r] 的范围进行排序
     */
    private static void sort(Comparable[] arr, int l, int r) {
        if (l >= r) {
            return;
        }

        int mid = (l + r) / 2;

        //将左半部分排序
        sort(arr, l, mid);
        
        //将右半部分排序
        sort(arr, mid + 1, r); 

        //对于arr[mid] <= arr[mid+1]的情况,不进行merge
        if (arr[mid].compareTo(arr[mid + 1]) > 0) {
            merge(arr, l, mid, r);
        }
    }

    /**
     * 将 arr[l...mid] 和 arr[mid+1...r] 两部分进行归并
     */
    private static void merge(Comparable[] arr, int l, int mid, int r) {
        int i = l;
        int j = mid + 1;

        System.arraycopy(arr, l, aux, l, r - l + 1);

        for (int k = l; k <= r; k++) {
            if (i > mid) {
                //左半部分元素已经处理完毕
                arr[k] = aux[j++];
             } 
            else if (j > r) {
                //右半部分元素已经处理完毕
                arr[k] = aux[i++]; 
            } else if (aux[i].compareTo(aux[j]) < 0) {
                arr[k] = aux[i++];
            } else {
                arr[k] = aux[j++];
            }
        }
    }
}
