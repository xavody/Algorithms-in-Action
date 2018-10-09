package me.imtt.graph.basics;

import java.util.Vector;

/**
 * 稠密图——邻接矩阵
 */
public class DenseGraph implements Graph{
    /**
     * 节点数
     */
    private int n;  

    /**
     * 边数
     */
    private int m; 

    /**
     * 是否为有向图
     */
    private boolean directed;

    /**
     * 图的具体数据
     */
    private boolean[][] g;

    public DenseGraph(int n, boolean directed) {
        this.n = n;

        ///初始化没有任何边
        this.m = 0;  

        /// true 表示有向图，false 表示无向图
        this.directed = directed;  

        /// g 初始化为 n*n 的布尔矩阵, 每一个 g[i][j] 均为 false, 表示没有任何边
        // false为 boolean型变量的默认值
        this.g = new boolean[n][n];
    }

    @Override
    public int getV() {
        return n;
    }

    @Override
    public int getE() {
        return m;
    }

    @Override
    public void addEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;

        if (hasEdge(v, w)) {
            return;
        }

        g[v][w] = true;

        ///如果为无向图
        if (!directed) {
            g[w][v] = true;
        } 

        m ++;
    }

    @Override
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;
        return g[v][w];
    }

    @Override
    public Iterable<Integer> adj(int v) {
        assert v >= 0 && v < n;
        Vector<Integer> adjV = new Vector<>();
        for (int i = 0; i < n; i++) {
            if (g[v][i]) {
                adjV.add(i);
            }
        }
        return adjV;
    }

    @Override
    public void show() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(g[i][j] + "\t");
            }
            System.out.println();
        }
    }
}
