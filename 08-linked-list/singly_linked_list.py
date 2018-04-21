"""
单链表
"""


class Node:
    """单链表节点"""
    def __init__(self, data, later=None):
        self.data = data
        self.later = later  # 指向下一个节点


class SinglyLinkedList:
    """单链表"""
    def __init__(self, source_collection=None):
        self.head = None
        if source_collection:
            for item in source_collection:
                self.insert_end(item)

    def __iter__(self):
        """迭代单链表"""
        probe = self.head
        while probe is not None:
            yield probe.data
            probe = probe.later

    def __str__(self):
        return '[' + ', '.join(map(str, self)) + ']'

    def sequential_search_with_data(self, target):
        """基于数据值的顺序搜索"""
        probe = self.head
        while probe is not None and target != probe.data:
            probe = probe.later
        if probe is None:
            return False  # target 不在单链表中
        else:
            return True  # target 在单链表中

    def sequential_search_with_index(self, index):
        """基于索引的顺序搜索"""
        if index < 0:
            raise IndexError('索引超出范围！')
        probe = self.head
        try:
            while index > 0:
                probe = probe.later
                index -= 1
            return probe.data
        except AttributeError:
            raise IndexError('索引超出范围！')

    def size(self):
        """返回单链表的大小"""
        counter = 0
        probe = self.head
        while probe is not None:
            counter += 1
            probe = probe.later
        return counter

    def replace_with_data(self, target, new_item):
        """基于数据值的替换"""
        probe = self.head
        while probe is not None and target != probe.data:
            probe = probe.later
        if probe is not None:
            probe.data = new_item
            return True  # 替换成功
        else:
            return False  # 目标项不存在

    def replace_with_index(self, index, new_item):
        """基于索引的替换"""
        if index < 0:
            raise IndexError('索引超出范围！')
        probe = self.head
        try:
            while index > 0:
                probe = probe.later
                index -= 1
            probe.data = new_item
        except AttributeError:
            raise IndexError('索引超出范围！')

    def insert_pre(self, data):
        """在开始处插入"""
        self.head = Node(data, self.head)

    def insert_end(self, data):
        """在末尾插入"""
        new_node = Node(data)
        if self.head is None:  # head 指针为 None
            self.head = new_node
        else:  # head 指针不为 None
            probe = self.head
            while probe.later is not None:
                probe = probe.later
            probe.later = new_node

    def insert(self, index, data):
        """在任何位置插入"""
        if index < 0:
            raise IndexError('索引超出范围！')
        elif index == 0 or self.head is None:  # 在开始处插入
            self.head = Node(data, self.head)
        else:  # index > 0
            probe = self.head
            while index > 1 and probe.later is not None:  # 如果 index 超出了链表结构的末尾就在末尾插入
                probe = probe.later
                index -= 1
            if index > 1:
                raise IndexError('索引超出范围！')
            probe.later = Node(data, probe.later)

    def delete_pre(self):
        """在开始处删除"""
        if self.head is None:
            raise KeyError('链表为空')
        remove_item = self.head.data
        self.head = self.head.later
        return remove_item

    def delete_end(self):
        """在末尾处删除"""
        if self.head is None:
            raise KeyError('链表为空')
        elif self.head.later is None:  # 只有一个节点
            remove_item = self.head.data
            self.head = None
        else:  # 含有多个节点
            probe = self.head
            while probe.later.later is not None:
                probe = probe.later
            remove_item = probe.later.data
            probe.later = None
        return remove_item

    def delete(self, index):
        """在任意位置删除"""
        if self.head is None:
            raise KeyError('链表为空')
        elif index < 0:
            raise IndexError('索引超出范围！')
        elif index == 0 or self.head.later is None:
            remove_item = self.head.data
            self.head = self.head.later
        else:  # index > 0
            probe = self.head
            while index > 1 and probe.later.later is not None:
                probe = probe.later
                index -= 1
            if index > 1:
                raise IndexError('索引超出范围！')
            remove_item = probe.later.data
            probe.later = probe.later.later
        return remove_item

    def is_empty(self):
        """判断单链表是否为空"""
        return True if self.head else False


if __name__ == '__main__':
    head = SinglyLinkedList([1, 2, 3])
    # head.insert_pre(1)
    # head.insert_pre(2)
    # head.insert_pre(3)
    # head.insert_end(4)
    # head.insert(1, 'a')
    # head.insert(7, '7')
    for i in head:
        print(i)
    #
    print(head)

    # head.del_pre()
    # head.del_end()
    #
    # head.delete(4)
    # print(head.sequential_search_with_index(5))
