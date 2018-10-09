"""
栈的链表实现
"""


class Node:
    """单链表节点"""
    def __init__(self, data, later=None):
        self.data = data
        self.later = later  # 指向下一个节点


class SinglyLinkedStack:
    def __init__(self, source_collection=None):
        self.size = 0
        self.head = None
        if source_collection:
            for item in source_collection:
                self.push(item)

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
            self.push(item)
        return self

    def push(self, item):
        """将元素压入栈顶"""
        self.head = Node(item, self.head)
        self.size += 1

    def peak(self):
        """返回栈顶"""
        if self.is_empty():
            raise KeyError("当前栈为空！")
        return self.head.data

    def pop(self):
        """删除栈顶并返回该元素"""
        if self.is_empty():
            raise KeyError("当前栈为空！")
        remove_item = self.head.data
        self.head = self.head.later
        self.size -= 1
        return remove_item

    def is_empty(self):
        return self.size == 0

    def clear(self):
        """将栈清空"""
        self.head = None
        self.size = 0
