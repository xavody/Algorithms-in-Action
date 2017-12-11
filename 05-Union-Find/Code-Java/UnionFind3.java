package UnionFind;

/**
 * 并查集——版本三
 * 使用一个数组构建一棵指向父节点的树
 * 并查集时间复杂度近乎是 O(1)
 */
public class UnionFind3 {
    private int count;  // 数据个数
    private int[] parent;  // parent[i]表示元素所指向的父节点
    private int[] sz; // sz[i]表示以i为根的集合中元素个数

    public UnionFind3(int count) {
        parent = new int[count];
        sz = new int[count];
        this.count = count;
        for (int i = 0; i < count; i++) {
            parent[i] = i;
            sz[i] = 1;
        }
    }

    // 查找元素 p 所对应的集合编号
    // 复杂度为 O(h), h 为树的高
    public int find(int p) {
        assert p >= 0 && p < count;
        // 不断去查询父节点, 直到到达根节点
        // 根节点的特点: parent[p] == p
        while (p != parent[p])
            p = parent[p];
        return p;
    }

    // 查看元素 p 和元素 q 是否所属一个集合
    // 复杂度为 O(h), h 为树的高度
    public boolean isConnected(int p, int q) {
        return find(p) == find(q);
    }

    // 合并元素 p 和元素 q 所属的集合
    // 复杂度为 O(h), h 为树的高度
    public void union(int p, int q) {
        int pRoot = find(p);
        int qRoot = find(q);

        if (pRoot == qRoot)
            return;

        // 根据两个元素所在树的元素个数不同判断合并方向
        // 将元素个数少的集合合并到元素个数多的集合上
        if (sz[pRoot] > sz[qRoot]) {
            parent[qRoot] = pRoot;
            sz[pRoot] += sz[qRoot];
        } else {
            parent[pRoot] = qRoot;
            sz[qRoot] += sz[pRoot];
        }
    }
}
