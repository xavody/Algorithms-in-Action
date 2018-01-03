package weightedGraph;

import java.util.Vector;

/**
 * 带权图的稀疏图——邻接表
 */
public class SparseWeightedGraph<Weight extends Number & Comparable> implements WeightedGraph {
    private int n;  // 节点数
    private int m;  // 边数
    private boolean directed;  // 是否为有向图
    private Vector<Edge<Weight>>[] g;  // 图的具体数据

    public SparseWeightedGraph(int n, boolean directed) {
        this.n = n;
        this.m = 0;  // 初始化没有任何边
        this.directed = directed;  // true 表示有向图，false 表示无向图

        // g 初始化为 n 个空的 vector, 表示每一个 g[i] 都为空, 即没有任何边
        this.g = (Vector<Edge<Weight>>[]) new Vector[n];
        for (int i = 0; i < n; i++) {
            g[i] = new Vector<>();
        }
    }

    // 返回节点个数
    @Override
    public int getV() {
        return n;
    }

    // 返回边数
    @Override
    public int getE() {
        return m;
    }

    // 向图中添加一个边
    @Override
    public void addEdge(Edge e) {
        assert e.getV() >= 0 && e.getV() < n;
        assert e.getW() >= 0 && e.getW() < n;
        g[e.getV()].add(new Edge(e));

        // 如果为无向图
        if (e.getV() != e.getW() && !directed)
            g[e.getW()].add(new Edge(e.getW(), e.getV(), e.getWeight()));

        m ++;
    }

    // 验证图中是否有从 v 到 w 的边
    @Override
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;

        for (int i = 0; i < g[v].size(); i++) {
            if (g[v].elementAt(i).other(i) == w)
                return true;
        }
        return false;
    }

    // 返回图中一个节点的所有邻边
    @Override
    public Iterable<Edge<Weight>> adj(int v) {
        assert v >= 0 && v < n;
        return g[v];
    }

    // 显示图的信息
    @Override
    public void show() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < g[i].size(); j++) {
                Edge e = g[i].elementAt(j);
                System.out.print("(to:" + e.other(i) + ", weight:" + e.getWeight() + ")\t");
            }
            System.out.println();
        }
    }
}
