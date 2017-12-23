package graphBasics;

/**
 * 求无权图的联通分量
 */
public class Components {
    private Graph G;
    private boolean[] visited; //记录 dfs 的过程中节点是否被访问
    private int count;  //记录联通分量个数
    private int[] id;  //每个节点所对应的联通分量标记

    public Components(Graph graph) {
        G = graph;
        visited = new boolean[G.getV()];
        id = new int[G.getV()];
        count = 0;

        for (int i = 0; i < G.getV(); i++) {
            visited[i] = false;
            id[i] = -1;
        }

        // 求图的联通分量
        for (int i = 0; i < G.getV(); i++) {
            if (!visited[i]) {
                dfs(i);
                count++;
            }
        }
    }

    // 图的深度优先遍历
    public void dfs(int v) {
        visited[v] = true;
        id[v] = count;

        for (int i: G.adj(v)) {
            if (!visited[i])
                dfs(i);
        }
    }

    // 返回图的联通分量个数"
    public int getCount() {
        return count;
    }

    // 查询点 v 和点 w 是否联通
    public boolean isConnected(int v, int w) {
        assert v >= 0 && v < G.getV();
        assert w >= 0 && w < G.getV();
        return id[v] == id[w];
    }
}
