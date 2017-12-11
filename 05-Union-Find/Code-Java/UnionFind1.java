package UnionFind;

/**
 * 并查集——版本一
 * 并查集时间复杂度近乎是 O(1)
 */
public class UnionFind1 {
    private int count;  // 数据个数
    private int[] id;

    public UnionFind1(int n) {
        count = n;
        id = new int[n];

        // 初始化, 每一个id[i]指向自己, 没有合并的元素
        for (int i = 0; i < n; i++)
            id[i] = i;
    }

    // 查找元素 p 所对应的集合编号
    // 复杂度为 O(1)
    public int find(int p) {
        assert p >= 0 && p < count;
        return id[p];
    }

    // 查看元素 p 和 q 是否所属一个集合
    // 复杂度为 O(1)
    public boolean isConnected(int p, int q) {
        return id[p] == id[q];
    }

    // 合并元素 p 和元素 q 所属的集合
    // 复杂度为 O(n)
    public void union(int p, int q) {
        int pId = id[p];
        int qId = id[q];

        if (pId == qId)
            return;

        // 将两个元素的所属集合编号合并
        for (int i = 0; i < count; i++)
            if (id[i] == pId)
                id[i] = qId;
    }
}
