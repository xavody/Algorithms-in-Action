"""
使用优化的Prim算法求图的最小生成树
"""
from weighted_graph.index_min_heap import IndexMinHeap
from weighted_graph.edge import Edge
from weighted_graph.sparse_weighted_graph import SparseWeightedGraph


class PrimMst:
    def __init__(self, graph):
        assert graph.get_e() >= 1
        self.G = graph  # 图的引用
        self.index_min_heap = IndexMinHeap(self.G.get_v())  # 最小索引堆, 算法辅助数据结构
        self.edge_to = [None for _ in range(self.G.get_v())]  # 访问的点所对应的边, 算法辅助数据结构
        self.marked = [False for _ in range(self.G.get_v())]  # 标记数组, 在算法运行过程中标记节点 i 是否被访问
        self.mst = []  # 最小生成树所包含的所有边
        self.mst_weight = 0.0  # 最小生成树的权值

        self.visit(0)
        while not self.index_min_heap.is_empty():
            # 使用最小堆找出已经访问的边中权值最小的边
            # 最小索引堆中存储的是点的索引, 通过点的索引找到相对应的边
            v = self.index_min_heap.extract_min_index()
            assert self.edge_to[v] is not None
            self.mst.append(self.edge_to[v])
            self.visit(v)

        for i in self.mst:
            self.mst_weight += i.get_weight()

    def visit(self, v):
        """访问节点 v"""
        try:
            assert not self.marked[v]
        except:
            print('error!!!!!!!')
        self.marked[v] = True

        # 将和节点v相连接的未访问的另一端点, 和与之相连接的边, 放入最小堆中
        for e in self.G.adj(v):
            w = e.other(v)
            if not self.marked[w]:
                if self.edge_to[w] is None:
                    # 如果没有访问过这个端点, 直接将这个端点和与之相连接的边加入索引堆
                    self.edge_to[w] = e
                    self.index_min_heap.insert(w, e.get_weight())
                elif e.get_weight() < self.edge_to[w].get_weight():
                    self.edge_to[w] = e
                    self.index_min_heap.change(w, e.get_weight())

    def get_mst(self):
        """返回最小生成树的所有边"""
        return self.mst

    def get_mst_weight(self):
        """返回最小生成树的权值"""
        return self.mst_weight

