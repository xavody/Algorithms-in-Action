"""
并查集——版本一
"""


class UnionFind1(object):
    def __init__(self, n):
        self.count = n  # 数据个数
        self.id = [i for i in range(0, n)]  # 初始化, 每一个id[i]指向自己, 没有合并的元素

    def find(self, p):
        """
        查找元素 p 所对应的集合编号
        复杂度为 O(1)
        """
        assert p in range(self.count)
        return self.id[p]

    def is_connected(self, p, q):
        """
        查看元素 p 和 q 是否所属一个集合
        复杂度为 O(1)
        """
        return self.id[p] == self.id[q]

    def union(self, p, q):
        """
        合并元素 p 和元素 q 所属的集合
        复杂度为 O(n)
        """
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return

        # 将两个元素的所属集合编号合并
        for i in range(self.count):
            if self.id[i] == p_id:
                self.id[i] = q_id
