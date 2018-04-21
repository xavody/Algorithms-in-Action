"""
优先队列的链表实现
"""
from .singly_linked_queue import SinglyLinkedQueue


class Node:
    """单链表节点"""
    def __init__(self, data, later=None):
        self.data = data
        self.later = later  # 指向下一个节点


class LinkedPriorityQueue:
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
        """将元素添加优先队列中"""
        # 如果优先队列为空或者新的项优先级低于队列中所有项的优先级，将新项添加到队列末尾中
        if self.is_empty() or item >= self.last.data:
            new_node = Node(item)
            if self.is_empty():
                self.head = new_node
            else:
                self.last.later = new_node
            self.last = new_node
        else:  # 否则遍历所有项找到合适位置
            probe = self.head
            trailer = None
            while item >= probe.data:
                trailer = probe
                probe = probe.later
            new_node = Node(item, probe)
            if trailer is None:
                self.head = new_node
            else:
                trailer.later = new_node
        self.size += 1

    def pop(self):
        """删除优先队列优先级最高项并返回该项"""
        if self.is_empty():
            raise KeyError("当前队列为空！")
        remove_item = self.head.data
        self.head = self.head.later
        if self.head is None:
            self.last = None
        self.size -= 1
        return remove_item

    def peak(self):
        """返回优先队列优先级最高项"""
        if self.is_empty():
            raise KeyError("当前队列为空！")
        return self.head.data

    def clear(self):
        """将优先队列清空"""
        self.head = self.last = None
        self.size = 0

    def is_empty(self):
        """优先队列为空返回 False，否则返回 True"""
        return self.size == 0


class LinkedPriorityQueue1(SinglyLinkedQueue):
    def __init__(self, source_collection=None):
        super().__init__(source_collection)

    def add(self, item):
        # 如果优先队列为空或者新的项优先级低于队列中所有项的优先级，将新项添加到队列末尾中
        if self.is_empty() or item >= self.last.data:
            super().add(item)
        else:  # 否则遍历所有项找到合适位置
            probe = self.head
            trailer = None
            while item >= probe.data:
                trailer = probe
                probe = probe.later
            new_node = Node(item, probe)
            if trailer is None:
                self.head = new_node
            else:
                trailer.later = new_node
            self.size += 1
