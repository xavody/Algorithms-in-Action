package graphBasics;

import java.util.Arrays;

/**
 * 稠密图——邻接矩阵
 */
public class DenseGraph {
    private int n;  // 节点数
    private int m;  // 边数
    private boolean directed;  // 是否为有向图
    private boolean[][] g;  // 图的具体数据

    public DenseGraph(int n, boolean directed) {
        this.n = n;
        this.m = 0;  // 初始化没有任何边
        this.directed = directed;  // true 表示有向图，false 表示无向图

        // g 初始化为 n*n 的布尔矩阵, 每一个 g[i][j] 均为 false, 表示没有任何边
        // false为 boolean型变量的默认值
        this.g = new boolean[n][n];
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

        if (hasEdge(v, w)) return;

        g[v][w] = true;

        // 如果为无向图
        if (!directed) g[w][v] = true;

        m ++;
    }

    // 验证图中是否有从 v 到 w 的边
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;
        return g[v][w];
    }
}
