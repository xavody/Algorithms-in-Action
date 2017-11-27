package binarySearchTree;

import java.util.LinkedList;

/**
 * 二叉搜索树
 */
public class BST<Key extends Comparable<Key>, Value> {
    // 二叉搜索树的根节点
    private Node root;

    private class Node {
        private Key key; // 键
        private Value val; // 值
        private Node left, right; // 指向子节点的链接
        private int N; // 该节点为根节点的子树中节点的个数（含该节点）

        private Node(Key key, Value val, int N) {
            this.key = key;
            this.val = val;
            this.N = N;
        }
    }

    // 返回二分搜索树的节点个数
    public int size() {
        return size(root);
    }

    // 返回二分搜索树是否为空
    public boolean isEmpty() {
        return root != null && root.N == 0;
    }

    // 向二分搜索树中插入一个新的(key, Value)数据对
    public void insert(Key key, Value val) {
        root = insert(root, key, val);
    }

    // 在二分搜索树中搜索键 key 所对应的值。如果这个值不存在, 则返回 null
    public Value search(Key key) {
        return search(root, key);
    }

    // 深度优先遍历-前中后序遍历
    public void preOrder() {
        preOrder(root);
    }

    public void inOrder() {
        inOrder(root);
    }

    public void postOrder() {
        postOrder(root);
    }

    // 广度优先遍历
    public void levelOrder() {
        // 使用 LinkedList 作为辅助队列
        LinkedList<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            Node node = q.remove();
            System.out.println(node.key);

            if (node.left != null)
                q.add(node.left);
            if (node.right != null)
                q.add(node.right);
        }
    }

    /*
    辅助函数
     */

    // 返回二分搜索树某节点为根节点的子树中节点的个数（含该节点）
    private int size(Node node) {
        if (node == null)
            return 0;
        return node.N;
    }


    // 如果 key 存在于 node 为根节点的子树中就更新它的值
    // 不存在就将 key-value 键值对作为新节点插入到子树中
    private Node insert(Node node, Key key, Value val) {
        if (node == null)
            return new Node(key, val, 1);
        int cmp = node.key.compareTo(key);
        if (cmp == 0)
            node.val = val;
        else if (cmp < 0)
            node.right = insert(node.right, key, val);
        else
            node.left = insert(node.left, key, val);
        node.N = size(node.left) + size(node.right) + 1;
        return node;
    }

    // 在以 node 为根节点的子树中查找并返回 key 所对应的值
    // 如果找不到返回 null
    private Value search(Node node, Key key) {
        if (node == null)
            return null;
        int cmp = node.key.compareTo(key);
        if (cmp == 0)
            return node.val;
        else if (cmp < 0)
            return search(node.right, key);
        else
            return search(node.left, key);
    }

    // 深度优先遍历
    // 对以 node 为根的二叉搜索树进行基于递归的前序遍历
    private void preOrder(Node node) {
        if (node != null) {
            System.out.println(node.key);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    // 深度优先遍历
    // 对以 node 为根的二叉搜索树进行基于递归的中序遍历
    private void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.println(node.key);
            inOrder(node.right);
        }
    }

    // 深度优先遍历
    // 对以 node 为根的二叉搜索树进行基于递归的后序遍历
    private void postOrder(Node node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            System.out.println(node.key);
        }
    }

    public static void main(String[] args) {
        BST bst = new BST();

        int N = 20;
        Integer[] arr = new Integer[N];
        for(int i = 0 ; i < N ; i ++)
            arr[i] = i;

        // 打乱数组顺序
        for(int i = 0 ; i < N ; i++){
            int pos = (int) (Math.random() * (i+1));
            Integer t = arr[pos];
            arr[pos] = arr[i];
            arr[i] = t;
        }

        for (int i = 0; i < N; i++) {
            bst.insert(arr[i], Integer.toString(arr[i]));
        }

        System.out.println(bst.size());
        System.out.println();

        bst.inOrder();
        System.out.println();
        bst.levelOrder();
    }
}
