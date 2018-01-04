"""
使用 Prim 算法求带权无向连通图的最小生成树
"""
from weighted_graph.min_heap import MinHeap
from weighted_graph.edge import Edge
from weighted_graph.sparse_weighted_graph import SparseWeightedGraph


class LazyPrimMST:
    def __init__(self, graph):
        self.G = graph  #图的引用
        self.minHeap = MinHeap(self.G.get_e())
        self.marked = [False for _ in range(self.G.get_v())]
        self.mst = []
        self.mst_weight = 0.0

        self.visit(0)
        while not self.minHeap.is_empty():
            # 使用最小堆找出已经访问的边中权值最小的边
            e = self.minHeap.extract_min()
            if self.marked[e.get_v()] == self.marked[e.get_w()]:
                # 如果这条边的两端都已经访问过了, 则扔掉这条边
                continue
            # 否则, 这条边则应该存在在最小生成树中
            self.mst.append(e)

            # 访问和这条边连接的还没有被访问过的节点
            if not self.marked[e.get_v()]:
                self.visit(e.get_v())
            else:
                self.visit(e.get_w())

        for i in self.mst:
            print('-' + str(i.get_weight()))
            self.mst_weight += i.get_weight()
            print('-' + str(self.mst_weight))

    def visit(self, v):
        """访问节点 v"""
        assert not self.marked[v]
        self.marked[v] = True

        # 将和节点 v 相连接的所有未访问的边放入最小堆中
        for e in self.G.adj(v):
            if not self.marked[e.get_w()]:
                self.minHeap.insert(e)

    def get_mst(self):
        """返回最小生成树的所有边"""
        return self.mst

    def get_mst_weight(self):
        """返回最小生成树的权值"""
        return self.mst_weight

