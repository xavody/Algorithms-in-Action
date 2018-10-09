package me.imtt.graph.weighted;

/**
 * 在堆的有关操作中，需要比较堆中元素的大小，所以Item需要extends Comparable
 */
public class MinHeap<Item extends Comparable> {
    private Item[] data;
    private int count;
    private int capacity;

    /**
     * 构造一个空堆, 可容纳 capacity 个元素
     */
    public MinHeap(int capacity) {
        data = (Item[]) new Comparable[capacity + 1];
        count = 0;
        this.capacity = capacity;
    }

    /**
     * 通过一个给定数组创建一个最小堆, 时间复杂度为O(n)
     */
    public MinHeap(Item arr[]) {
        int n = arr.length;
        data = (Item[]) new Comparable[n + 1];
        capacity = n;

        System.arraycopy(arr, 0, data, 1, n);
        count = n;

        for (int i = count / 2; i >= 1; i--) {
            shiftDown(i);
        }
    }

    /**
     * 返回堆中的元素个数
     */
    public int size() {
        return count;
    }

    /**
     * 返回堆中是否为空
     */
    public boolean isEmpty() {
        return count == 0;
    }

    /**
     * 向最小堆中插入一个新的元素 item
     */
    public void insert(Item item) {
        assert count + 1 <= capacity;
        data[++count] = item;
        shiftUp(count);
    }

    /**
     * 获取最小堆中的堆顶元素
     */
    public Item getMin() {
        assert (count > 0);
        return data[1];
    }

    /**
     * 从最小堆中取出堆顶元素, 即堆中所存储的最小数据
     */
    public Item extractMin() {
        assert count > 0;
        Item min = data[1];
        data[1] = data[count];
        data[count--] = null;
        shiftDown(1);
        return min;
    }

    /**
     * 下至上的堆有序化，保证最小堆的性质
     */
    public void shiftUp(int k) {
        while (k > 1 && data[k / 2].compareTo(data[k]) > 0) {
            swap(k, k / 2);
            k /= 2;
        }
    }

    /**
     * 由上至下的堆有序化，保证最小堆的性质
     */
    public void shiftDown(int k) {
        while (k * 2 <= count) {
            int j = k * 2;
            if (j + 1 <= count && data[j + 1].compareTo(data[j]) < 0) {
                j++;
            }
            if (data[k].compareTo(data[j]) <= 0) {
                break;
            }
            swap(k, j);
            k = j;
        }
    }

    /**
     * 交换堆中两个元素
     */
    private void swap(int i, int j) {
        Item temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }
}
