"""
二叉搜索树
"""
import queue
from random import randint


class BST(object):
    class Node(object):
        """二分查找树上一个节点"""

        def __init__(self, key=None, val=None, n=None):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.N = n  # 该节点为根节点的子树中节点的个数（含该节点）

    def __init__(self):
        """根节点"""
        self.__root = None

    def size(self):
        """返回二分搜索树的节点个数"""
        return self.__size_node(self.__root)

    def is_empty(self):
        """返回二分搜索树是否为空"""
        return self.__root.N == 0 and self.__root.N is None

    def insert(self, key, val):
        """
        向二分搜索树中插入一个新的(key, Value)数据对
        查找 key，找到则更新它的值，否则创建一个新的节点
        """
        self.__root = self.__insert_node(self.__root, key, val)

    def search(self, key):
        """在二分搜索树中搜索键 key 所对应的值。如果这个值不存在, 则返回 None"""
        return self.__search_node(self.__root, key)

    def pre_order(self):
        """深度优先遍历-前序遍历"""
        self.__pre_order_node(self.__root)

    def in_order(self):
        """深度优先遍历-中序遍历"""
        self.__in_order_node(self.__root)

    def post_order(self):
        """深度优先遍历-后序遍历"""
        self.__post_order_node(self.__root)

    def level_order(self):
        """广度优先遍历"""
        q = queue.Queue()
        q.put(self.__root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)

    """辅助函数"""

    @staticmethod
    def __size_node(node):
        """返回二分搜索树某节点为根节点的子树中节点的个数（含该节点）"""
        return node.N if node else 0

    def __insert_node(self, node, key, val):
        """
        如果 key 存在于 node 为根节点的子树中就更新它的值
        不存在就将 key-value 键值对作为新节点插入到子树中
        """
        if node is None:
            return BST.Node(key, val, 1)
        if int(node.key) == key:
            node.val = val
        if int(node.key) < key:
            node.right = self.__insert_node(node.right, key, val)
        else:
            node.left = self.__insert_node(node.left, key, val)
        node.N = self.__size_node(node.left) + self.__size_node(node.right) + 1
        return node

    def __search_node(self, node, key):
        """在以 node 为根节点的子树中查找并返回 key 所对应的值如果找不到返回 null"""
        if node is None:
            return None
        if node.key == key:
            return node.val
        elif node.key < key:
            return self.__search_node(node.right, key)
        else:
            return self.__search_node(node.left, key)

    def __pre_order_node(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的前序遍历
        """
        if node:
            print(node.val)
            self.__pre_order_node(node.left)
            self.__pre_order_node(node.right)

    def __in_order_node(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的中序遍历
        """
        if node:
            self.__in_order_node(node.left)
            print(node.val)
            self.__in_order_node(node.right)

    def __post_order_node(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的后序遍历
        """
        if node:
            self.__post_order_node(node.left)
            self.__post_order_node(node.right)
            print(node.val)


if __name__ == '__main__':
    nodes = BST()
    lst = [randint(10, 30) for _ in range(20)]
    for i in lst:
        nodes.insert(i, str(i))
    print(nodes.size())
    print()

    nodes.in_order()
    print()

    nodes.level_order()
