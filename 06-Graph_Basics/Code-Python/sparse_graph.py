"""
稀疏图——邻接表
"""


class SparseGraph(object):
    def __init__(self, n, directed):
        """
        g 初始化为 n 个空的 list, 表示每一个 g[i] 都为空, 即没有任何边
        :param n: 节点数
        :param directed: True 表示有向图，False 表示无向图
        """
        assert n > 0
        self.n = n
        self.m = 0  # 边数，初始化没有任何边
        self.directed = directed
        self.g = [[] for _ in range(n)]

    def get_v(self):
        """返回节点个数"""
        return self.n

    def get_e(self):
        """返回边数"""
        return self.m

    def add_edge(self, v, w):
        """向图中添加一个边"""
        assert v in range(self.n)
        assert w in range(self.n)
        self.g[v].append(w)

        if v != w and not self.directed:
            self.g[w].append(v)

        self.m += 1

    def has_edge(self, v, w):
        """验证图中是否有从 v 到 w 的边"""
        assert v in range(self.n)
        assert w in range(self.n)
        if w in self.g[v]:
            return True
        return False
