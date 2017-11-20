package heap;

/**
 * 最大堆
 * 索引从1开始
 */
public class MaxHeap<Item extends Comparable> {
    protected Item[] data;
    protected int count;
    protected int capacity;

    // 构造函数, 构造一个空堆, 可容纳capacity个元素
    public MaxHeap(int capacity) {
        data = (Item[]) new Comparable[capacity + 1];
        count = 0;
        this.capacity = capacity;
    }

    // 构造函数, 通过一个给定数组创建一个最大堆
    // 该构造堆的过程, 时间复杂度为O(n)
    public MaxHeap(Item[] arr) {
        int n = arr.length;
        data = (Item[])new Comparable[n + 1];
        capacity = n;

        System.arraycopy(arr, 0, data, 1, n);
        count = n;

        for (int i = count / 2; i > 0; i--) {
            shiftDown(i);
        }
    }

    // 测试 MaxHeap
    public static void main(String[] args) {
        MaxHeap<Integer> maxHeap = new MaxHeap<Integer>(100);
        int N = 100; // 堆中元素个数
        int M = 100; // 堆中元素取值范围[0, M)
        for (int i = 0; i < N; i++)
            maxHeap.insert(new Integer((int) (Math.random() * M)));

        Integer[] arr = new Integer[N];

        // 将maxheap中的数据逐渐使用extractMax取出来
        // 取出来的顺序应该是按照从大到小的顺序取出来的
        for (int i = 0; i < N; i++) {
            arr[i] = maxHeap.extractMax();
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // 确保arr数组是从大到小排列的
        for (int i = 1; i < N; i++)
            assert arr[i - 1] >= arr[i];
    }

    // 返回堆中的元素个数
    public int size() {
        return count;
    }

    //
    public boolean imEmpty() {
        return count == 0;
    }

    // 获取最大堆中的堆顶元素
    public Item getMax() {
        assert count > 0;
        return data[1];
    }

    // 在最大堆中插入一个新的元素
    public void insert(Item item) {
        assert count + 1 <= capacity;
        data[++count] = item;
        shiftUp(count);
    }

    // 从最大堆中取出堆顶元素, 即堆中所存储的最大数据
    public Item extractMax() {
        assert count > 0;
        Item max = data[1];
        data[1] = data[count];
        data[count--] = null;
        shiftDown(1);
        return max;
    }

    // 由下至上的堆有序化，保证最大堆的性质
    private void shiftUp(int k) {
        while (k > 1 && data[k / 2].compareTo(data[k]) < 0) {
            // 如果当前元素大于父节点，交换
            swap(k, k / 2);
            k /= 2;
        }
    }

    // 由上至下的堆有序化，保证最大堆的性质
    private void shiftDown(int k) {
        while (2 * k <= count) {
            int j = k * 2;
            if (j + 1 <= count && data[j + 1].compareTo(data[j]) > 0)
                j++;
            if (data[k].compareTo(data[j]) >= 0)
                break;
            swap(k, j);
            k = j;
        }
    }

    //交换堆中两个元素
    private void swap(int i, int j) {
        Item temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }
}
