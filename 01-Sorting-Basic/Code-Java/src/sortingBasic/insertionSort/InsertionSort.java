package sortingBasic.insertionSort;

/**
 * 插入排序（升序）
 */
public class InsertionSort {
    public static void newSort(Comparable[] arr) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = i; j > 0 && arr[j].compareTo(arr[j - 1]) < 0; j--)
                swap(arr, j, j - 1);
        }
    }

    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
