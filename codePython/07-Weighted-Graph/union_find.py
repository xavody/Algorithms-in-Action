"""
并查集，使用一个数组构建一棵指向父节点的树
时间复杂度近乎是 O(1)
"""


class UnionFind(object):
    def __init__(self, count):
        self.count = count  # 数据个数

        # parent[i]表示元素所指向的父节点
        # 初始化, 每一个 parent[i] 指向自己, 表示每一个元素自己自成一个集合
        self.parent = [i for i in range(self.count)]

        # rank[i] 表示以i为根的集合所表示的树的层数
        self.rank = [1 for _ in range(self.count)]

    def find(self, p):
        """
        查找元素 p 所对应的集合编号
        复杂度为 O(h), h 为树的高度
        """
        assert p in range(self.count)
        # 不断去查询父节点, 直到到达根节点
        # 根节点的特点: parent[p] == p

        # 路径压缩版本一，实践性更好
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

        # 路径压缩版本二，理论上更好
        # if p != self.parent[p]:
        #     self.parent[p] = self.find(self.parent[p])
        # return self.parent[p]

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

        # 根据两个元素所在树的元素个数不同判断合并方向
        # 将元素个数少的集合合并到元素个数多的集合上
        if self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[p_root] = q_root
        else:
            self.parent[p_root] = q_root
            self.rank[q_root] += 1
