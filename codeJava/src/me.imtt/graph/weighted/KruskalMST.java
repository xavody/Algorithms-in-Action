package me.imtt.graph.weighted;

import me.imtt.unionfind.UnionFind5;

import java.util.Vector;

/**
 * Kruskal 算法求最小生成树
 */
public class KruskalMST<Weight extends Number & Comparable> {
    /**
     * 最小生成树所包含的所有边
     */
    private Vector<Edge<Weight>> mst;

    /**
     * 最小生成树的权值
     */
    private Number mstWeight;

    /**
     * 使用Kruskal算法计算graph的最小生成树
     */
    public KruskalMST(WeightedGraph graph) {
        mst = new Vector<>();
        mstWeight = 0.0;

        ///将图中的所有边存放到一个最小堆中
        MinHeap<Edge<Weight>> minHeap = new MinHeap<>(graph.getE());
        for (int i = 0; i < graph.getV(); i++) {
            for (Object item: graph.adj(i)) {
                Edge<Weight> e = (Edge<Weight>) item;
                if (e.getV() <= e.getW()) {
                    System.out.println("insert: " + e);
                    minHeap.insert(e);
                }
            }
        }

        ///创建一个并查集, 来查看已经访问的节点的联通情况
        UnionFind5 unionFind = new UnionFind5(graph.getV());
        while (!minHeap.isEmpty() && mst.size() < graph.getV() - 1) {
            // 从最小堆中依次从小到大取出所有的边
            Edge<Weight> e = minHeap.extractMin();
            System.out.println("extract:" + e);
            if (unionFind.isConnected(e.getV(), e.getW())) {
                continue;
            }

            //否则, 将这条边添加进最小生成树, 同时标记边的两个端点联通
            mst.add(e);
            unionFind.union(e.getV(), e.getW());
        }
        System.out.println("last: " + minHeap.extractMin());

        ///计算最小生成树的权值
        for (int i = 0; i < mst.size(); i++) {
            mstWeight = mstWeight.doubleValue() + mst.elementAt(i).getWeight().doubleValue();
        }
    }

    /**
     * 返回最小生成树的所有边
     */
    public Vector<Edge<Weight>> getMst() {
        return mst;
    }

    /**
     * 返回最小生成树的权值
     */
    public Number getMstWeight() {
        return mstWeight;
    }
}
