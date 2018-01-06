"""
带权图的稀疏图——邻接表
"""
from weighted_graph.edge import Edge


class SparseWeightedGraph:
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

    def add_edge(self, edge):
        """向图中添加一个边"""
        assert edge.get_v() in range(self.n)
        assert edge.get_w() in range(self.n)
        self.g[edge.get_v()].append(edge)

        if edge.get_v() != edge.get_w() and not self.directed:
            self.g[edge.get_w()].append(Edge(edge.get_w(), edge.get_v(), edge.get_weight()))

        self.m += 1

    def has_edge(self, v, w):
        """验证图中是否有从 v 到 w 的边"""
        assert v in range(self.n)
        assert w in range(self.n)
        for e in self.g[v]:
            if e.get_w == w:
                return True
        return False

    def adj(self, v):
        """返回图中一个节点的所有邻边"""
        return self.g[v]

    def show(self):
        """显示图的信息"""
        for i in self.g:
            for j in i:
                print('(to:' + str(j.get_w()) + ', weight:' + str(j.get_weight()) + ')', end='\t')
            print()

