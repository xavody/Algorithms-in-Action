package me.imtt.graph.basics;

import java.util.Vector;

/**
 * 稀疏图——邻接表
 */
public class SparseGraph implements Graph{
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
    private Vector<Integer>[] g;

    public SparseGraph(int n, boolean directed) {
        this.n = n;

        ///初始化没有任何边
        this.m = 0;

        /// true 表示有向图，false 表示无向图
        this.directed = directed; 

        /// g 初始化为 n 个空的 vector, 表示每一个 g[i] 都为空, 即没有任何边
        this.g = (Vector<Integer>[]) new Vector[n];
        for (int i = 0; i < n; i++) {
            g[i] = new Vector<>();
        }
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
        g[v].add(w);

        ///如果为无向图
        if (v != w && !directed) {
            g[w].add(v);
        }

        m ++;
    }

    @Override
    public boolean hasEdge(int v, int w) {
        assert v >= 0 && v < n;
        assert w >= 0 && w < n;

        for (int i = 0; i < g[v].size(); i++) {
            if (g[v].elementAt(i) == w) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Iterable<Integer> adj(int v) {
        assert v >= 0 && v < n;
        return g[v];
    }

    @Override
    public void show() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < g[i].size(); j++) {
                System.out.print(g[i].elementAt(j) + "\t");
            }
            System.out.println();
        }
    }
}
