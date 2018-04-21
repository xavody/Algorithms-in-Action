"""
基于双链表的列表
"""


class TwoWayNode:
    """双链表节点"""
    def __init__(self, data=None, previous=None, later=None):
        self.data = data
        self.previous = previous
        self.later = later


class LinkedList:
    """基于双链表的列表"""
    def __init__(self, source_collection=None):
        self.head = TwoWayNode()  # 哨兵节点
        self.head.previous = self.head.later = self.head
        self.size = 0
        self.mod_count = 0
        if source_collection:
            for item in source_collection:
                self.add(item)

    def __iter__(self):
        probe = self.head.later
        while probe != self.head:
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

    def is_empty(self):
        """列表为空返回 False，否则返回 True"""
        return self.size == 0

    def clear(self):
        """将列表清空"""
        self.head = TwoWayNode()
        self.size = 0
        self.head.previous = self.head.later = self.head

    def get_mod_count(self):
        return self.mod_count

    def inc_mod_count(self):
        self.mod_count += 1

    def index(self, item):
        """基于内容的操作，返回项 item 在列表中的索引"""
        po = 0
        for data in self:
            if data == item:
                return po
            else:
                po += 1
        if po == len(self):
            raise ValueError(str(item) + "不在列表中！")

    def add(self, item):
        """基于内容的操作，在列表尾部添加项"""
        self.insert(len(self), item)

    def remove(self, item):
        """基于内容的操作，从列表中删除项 item"""
        po = self.index(item)
        self.pop(po)

    def _get_node(self, i):
        """基于索引的操作的辅助方法，返回第 i 项的指针"""
        if i == len(self):
            return self.head
        elif i == len(self) - 1:
            return self.head.previous
        else:
            probe = self.head.later
            while i > 0:
                probe = probe.later
                i -= 1
            return probe

    def __getitem__(self, i):
        """基于索引的操作，返回索引 i 处的项"""
        if i < 0 or i >= len(self):
            raise IndexError("列表索引超出范围！")
        return self._get_node(i).data

    def __setitem__(self, i, item):
        """基于索引的操作，用 item 替换索引 i 处的项"""
        if i < 0 or i >= len(self):
            raise IndexError("列表索引超出范围！")
        self._get_node(i).data = item

    def insert(self, i, item):
        """基于索引的操作，在索引 i 处添加项 item"""
        if i < 0 or i > len(self):
            raise IndexError("列表索引超出范围！")
        node = self._get_node(i)
        new_node = TwoWayNode(item, previous=node.previous, later=node)
        node.previous.later = new_node
        node.previous = new_node
        self.size += 1
        self.inc_mod_count()

    def pop(self, i=None):
        """基于索引的操作，删除并返回索引 i 的项，如果没有参数 i，删除并返回最后一项"""
        if i is None:
            i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("列表索引超出范围！")
        node = self._get_node(i)
        remove_item = node.data
        node.previous.later = node.later
        node.later.previous = node.previous
        self.size -= 1
        self.inc_mod_count()
        return remove_item


linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
print(linked_list)
print(linked_list.index(2))
# linked_list.remove(2)
linked_list[1] = 7
print(linked_list)
linked_list.insert(3, 4)
print(linked_list)
print(linked_list.pop(0))
print(linked_list)

linked_list1 = LinkedList([5, 6, 8])
print(linked_list1)
print(linked_list == linked_list1)
linked_list += linked_list1
print(linked_list)
