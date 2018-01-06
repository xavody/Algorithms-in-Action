package weightedGraph;

import java.util.Vector;

/**
 * 使用 Prim 算法求带权无向连通图的最小生成树
 * 时间复杂度 O(ElogE)
 */
public class LazyPrimMST<Weight extends Number & Comparable> {
    private WeightedGraph<Weight> G;  //图的引用
    private MinHeap<Edge<Weight>> minHeap;  //最小堆, 算法辅助数据结构
    private boolean[] marked;  //标记数组, 在算法运行过程中标记节点 i 是否被访问
    private Vector<Edge<Weight>> mst;  //最小生成树所包含的所有边
    private Number mstWeight;  //最小生成树的权值

    public LazyPrimMST(WeightedGraph<Weight> graph) {
        G = graph;
        minHeap = new MinHeap<>(G.getE());
        marked = new boolean[G.getV()];
        mst = new Vector<>();
        mstWeight = 0.0;

        // lazy prime
        visit(0);
        while (!minHeap.isEmpty()) {
            // 使用最小堆找出已经访问的边中权值最小的边
            Edge<Weight> e = minHeap.extractMin();

            // 如果这条边的两端都已经访问过了, 则扔掉这条边
            if (marked[e.getV()] == marked[e.getW()])
                continue;
            // 否则, 这条边则应该存在在最小生成树中
            mst.add(e);

            // 访问和这条边连接的还没有被访问过的节点
            if (!marked[e.getV()])
                visit(e.getV());
            else
                visit(e.getW());
        }

        // 计算最小生成树的权值
        for (int i = 0; i < mst.size(); i++)
            mstWeight = mstWeight.doubleValue() + mst.elementAt(i).getWeight().doubleValue();
    }

    // 访问节点 v
    public void visit(int v) {
        assert !marked[v];
        marked[v] = true;

        // 将和节点 v 相连接的所有未访问的边放入最小堆中
        for (Edge<Weight> e: G.adj(v)) {
            if (!marked[e.other(v)])
                minHeap.insert(e);
        }
    }

    // 返回最小生成树的所有边
    public Vector<Edge<Weight>> getMst() {
        return mst;
    }

    // 返回最小生成树的权值
    public Number getMstWeight() {
        return mstWeight;
    }
}
