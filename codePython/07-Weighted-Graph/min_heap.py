"""
最小堆，索引从1开始
"""


class MinHeap(object):
    def __init__(self, capacity=0, lst=None):
        """
        如果传入参数为长度 capacity，构造一个可容纳 capacity 个元素的空堆
        如果传入参数为序列 lst，由 lst 构建一个最小堆
        """
        self.data = [0, ]
        if capacity and (not lst):
            self.count = 0
            self.capacity = capacity
        elif (not capacity) and lst:
            n = len(lst)
            self.capacity = n
            self.data.extend(lst)
            self.count = n
            for i in range(n // 2, 0, -1):
                self.shift_down(i)

    def get_size(self):
        """
        返回堆中元素个数
        """
        return self.count

    def is_empty(self):
        """
        返回一个布尔值, 表示堆中是否为空
        """
        return self.count == 0

    def get_min(self):
        """
        获取最小堆中的堆顶元素
        """
        assert self.count > 0
        return self.data[1]

    def insert(self, item):
        """
        在最小堆中插入一个新的元素
        """
        assert self.count + 1 <= self.capacity
        self.count += 1
        self.data.append(item)
        self.shift_up(self.count)

    def extract_min(self):
        """
        从最小堆中取出堆顶元素, 即堆中所存储的最小数据
        """
        assert self.count > 0
        re_min = self.data[1]
        self.data[1] = self.data[self.count]
        self.data.pop()
        self.count -= 1
        self.shift_down(1)
        return re_min

    def shift_up(self, k):
        """
        由下至上的堆有序化，保证最小堆的性质
        """
        while k > 1 and (self.data[k // 2] > self.data[k]):
            self.data[k], self.data[k // 2] = self.data[k // 2], self.data[k]
            k //= 2

    def shift_down(self, k):
        """
        由上至下的堆有序化，保证最小堆的性质
        """
        while k * 2 <= self.count:
            j = k * 2
            if j + 1 <= self.count and self.data[j + 1] < self.data[j]:
                j += 1
            if self.data[j] > self.data[k]:
                break
            self.data[k], self.data[j] = self.data[j], self.data[k]
            k = j
