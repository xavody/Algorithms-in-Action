package graphBasics;

import java.util.Stack;
import java.util.Vector;

/**
 * 寻路
 */
public class Path {
    private Graph G;
    private int s;  //起始点
    private boolean[] visited;  //记录dfs的过程中节点是否被访问
    private int[] from;  //记录路径, from[i]表示查找的路径上i的上一个节点

    // 寻路算法, 寻找图 graph 从 s 点到其他点的路径
    public Path(Graph graph, int s) {
        G = graph;
        assert s >= 0 && s < G.getV();

        this.s = s;
        visited = new boolean[G.getV()];
        from = new int[G.getV()];

        for (int i = 0; i < G.getV(); i++) {
            visited[i] = false;
            from[i] = -1;
        }

        dfs(s);
    }

    // 图的深度优先遍历
    public void dfs(int v) {
        visited[v] = true;

        for (int i: G.adj(v)) {
            if (!visited[i]) {
                from[i] = v;
                dfs(i);
            }
        }
    }

    // 查询从 s 点到 w 点是否有路径
    public boolean hasPath(int w) {
        assert w >= 0 && w < G.getV();
        return visited[w];
    }

    // 查询从 s 点到 w 点的路径, 存放在 vec 中
    public Vector<Integer> path(int w) {
        assert hasPath(w);

        Stack<Integer> stack = new Stack<>();
        int p = w;
        while (p != -1) {
            stack.push(p);
            p = from[p];
        }

        Vector<Integer> res = new Vector<>();
        while (!stack.isEmpty())
            res.add(stack.pop());

        return res;
    }

    // 打印出从 s 点到 w 点的路径
    public void showPath(int w) {
        assert hasPath(w);
        Vector<Integer> vec = path(w);
        for (int i: vec) {
            if (i == vec.lastElement())
                System.out.println(i);
            else System.out.print(i + "->");
        }
    }
}
