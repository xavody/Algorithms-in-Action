package graphBasics;

import java.util.Vector;

/**
 * 稀疏图——邻接表
 */
public class SparseGraph implements Graph{
    private int n;  // 节点数
    private int m;  // 边数
    private boolean directed;  // 是否为有向图
    private Vector<Integer>[] g;  // 图的具体数据

    public SparseGraph(int n, boolean directed) {
        this.n = n;
        this.m = 0;  // 初始化没有任何边
        this.directed = directed;  // true 表示有向图，false 表示无向图

        // g 初始化为 n 个空的 vector, 表示每一个 g[i] 都为空, 即没有任何边
        this.g = (Vector<Integer>[]) new Vector[n];
        for (int i = 0; i < n; i++) {
            g[i] = new Vector<>();
        }
    }

    // 返回节点个数
    public int getV() {
        return n;
    }

    // 返回边数
    public int getE() {
        return m;
    }

    // 向图中添加一个边
    public void addEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;
        g[v].add(w);

        // 如果为无向图
        if (v != w && !directed)
            g[w].add(v);

        m ++;
    }

    // 验证图中是否有从 v 到 w 的边
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;

        for (int i = 0; i < g[v].size(); i++) {
            if (g[v].elementAt(i) == w)
                return true;
        }
        return false;
    }

    // 返回图中一个顶点的所有邻边
    public Iterable<Integer> adj(int v) {
        assert v >= 0 && v < n;
        return g[v];
    }

    // 显示图的信息
    public void show() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < g[i].size(); j++)
                System.out.print(g[i].elementAt(j) + "\t");
            System.out.println();
        }
    }
}
