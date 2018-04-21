"""
二叉搜索树
"""
import queue


class BST:
    class Node:
        """树节点"""

        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

    def __init__(self, source_collection=None):
        self.size = 0  # 二叉搜索树中节点的个数
        self.root = None  # 根节点
        if source_collection:
            for item in source_collection:
                self.insert(item)

    def __iter__(self):
        if self.root is not None:
            lst = list()
            lst.append(self.root)
            while lst:
                node = lst.pop()
                yield node.data
                if node.right is not None:
                    lst.append(node.right)
                if node.left is not None:
                    lst.append(node.left)

    def __str__(self):
        def recurse(node, level):
            s = ''
            if node is not None:
                s += recurse(node.right, level + 1)
                s += '| ' * level
                s += str(node.data) + '\n'
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

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
            self.insert(item)
        return self

    def is_empty(self):
        """列表为空返回 False，否则返回 True"""
        return self.size == 0

    def clear(self):
        """将列表清空"""
        self.root = None
        self.size = 0

    def search(self, item):
        """在二叉搜索树中搜索 item。如果存在, 返回第一个匹配的项，否则返回 None"""

        def recurse(node):
            if node is None:
                return None
            elif item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)

        return recurse(self.root)

    def pre_order(self):
        """深度优先遍历-前序遍历
        把遍历的每一项添加到列表中，并返回该列表的迭代器
        """
        lst = list()

        def recurse(node):
            if node is not None:
                lst.append(node.data)
                recurse(node.left)
                recurse(node.right)

        recurse(self.root)
        return iter(lst)

    def in_order(self):
        """深度优先遍历-中序遍历
        把遍历的每一项添加到列表中，并返回该列表的迭代器
        """
        lst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                lst.append(node.data)
                recurse(node.right)

        recurse(self.root)
        return iter(lst)

    def post_order(self):
        """深度优先遍历-后序遍历
        把遍历的每一项添加到列表中，并返回该列表的迭代器
        """
        lst = list()

        def recurse(node):
            if node is not None:
                recurse(node.left)
                recurse(node.right)
                lst.append(node.data)

        recurse(self.root)
        return iter(lst)

    def level_order(self):
        """广度优先遍历
        把遍历的每一项添加到列表中，并返回该列表的迭代器
        """
        lst = list()
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get()
            lst.append(node.data)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return lst

    def insert(self, item):
        """将一个项插入到二叉搜索树的适当位置
        如果 item 与某一项的值相等，插入到这一项的右子树中
        """

        def recurse(node):
            if item < node.data:
                if node.left is None:
                    node.left = BST.Node(item)
                else:
                    recurse(node.left)
            elif node.right is None:
                node.right = BST.Node(item)
            else:
                recurse(node.right)

        if self.is_empty():
            self.root = BST.Node(item)
        else:
            recurse(self.root)
        self.size += 1

    def get_min(self):
        """获取二叉搜索树中最小项"""

        def recurse(node):
            if node.left is None:
                return node.data
            return recurse(node.left)

        return recurse(self.root)

    def get_max(self):
        """获取二叉搜索树中最大项"""

        def recurse(node):
            if node.right is None:
                return node.data
            return recurse(node.right)

        return recurse(self.root)

    def remove_min(self):
        """删除二叉搜索树中最小项"""
        if self.size == 0:
            raise KeyError("二叉搜索树为空！")

        def recurse(node):
            if node.left.left is None:
                node.left = node.left.right
            else:
                recurse(node.left)

        recurse(self.root)
        self.size -= 1

    def remove_max(self):
        """删除二叉搜索树中最大项"""
        if self.size == 0:
            raise KeyError("二叉搜索树为空！")

        def recurse(node):
            if node.right.right is None:
                node.right = node.right.left
            else:
                recurse(node.right)

        recurse(self.root)
        self.size -= 1

    def remove(self, item):
        """在二叉搜索树中删除项 item。"""
        if item not in self:
            raise KeyError("需要移除的项不存在！")

        def recurse(node):
            if item == node.data:
                if node.left is None:  # 左子树为空
                    return node.right
                elif node.right is None:  # 右子树为空
                    return node.left
                else:  # 左右子树均不为空
                    new_node = self._pop_right_min(node)
                    new_node.left, new_node.right = node.left, node.right
                    return new_node
            elif item < node.data:
                node.left = recurse(node.left)
                return node
            else:
                node.right = recurse(node.right)
                return node

        self.root = recurse(self.root)

    @staticmethod
    def _pop_right_min(node):
        if node.right.left is None:
            pop_node = node.right
            node.right = node.right.right
        else:
            node = node.right
            while node.left.left is not None:
                node = node.left
            pop_node = node.left
            node.left = node.left.right
        return pop_node


bst = BST([10, 6, 3, 4, 5, 8, 9, 7, 17, 14, 19, 12, 18, 21, 24, 16])
# bst = BST([10, 6, 3, 4, 5])
print(bst)
# bst.remove_min()
# print(bst)
# bst.remove_max()
# print(bst)
# bst.remove(3)
# print(bst)

# for i in bst:
#     print(i)

# bst1 = BST([7, 17, 14, 19, 12])
# bst += bst1
# print(bst)

# print(list(bst.level_order()))
bst.remove_min()
print(bst)
