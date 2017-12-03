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
        return self.__size(self.__root)

    def is_empty(self):
        """返回二分搜索树是否为空"""
        return self.__root.N == 0 and self.__root.N is None

    def insert(self, key, val):
        """
        向二分搜索树中插入一个新的(key, Value)数据对
        查找 key，找到则更新它的值，否则创建一个新的节点
        """
        self.__root = self.__insert(self.__root, key, val)

    def search(self, key):
        """在二分搜索树中搜索键 key 所对应的值。如果这个值不存在, 则返回 None"""
        return self.__search(self.__root, key)

    def pre_order(self):
        """深度优先遍历-前序遍历"""
        self.__pre_order(self.__root)

    def in_order(self):
        """深度优先遍历-中序遍历"""
        self.__in_order(self.__root)

    def post_order(self):
        """深度优先遍历-后序遍历"""
        self.__post_order(self.__root)

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

    def get_min(self):
        """返回二分搜索树的最小的键值"""
        min_node = self.__get_min(self.__root)
        return min_node.key

    def get_max(self):
        """返回二分搜索树的最大的键值"""
        max_node = self.__get_max(self.__root)
        return max_node.key

    def remove_min(self):
        """删除二分搜索树中最小值所在节点"""
        if self.__root is not None:
            self.__root = self.__remove_min(self.__root)

    def remove_max(self):
        """删除二分搜索树中最小值所在节点"""
        if self.__root is not None:
            self.__root = self.__remove_max(self.__root)

    def remove(self, key):
        """从二分搜索树中删除键值为 key 的节点"""
        self.__remove(self.__root, key)

    def select(self, k):
        """找到排名为 k 的键，即有 k 个小于它的键，排名从0开始"""
        return self.__select(self.__root, k).key

    def rank(self, key):
        """找到 key 的排名，排名从0开始"""
        return self.__rank(self.__root, key)

    """辅助函数"""

    @staticmethod
    def __size(node):
        """返回二分搜索树某节点为根节点的子树中节点的个数（含该节点）"""
        return node.N if node else 0

    def __insert(self, node, key, val):
        """
        如果 key 存在于 node 为根节点的子树中就更新它的值
        不存在就将 key-value 键值对作为新节点插入到子树中
        """
        if node is None:
            return BST.Node(key, val, 1)
        if node.key == key:
            node.val = val
        if node.key < key:
            node.right = self.__insert(node.right, key, val)
        else:
            node.left = self.__insert(node.left, key, val)
        node.N = self.__size(node.left) + self.__size(node.right) + 1
        return node

    def __search(self, node, key):
        """在以 node 为根节点的子树中查找并返回 key 所对应的值如果找不到返回 null"""
        if node is None:
            return None
        if node.key == key:
            return node.val
        elif node.key < key:
            return self.__search(node.right, key)
        else:
            return self.__search(node.left, key)

    def __pre_order(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的前序遍历
        """
        if node:
            print(node.val)
            self.__pre_order(node.left)
            self.__pre_order(node.right)

    def __in_order(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的中序遍历
        """
        if node:
            self.__in_order(node.left)
            print(node.val)
            self.__in_order(node.right)

    def __post_order(self, node):
        """
        深度优先遍历
        对以 node 为根的二叉搜索树进行基于递归的后序遍历
        """
        if node:
            self.__post_order(node.left)
            self.__post_order(node.right)
            print(node.val)

    def __get_min(self, node):
        """返回以 node 为根的二分搜索树的最小键值所在的节点"""
        if node.left is None:
            return node
        return self.__get_min(node.left)

    def __get_max(self, node):
        """返回以 node 为根的二分搜索树的最大键值所在的节点"""
        if node.right is None:
            return node
        return self.__get_max(node.right)

    def __remove_min(self, node):
        """
        删除以 node 为根的二分搜索树中的最小节点
        返回删除节点后新的二分搜索树的根
        """
        if node.left is None:
            node_right = node.right
            node.right = None
            return node_right
        node.left = self.__remove_min(node.left)
        self.__shift_n(node)
        return node

    def __remove_max(self, node):
        """
        删除以 node 为根的二分搜索树中的最大节点
        返回删除节点后新的二分搜索树的根
        """
        if node.right is None:
            node_left = node.left
            node.left = None
            return node_left
        node.right = self.__remove_max(node.right)
        self.__shift_n(node)
        return node

    def __remove(self, node, key):
        """
        删除以 node 为根的二分搜索树中键值为 key 的节点, 递归算法
        返回删除节点后新的二分搜索树的根
        """
        if node is None:
            return node

        if node.key < key:
            node.right = self.__remove(node.right, key)
            self.__shift_n(node)
            return node
        elif node.key > key:
            node.left = self.__remove(node.left, key)
            self.__shift_n(node)
            return node
        else:
            if node.left is None:  #待删除节点左子树为空
                node_right = node.right
                node.right = None
                return node_right
            elif node.right is None:  #待删除节点右子树为空的情况
                node_left = node.left
                node.left = None
                return node_left
            else:
                """
                待删除节点左右子树均不为空
                找到比待删除节点大的最小节点, 即待删除节点右子树的最小节点
                用这个节点顶替待删除节点的位置
                """
                t = node
                node = self.__get_min(t)
                node.right = self.__remove_min(t)
                node.left = t.left
                self.__shift_n(node)
                return node

    @staticmethod
    def __shift_n(node):
        """使各节点以本节点为根节点的子树中节点的个数正确"""
        if node.left is None and node.right is None:
            node.N = 1
        elif node.left is None:
            node.N = node.right.N + 1
        elif node.right is None:
            node.N = node.left.N + 1
        else:
            node.N = node.right.N + node.left.N + 1

    def __select(self, node, k):
        """返回排名为 k 的节点"""
        if node is None:
            return None
        t = self.__size(node.left)
        if t < k:
            return self.__select(node.right, k - t - 1)
        elif t > k:
            return self.__select(node.left, k)
        else:
            return node

    def __rank(self, node, key):
        """返回以 node 以根节点的子树中小于 node.key 的数量"""
        if node is None:
            return 0
        if key < node.key:
            return self.__rank(node.left, key)
        elif key > node.key:
            return self.__rank(node.right, key) + self.__size(node.left) + 1
        else:
            return self.__size(node.left)


if __name__ == '__main__':
    nodes = BST()
    lst = [randint(10, 1000) for _ in range(20)]
    for i in lst:
        nodes.insert(i, str(i))
    print(nodes.size())
    print()

    nodes.in_order()
    print()

    print()
    print(nodes.get_min())
    print(nodes.get_max())

    print('********')
    # nodes.remove_min()
    # print(nodes.size())
    # nodes.remove_max()
    # print(nodes.size())
    # temp = lst[10]
    # print('temp:', temp)
    # nodes.remove(temp)
    # nodes.in_order()
    # print()
    # print(nodes.size())

    print(nodes.select(5))
    print('lst[10]', lst[10])
    print(nodes.rank(lst[10]))
