"""
队列的链表实现
"""


class Node:
    """单链表节点"""
    def __init__(self, data, later=None):
        self.data = data
        self.later = later  # 指向下一个节点


class SinglyLinkedQueue:
    def __init__(self, source_collection=None):
        self.size = 0
        self.head = self.last = None
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __iter__(self):
        probe = self.head
        while probe is not None:
            yield probe.data
            probe = probe.later

    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        other_iter = iter(other)
        for item in self:
            if item != next(other_iter):
                return False
        return True

    def __add__(self, other):
        for item in other:
            self.add(item)
        return self

    def add(self, item):
        """将元素添加队列末尾"""
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.last.later = new_node
        self.last = new_node
        self.size += 1

    def pop(self):
        """删除队列开始项并返回该元素"""
        if self.is_empty():
            raise KeyError("当前队列为空！")
        remove_item = self.head.data
        self.head = self.head.later
        if self.head is None:
            self.last = None
        self.size -= 1
        return remove_item

    def peak(self):
        """返回队列开始项"""
        if self.is_empty():
            raise KeyError("当前队列为空！")
        return self.head.data

    def clear(self):
        """将队列清空"""
        self.head = self.last = None
        self.size = 0

    def is_empty(self):
        """队列为空返回 False，否则返回 True"""
        return self.size == 0
