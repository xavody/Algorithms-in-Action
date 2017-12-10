"""
并查集——版本二
使用一个数组构建一棵指向父节点的树
"""


class UnionFind2(object):
    def __init__(self, count):
        self.count = count  # 数据个数

        # parent[i]表示元素所指向的父节点
        # 初始化, 每一个 parent[i] 指向自己, 表示每一个元素自己自成一个集合
        self.parent = [i for i in range(self.count)]

    def find(self, p):
        """
        查找元素 p 所对应的集合编号
        复杂度为 O(h), h 为树的高度
        """
        assert p in range(self.count)
        # 不断去查询父节点, 直到到达根节点
        # 根节点的特点: parent[p] == p
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def is_connected(self, p, q):
        """
        查看元素 p 和元素 q 是否所属一个集合
        复杂度为 O(h), h 为树的高度
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        合并元素 p 和元素 q 所属的集合
        复杂度为 O(h), h 为树的高度
        """
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        self.parent[p_root] = q_root
