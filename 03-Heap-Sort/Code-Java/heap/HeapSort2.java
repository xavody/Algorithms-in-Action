package heap;

import java.util.Arrays;

/**
 * 堆排序，版本二
 */
public class HeapSort2 {
    // 使用最大堆，将 arr 数组通过 MaxHeap 构造函数创建最大堆，
    // 再将所有元素从堆中依次取出来, 即完成了排序（由小到大）
    // 将所有元素依次从堆中取出来的时间复杂度为O(nlogn)
    // 堆排序的整体时间复杂度为O(nlogn)
    public static void newSort(Comparable[] arr) {
        int n = arr.length;
        MaxHeap<Comparable> maxHeap = new MaxHeap<Comparable>(arr);
        for (int i = n - 1; i >= 0; i--)
            arr[i] = maxHeap.extractMax();
    }
}
