package weightedGraph;

import java.util.Vector;

/**
 * 使用优化的Prim算法求图的最小生成树
 */
public class PrimMST<Weight extends Number & Comparable> {
    private WeightedGraph<Weight> G;  //图的引用
    private IndexMinHeap<Weight> indexMinHeap;  //最小索引堆, 算法辅助数据结构
    private Edge<Weight>[] edgeTo;  //访问的点所对应的边, 算法辅助数据结构
    private boolean[] marked;  //标记数组, 在算法运行过程中标记节点 i 是否被访问
    private Vector<Edge<Weight>> mst;  //最小生成树所包含的所有边
    private Number mstWeight;  //最小生成树的权值

    public PrimMST(WeightedGraph graph) {
        G = graph;
        assert graph.getE() >= 1;
        indexMinHeap = new IndexMinHeap<>(graph.getV());
        mstWeight = 0.0;

        marked = new boolean[G.getV()];
        edgeTo = new Edge[G.getV()];
        for (int i = 0; i < G.getV(); i++) {
            marked[i] = false;
            edgeTo[i] = null;
        }

        mst = new Vector<>();

        visit(0);
        while (!indexMinHeap.isEmpty()) {
            // 使用最小索引堆找出已经访问的边中权值最小的边
            // 最小索引堆中存储的是点的索引, 通过点的索引找到相对应的边
            int v = indexMinHeap.extractMinIndex();
            assert edgeTo[v] != null;
            mst.add(edgeTo[v]);
            visit(v);
        }

        // 计算最小生成树的权值
        for (int i = 0; i < mst.size(); i++)
            mstWeight = mstWeight.doubleValue() + mst.elementAt(i).getWeight().doubleValue();
    }

    // 访问节点 v
    public void visit(int v) {
        assert !marked[v];
        marked[v] = true;

        // 将和节点v相连接的未访问的另一端点, 和与之相连接的边, 放入最小堆中
        for (Object item : G.adj(v)) {
            Edge<Weight> e = (Edge<Weight>) item;
            int w = e.other(v);
            if (!marked[w]) {
                // 如果没有访问过这个端点, 直接将这个端点和与之相连接的边加入索引堆
                if (edgeTo[w] == null) {
                    edgeTo[w] = e;
                    indexMinHeap.insert(w, e.getWeight());
                } else if (e.getWeight().compareTo(edgeTo[w].getWeight()) < 0) {
                    // 如果访问过这个端点, 但现在的边比之前考虑的边更短, 则进行替换
                    edgeTo[w] = e;
                    indexMinHeap.change(w, e.getWeight());
                }
            }
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
