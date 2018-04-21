"""
双链表
"""


class TwoWayNode:
    """双链表节点"""
    def __init__(self, data, previous=None, later=None):
        self.data = data
        self.previous = previous
        self.later = later


class DoublyLinkedList:
    """双链表"""
    def __init__(self, source_collection=None):
        self.head = self.last = None
        if source_collection:
            for item in source_collection:
                self.insert_end(item)

    def __iter__(self):
        """迭代双链表"""
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
            return False  # target 不在双链表中
        else:
            return True  # target 在双链表中

    def sequential_search_with_index(self, index):
        """基于索引的顺序搜索"""
        if index < 0 or index >= self.size():
            raise IndexError('索引超出范围！')
        probe = self.head
        while index > 0:
            probe = probe.later
            index -= 1
        return probe.data

    def size(self):
        """返回双链表的大小"""
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
        if index < 0 or index >= self.size():
            raise IndexError('索引超出范围！')
        probe = self.head
        while index > 0:
            probe = probe.later
            index -= 1
        probe.data = new_item

    def insert_pre(self, data):
        """在开始处插入"""
        new_node = TwoWayNode(data, later=self.head)
        if self.head:  # 链表不为空
            self.head.previous = new_node
        else:  # 链表为空
            self.last = new_node
        self.head = new_node

    def insert_end(self, data):
        """在末尾插入"""
        new_node = TwoWayNode(data)
        if self.head is None:  # head 指针为 None
            self.head = new_node
        else:  # head 指针不为 None
            self.last.later = new_node
            new_node.previous = self.last
        self.last = new_node

    def insert(self, index, data):
        """在任何位置插入"""
        length = self.size()
        if index < 0 or index > length:
            raise IndexError('索引超出范围！')

        if index == 0:  # 在开始处插入
            self.insert_pre(data)
        elif index == length:  # 在末尾插入
            new_node = TwoWayNode(data)
            self.last.later = new_node
            new_node.previous = self.last
            self.last = new_node
        else:  # index > 0
            probe = self.head
            while index > 1 and probe.later is not None:  # 如果 index 超出了链表结构的末尾就在末尾插入
                probe = probe.later
                index -= 1
            new_node = TwoWayNode(data, previous=probe, later=probe.later)
            probe.later.previous = new_node
            probe.later = new_node

    def delete_pre(self):
        """在开始处删除"""
        if self.head is None:
            raise KeyError('链表为空')

        remove_item = self.head.data
        if self.head.later is None:  # 只有一个节点
            self.head = self.last = None
        else:
            self.head = self.head.later
            self.head.previous = None
        return remove_item

    def delete_end(self):
        """在末尾处删除"""
        if self.head is None:
            raise KeyError('链表为空')

        if self.head.later is None:  # 只有一个节点
            remove_item = self.head.data
            self.head = self.last = None
        else:  # 含有多个节点
            remove_item = self.last.data
            self.last = self.last.previous
            self.last.later = None
        return remove_item

    def delete(self, index):
        """在任意位置删除"""
        length = self.size()
        if self.head is None:
            raise KeyError('链表为空')

        if index < 0 or index >= length:
            raise IndexError('索引超出范围！')
        elif index == 0:  # 在开始处删除
            remove_item = self.delete_pre()
        elif index == length - 1:  # 在末尾处删除
            remove_item = self.delete_end()
        else:  # index > 0
            probe = self.head
            while index > 1 and probe.later.later is not None:
                probe = probe.later
                index -= 1
            remove_item = probe.later.data
            probe.later = probe.later.later
            probe.later.later.previous = probe
        return remove_item

    def is_empty(self):
        """判断双链表是否为空"""
        return True if self.head else False

    # def get_last_and_second_last(self):
    #     print('last: ', self.last.data, 'second last: ', self.last.previous.data)


d = DoublyLinkedList([1, 2, 3, 4])
print(d)
print(d.size())
# print(d.sequential_search_with_index(3))
# print(d.replace_with_index(3, 8))
print(d)
print("##############")
d1 = DoublyLinkedList()
d1.insert_pre(1)
d1.insert_pre(2)
d1.insert_pre(3)
d1.insert_end(5)
print(d1)
# d1.insert(3, 7)
# d1.delete_pre()
print(d1)
for dd in d1:
    print(dd)
