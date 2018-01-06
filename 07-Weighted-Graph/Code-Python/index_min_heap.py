"""
最小索引堆，索引从1开始
"""


class IndexMinHeap(object):
    def __init__(self, capacity):
        """可容纳 capacity 个元素的最小索引堆"""
        self.data = [None for _ in range(capacity + 1)]  # 最小索引堆中的数据
        self.indexes = [None for _ in range(capacity + 1)]  # 最小索引堆中的索引, indexes[x]=i表示索引i在x的位置
        self.reverse = [0 for _ in range(capacity + 1)]  # 最小索引堆中的反向索引, reverse[i]=x表示索引i在x的位置
        self.count = 0
        self.capacity = capacity

    def get_size(self):
        """返回堆中元素个数"""
        return self.count

    def is_empty(self):
        """返回一个布尔值, 表示堆中是否为空"""
        return self.count == 0

    def get_min(self):
        """获取最大堆中的堆顶元素"""
        assert self.count > 0
        return self.data[self.indexes[1]]

    def insert(self, i, item):
        """
        向最小索引堆中插入一个新的元素, 新元素的索引为i, 元素为item
        传入的i对用户而言,是从0索引的
        """
        assert self.count + 1 <= self.capacity
        assert i + 1 in range(1, self.capacity + 1)
        assert not self.contain(i)

        i += 1
        self.data[i] = item
        self.count += 1
        self.indexes[self.count] = i
        self.reverse[i] = self.count
        self.shift_up(self.count)

    def extract_min(self):
        """从最小索引堆中取出堆顶元素, 即索引堆中所存储的最小数据"""
        assert self.count > 0
        re_min = self.data[self.indexes[1]]
        self.swap_indexes(1, self.count)
        self.reverse[self.indexes[self.count]] = 0
        self.count -= 1
        self.shift_down(1)
        return re_min

    def extract_min_index(self):
        """从最小索引堆中取出堆顶元素的索引"""
        assert self.count > 0
        re_min = self.indexes[1] - 1
        self.swap_indexes(1, self.count)
        self.reverse[self.indexes[self.count]] = 0
        self.count -= 1
        return re_min

    def get_min_indexes(self):
        """获取最小索引堆中的堆顶元素的索引"""
        assert self.count > 0
        return self.reverse[1] - 1

    def contain(self, i):
        """看索引i所在的位置是否存在元素"""
        assert i + 1 in range(1, self.capacity + 1)
        return self.reverse[i + 1] != 0

    def get_item(self, i):
        """获取最小索引堆中索引为i的元素"""
        assert self.contain(i)
        return self.data[i + 1]

    def change(self, i, item):
        """将最小索引堆中索引为i的元素修改为item"""
        assert self.contain(i)
        i += 1
        self.data[i] = item
        self.shift_up(self.reverse[i])
        self.shift_down(self.reverse[i])

    def shift_up(self, k):
        """
        由上至下的索引堆有序化，保证最小索引堆的性质
        索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
        """
        while k > 1 and self.data[self.indexes[k // 2]] > self.data[self.indexes[k]]:
            self.swap_indexes(k, k // 2)
            k //= 2

    def shift_down(self, k):
        """
        由上至下的索引堆有序化，保证最小索引堆的性质
        索引堆中, 数据之间的比较根据data的大小进行比较, 但实际操作的是索引
        """
        while k * 2 <= self.count:
            j = k * 2
            if j + 1 <= self.count and self.data[self.indexes[j + 1]] < self.data[self.indexes[j]]:
                j += 1
            if self.data[self.indexes[k]] <= self.data[self.indexes[j]]:
                break
            self.swap_indexes(k, j)
            k = j

    def swap_indexes(self, i, j):
        """交换索引堆中的索引i和j"""
        self.indexes[i], self.indexes[j] = self.indexes[j], self.indexes[i]
        self.reverse[self.indexes[i]], self.reverse[self.indexes[j]] = i, j

