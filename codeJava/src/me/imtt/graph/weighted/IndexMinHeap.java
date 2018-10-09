package me.imtt.graph.weighted;

/**
 * 最小索引堆
 */
public class IndexMinHeap<Item extends Comparable> {
    /**
     * 最小索引堆中的数据
     */
    private Item[] data;

    /**
     * 最小索引堆中的索引, indexes[x]=i表示索引i在x的位置
     */
    private int[] indexes;

    /**
     * 最小索引堆中的反向索引, reverse[i]=x表示索引i在x的位置
     */
    private int[] reverse;

    private int count;

    private int capacity;

    /**
     * 构造一个空堆, 可容纳 capacity 个元素
     */
    public IndexMinHeap(int capacity) {
        data = (Item[]) new Comparable[capacity + 1];
        indexes = new int[capacity + 1];
        reverse = new int[capacity + 1];
        for (int i = 0; i <= capacity; i++) {
            reverse[i] = 0;
        }
        count = 0;
        this.capacity = capacity;
    }

    /**
     * 返回索引堆中的元素个数
     */
    public int size() {
        return count;
    }

    /**
     * 返回索引堆中是否为空
     */
    public boolean isEmpty() {
        return count == 0;
    }

    /**
     * 向最小索引堆中插入一个新的元素, 新元素的索引为i, 元素为item
     * 传入的i对用户而言,是从0索引的
     */
    public void insert(int i, Item item) {
        assert count + 1 <= capacity;
        assert i + 1 >= 1 && i + 1 <= capacity;
        assert !contain(i);

        i++;
        data[i] = item;
        indexes[++count] = i;
        reverse[i] = count;
        shiftUp(count);
    }

    /**
     * 获取最小索引堆中的堆顶元素
     */
    public Item getMin() {
        assert (count > 0);
        return data[indexes[1]];
    }

    /**
     * 从最小索引堆中取出堆顶元素, 即索引堆中所存储的最小数据
     */
    public Item extractMin() {
        assert count > 0;

        Item min = data[indexes[1]];
        swapIndexes(1, count);
        reverse[indexes[count--]] = 0;
        shiftDown(1);
        return min;
    }

    /**
     * 从最小索引堆中取出堆顶元素的索引
     */
    public int extractMinIndex() {
        assert count > 0;
        int min = indexes[1] - 1;
        swapIndexes(1, count);
        reverse[indexes[count]] = 0;
        count--;
        return min;
    }

    /**
     * 获取最小索引堆中的堆顶元素的索引
     */
    public int getMinIndexes() {
        assert count > 0;
        return reverse[1] - 1;
    }

    /**
     * 看索引i所在的位置是否存在元素
     */
    public boolean contain(int i) {
        assert i + 1 >= 1 && i + 1 <= capacity;
        return reverse[i + 1] != 0;
    }

    /**
     * 获取最小索引堆中索引为i的元素
     */
    public Item getItem(int i) {
        assert contain(i);
        return data[i + 1];
    }

    /**
     * 将最小索引堆中索引为i的元素修改为newItem
     */
    public void change(int i, Item newItem) {
        assert contain(i);
        i++;
        data[i] = newItem;

        shiftUp(reverse[i]);
        shiftDown(reverse[i]);
    }

    /**
     * 由上至下的索引堆有序化，保证最小索引堆的性质
     * 索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
     */
    public void shiftUp(int k) {
        while (k > 1 && data[indexes[k / 2]].compareTo(data[indexes[k]]) > 0) {
            swapIndexes(k, k / 2);
            k /= 2;
        }
    }

    /**
     * 由上至下的索引堆有序化，保证最小索引堆的性质
     * 索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
     */
    public void shiftDown(int k) {
        while (k * 2 < count) {
            int j = k * 2;
            if (j + 1 <= count && data[indexes[j + 1]].compareTo(data[indexes[j]]) < 0) {
                j++;
            }
            if (data[indexes[k]].compareTo(data[indexes[j]]) <= 0) {
                break;
            }
            swapIndexes(k, j);
            k = j;
        }
    }

    /**
     * 交换索引堆中的索引i和j
     */
    private void swapIndexes(int i, int j) {
        int t = indexes[i];
        indexes[i] = indexes[j];
        indexes[j] = t;

        reverse[indexes[i]] = i;
        reverse[indexes[j]] = j;
    }
}
