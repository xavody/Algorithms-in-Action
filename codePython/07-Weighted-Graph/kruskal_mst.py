"""
Kruskal 算法求最小生成树
"""
from .min_heap import MinHeap
from .union_find import UnionFind


class KruskalMst:
    def __init__(self, graph):
        self.mst = []  # 最小生成树所包含的所有边
        self.mst_weight = 0.0  # 最小生成树的权值

        # 将图中的所有边存放到一个最小堆中
        min_heap = MinHeap(graph.get_e())
        for i in range(graph.get_v()):
            for e in graph.adj(i):
                if e.get_v() <= e.get_w():
                    min_heap.insert(e)

        # 创建一个并查集, 来查看已经访问的节点的联通情况
        union_find = UnionFind(graph.get_v())
        while not min_heap.is_empty() and len(self.mst) < graph.get_v() - 1:
            e = min_heap.extract_min()
            # 如果该边的两个端点是联通的, 说明加入这条边将产生环, 扔掉这条边
            if union_find.is_connected(e.get_v(), e.get_w()):
                continue
            # 否则, 将这条边添加进最小生成树, 同时标记边的两个端点联通
            self.mst.append(e)
            union_find.union(e.get_v(), e.get_w())

        for i in self.mst:
            self.mst_weight += i.get_weight()

    def get_mst(self):
        """返回最小生成树的所有边"""
        return self.mst

    def get_mst_weight(self):
        """返回最小生成树的权值"""
        return self.mst_weight

