package sortingBasic.bubbleSort;


/**
 * 冒泡排序（升序）
 */
public class BubbleSort {
    public static void newSort(Comparable[] arr) {
        for (int i = arr.length - 1; i > 0; i--) {
            boolean flag = true;
            for (int j = 0; j < i; j++) {
                if (arr[j + 1].compareTo(arr[j]) < 0) {
                    flag = false;
                    swap(arr, j, j + 1);
                }
            }
            if (flag)
                break;
        }
    }

    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

}
