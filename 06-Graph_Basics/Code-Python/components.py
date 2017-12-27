"""
求无权图的联通分量
"""


class Components:
    """求无向图的连通分量"""
    def __init__(self, graph):
        self.G = graph  #图的引用
        self.visited = [False for _ in range(self.G.get_v())]  #记录 dfs 的过程中节点是否被访问
        self.count = 0  #记录连通分量个数
        self.id = [-1 for _ in range(self.G.get_v())]  #每个节点所对应的连通分量标记

        # 求图的连通分量
        for i in range(self.G.get_v()):
            if not self.visited[i]:
                self.dfs(i)
                self.count += 1

    def dfs(self, v):
        """图的深度优先遍历"""
        self.visited[v] = True
        self.id[v] = self.count

        for i in self.G.adj(v):
            if not self.visited[i]:
                self.dfs(i)

    def get_count(self):
        """返回图的连通分量个数"""
        return self.count

    def is_connected(self, v, w):
        """查询点 v 和点 w 是否连通"""
        assert v in range(self.G.get_v())
        assert w in range(self.G.get_v())
        return self.id[v] == self.id[w]
