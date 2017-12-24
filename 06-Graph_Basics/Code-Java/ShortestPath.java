package graphBasics;

import java.util.LinkedList;
import java.util.Stack;
import java.util.Vector;

public class ShortestPath {
    private Graph G;
    private int s;  //起始点
    private boolean[] visited;  //记录dfs的过程中节点是否被访问
    private int[] from;  //记录路径, from[i]表示查找的路径上i的上一个节点
    private int[] ord;  //记录路径中节点的次序。ord[i]表示i节点在路径中的次序。

    // 寻路算法, 寻找图 graph 从 s 点到其他点的路径
    public ShortestPath(Graph graph, int s) {
        G = graph;
        assert s >= 0 && s < G.getV();

        this.s = s;
        visited = new boolean[G.getV()];
        from = new int[G.getV()];
        ord = new int[G.getV()];

        for (int i = 0; i < G.getV(); i++) {
            visited[i] = false;
            from[i] = -1;
            ord[i] = -1;
        }

        // 无向图最短路径算法, 从 s 开始广度优先遍历整张图
        LinkedList<Integer> q = new LinkedList<>();
        q.push(s);
        visited[s] = true;
        ord[s] = 0;
        while (!q.isEmpty()) {
            int v = q.pop();
            for (int i: G.adj(v)) {
                if (!visited[i]) {
                    q.push(i);
                    visited[i] = true;
                    from[i] = v;
                    ord[i] = ord[v] + 1;
                }
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

    // 查看从 s 点到 w 点的最短路径长度
    // 若从 s 到 w 不可达，返回-1
    public int length(int w){
        assert w >= 0 && w < G.getV();
        return ord[w];
    }
}
