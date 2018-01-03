package weightedGraph;

import java.util.Vector;

/**
 * 带权图的稠密图——邻接矩阵
 */
public class DenseWeightedGraph<Weight extends Number & Comparable> implements WeightedGraph {
    private int n;  // 节点数
    private int m;  // 边数
    private boolean directed;  // 是否为有向图
    private Edge<Weight>[][] g;  // 图的具体数据

    public DenseWeightedGraph(int n, boolean directed) {
        assert n >= 0;
        this.n = n;
        this.m = 0;  // 初始化没有任何边
        this.directed = directed;  // true 表示有向图，false 表示无向图

        // g 初始化为 n*n 的布尔矩阵, 每一个 g[i][j] 均为 null, 表示没有任何边
        this.g = new Edge[n][n];
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

        if (hasEdge(e.getV(), e.getW())) return;

        g[e.getV()][e.getW()] = new Edge(e);

        // 如果为无向图
        if (e.getV() != e.getW() && !directed)
            g[e.getV()][e.getW()] = new Edge(e.getW(), e.getV(), e.getWeight());

        m ++;
    }

    // 验证图中是否有从 v 到 w 的边
    @Override
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;
        return g[v][w] != null;
    }

    // 返回图中一个节点的所有邻边
    @Override
    public Iterable<Edge<Weight>> adj(int v) {
        assert v >= 0 && v < n;
        Vector<Edge<Weight>> adjV = new Vector<>();
        for (int i = 0; i < n; i++)
            if (g[v][i] != null)
                adjV.add(g[v][i]);
        return adjV;
    }

    // 显示图的信息
    @Override
    public void show() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                if (g[i][j] != null)
                    System.out.print(g[i][j].getWeight() + "\t");
                else System.out.print("NULL\t");
            System.out.println();
        }
    }
}
