package me.imtt.graph.basics;

/**
 * 图的接口
 */
public interface Graph {
    /**
     * 返回节点个数
     */
    public int getV();

    /**
     * 返回边数
     */
    public int getE();

    /**
     * 向图中添加一个边
     */
    public void addEdge(int v, int w);

    /**
     * 验证图中是否有从 v 到 w 的边
     */
    public boolean hasEdge(int v, int w);

    /**
     * 返回图中一个顶点的所有邻边
     */
    public Iterable<Integer> adj(int v);

    /**
     * 显示图的信息
     */
    public void show();
}
