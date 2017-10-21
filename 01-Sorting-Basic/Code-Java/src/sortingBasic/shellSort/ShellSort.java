package sortingBasic.shellSort;

/**
 * 希尔排序（升序）
 */
public class ShellSort {
    public static void newSort(Comparable[] arr) {
        int length = arr.length;
        int gap = 1;
        while (gap < length / 3)
            gap = 3 * gap + 1;
        for (; gap > 0; gap /= 3) {
            for (int i = gap; i < length; i++) {
                Comparable temp = arr[i];
                int j = i;
                for (;j >= gap && temp.compareTo(arr[j - gap]) < 0; j -= gap)
                    arr[j] = arr[j - gap];
                arr[j] = temp;
            }
        }
    }
}
