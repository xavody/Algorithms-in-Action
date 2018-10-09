"""
稠密图——邻接矩阵
"""


class DenseGraph:
    def __init__(self, n, directed):
        """
        g 初始化为 n*n 的布尔矩阵, 每一个 g[i][j] 均为 False, 表示没有任何边
        :param n: 节点数
        :param directed: True 表示有向图，False 表示无向图
        """
        assert n > 0
        self.n = n
        self.m = 0  # 边数，初始化没有任何边
        self.directed = directed
        self.g = [[False for _ in range(n)] for _ in range(n)]

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
        if self.has_edge(v, w):
            return

        self.g[v][w] = True

        # 如果为无向图
        if not self.directed:
            self.g[w][v] = True

        self.m += 1

    def has_edge(self, v, w):
        """验证图中是否有从 v 到 w 的边"""
        assert v in range(self.n)
        assert w in range(self.n)
        return self.g[v][w]

    def adj(self, v):
        """返回图中一个顶点的所有邻边"""
        return [i for i in range(self.n) if self.g[v][i]]

    def show(self):
        """显示图的信息"""
        for i in self.g:
            for j in i:
                print(j, end='\t')
            print()

