package me.imtt.heap;

/**
 * 堆排序，版本一
 */
public class HeapSort1 {
    /**
     * 使用最大堆，将所有的元素依次添加到堆中,
     * 再将所有元素从堆中依次取出来, 即完成了排序（由小到大）
     * 堆排序的整体时间复杂度为O(nlogn)
     */
    public static void sort(Comparable[] arr) {
        int n = arr.length;
        MaxHeap<Comparable> maxHeap = new MaxHeap<Comparable>(n);

        for (int i = 0; i < n; i++) {
            maxHeap.insert(arr[i]);
        }
        for (int i = n - 1; i >= 0; i--) {
            arr[i] = maxHeap.extractMax();
        }
    }
}
