"""
广度优先遍历
同时求出了无权图的最短路径
"""
import queue


class ShortestPath:
    def __init__(self, graph, s):
        """寻路算法, 寻找图 graph 从 s 点到其他点的路径"""
        self.G = graph  #图的引用
        assert s in range(self.G.get_v())
        self.visited = [False for _ in range(self.G.get_v())]  #记录 dfs 的过程中节点是否被访问
        self.s = s  #起始点
        self._from = [-1 for _ in range(self.G.get_v())]  # 记录路径, _from[i]表示查找的路径上i的上一个节点
        self._ord = [-1 for _ in range(self.G.get_v())]  # 记录路径中节点的次序。_ord[i]表示i节点在路径中的次序。

        # 无向图最短路径算法, 从 s 开始广度优先遍历整张图
        q = queue.Queue()
        q.put(s)
        self.visited[s] = True
        self._ord[s] = 0
        while not q.empty():
            v = q.get()
            for i in self.G.adj(v):
                if not self.visited[i]:
                    q.put(i)
                    self.visited[i] = True
                    self._from[i] = v
                    self._ord[i] = self._ord[v] + 1

    def path(self, w):
        """查询从 s 点到 w 点的路径, 存放在 vec 中"""
        assert self.has_path(w)
        vec = []
        p = w
        while p != -1:
            vec.append(p)
            p = self._from[p]
        return vec[::-1]

    def has_path(self, w):
        """查询从 s 点到 w 点是否有路径"""
        assert w in range(self.G.get_v())
        return self.visited[w]

    def show_path(self, w):
        """打印出从 s 点到 w 点的路径"""
        assert self.has_path(w)
        vec = self.path(w)
        for i in vec:
            if i == vec[-1]:
                print(i)
            else:
                print(i, end='->')

    def length(self, w):
        """查看从 s 点到 w 点的最短路径长度。若从 s 到 w 不可达，返回-1"""
        assert w in range(self.G.get_v())
        return self._ord[w]
