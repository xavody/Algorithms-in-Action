package me.imtt.binarysearchtree;

import java.util.LinkedList;

/**
 * 二分搜索树
 */
public class BST<Key extends Comparable<Key>, Value> {
    private class Node {
        Key key;
        Value val;
        Node left, right;
        int n;
    
        private Node(Key key, Value val, int n) {
            this.key = key;
            this.val = val;
            this.n = n;
        }
    }
    /**
     * 二分搜索树的根结点
     */
    private Node root;

    /**
     * 返回二分搜索树的结点个数
     */
    public int size() {
        return size(root);
    }

    /**
     * 返回二分搜索树某结点为根结点的子树中结点的个数（含该结点）
     */
    private int size(Node node) {
        if (node == null) {
            return 0;
        }
        return node.n;
    }

    /**
     * 返回二分搜索树是否为空
     */
    public boolean isEmpty() {
        return root != null && root.n == 0;
    }

    /**
     * 向二分搜索树中插入一个新的(key, Value)数据对
     */
    public void insert(Key key, Value val) {
        root = insert(root, key, val);
    }

    /**
     * 如果 key 存在于 node 为根结点的子树中就更新它的值
     * 不存在就将 key-value 键值对作为新结点插入到子树中
     */
    private Node insert(Node node, Key key, Value val) {
        if (node == null) {
            return new Node(key, val, 1);
        }

        int cmp = node.key.compareTo(key);
        if (cmp == 0) {
            node.val = val;
        } else if (cmp < 0) {
            node.right = insert(node.right, key, val);
        } else {
            node.left = insert(node.left, key, val);
        }

        node.n = size(node.left) + size(node.right) + 1;
        return node;
    }

    /**
     * 在二分搜索树中搜索键 key 所对应的值。如果这个值不存在, 则返回 null
     */
    public Value search(Key key) {
        return search(root, key);
    }

    /**
     * 在以 node 为根结点的子树中查找并返回 key 所对应的值
     * 如果找不到返回 null
     */
    private Value search(Node node, Key key) {
        if (node == null) {
            return null;
        }

        int cmp = node.key.compareTo(key);
        if (cmp == 0) {
            return node.val;
        } else if (cmp < 0) {
            return search(node.right, key);
        } else {
            return search(node.left, key);
        }
    }

    /**
     * 深度优先遍历-前序遍历
     */
    public void preOrder() {
        preOrder(root);
    }

    /**
     * 对以 node 为根的二分搜索树进行基于递归的前序遍历
     */
    private void preOrder(Node node) {
        if (node != null) {
            System.out.println(node.key);
            preOrder(node.left);
            preOrder(node.right);
        }
    }

    /**
     * 深度优先遍历-中序遍历
     */
    public void inOrder() {
        inOrder(root);
    }

    /**
     * 对以 node 为根的二分搜索树进行基于递归的中序遍历
     */
    private void inOrder(Node node) {
        if (node != null) {
            inOrder(node.left);
            System.out.println(node.key);
            inOrder(node.right);
        }
    }

    /**
     * 深度优先遍历-后序遍历
     */
    public void postOrder() {
        postOrder(root);
    }

    /**
     * 对以 node 为根的二分搜索树进行基于递归的后序遍历
     */
    private void postOrder(Node node) {
        if (node != null) {
            postOrder(node.left);
            postOrder(node.right);
            System.out.println(node.key);
        }
    }

    /**
     * 广度优先遍历
     */
    public void levelOrder() {
        ///使用 LinkedList 作为辅助队列
        LinkedList<Node> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) {
            Node node = q.remove();
            System.out.println(node.key);

            if (node.left != null) {
                q.add(node.left);
            }
            if (node.right != null) {
                q.add(node.right);
            }
        }
    }

    /**
     * 返回二分搜索树的最小的键值
     */
    public Key getMin() {
        Node minNode = getMin(root);
        return minNode.key;
    }

    /**
     * 返回以 node 为根的二分搜索树的最小键值所在的结点
     */
    private Node getMin(Node node) {
        if (node.left == null) {
            return node;
        }
        return getMin(node.left);
    }

    /**
     * 返回二分搜索树的最大的键值
     */
    public Key getMax() {
        Node maxNode = getMax(root);
        return maxNode.key;
    }

    /**
     * 返回以 node 为根的二分搜索树的最大键值所在的结点
     */
    private Node getMax(Node node) {
        if (node.right == null) {
            return node;
        }
        return getMax(node.right);
    }

    /**
     * 删除二分搜索树中最小值所在结点
     */
    public void removeMin() {
        if (root != null) {
            root = removeMin(root);
        }
    }

    /**
     * 删除以 node 为根的二分搜索树中的最小结点
     * 返回删除结点后新的二分搜索树的根
     */
    private Node removeMin(Node node) {
        if (node.left == null) {
            Node nodeRight = node.right;
            node.right = null;
            return nodeRight;
        }
        node.left = removeMin(node.left);
        shiftN(node);
        return node;
    }

    /**
     * 删除二分搜索树中最大值所在结点
     */
    public void removeMax() {
        if (root != null) {
            root = removeMax(root);
        }
    }

    /**
     * 删除以 node 为根的二分搜索树中的最大结点
     * 返回删除结点后新的二分搜索树的根
     */
    private Node removeMax(Node node) {
        if (node.right == null) {
            Node nodeLeft = node.left;
            node.left = null;
            return nodeLeft;
        }
        node.right = removeMax(node.right);
        shiftN(node);
        return node;
    }

    /**
     * 从二分搜索树中删除键值为 key 的结点
     */
    public void remove(Key key) {
        root = remove(root, key);
    }

    /**
     * 删除以 node 为根的二分搜索树中键值为 key 的结点, 递归算法
     * 返回删除结点后新的二分搜索树的根
     */
    private Node remove(Node node, Key key) {
        if (node == null) {
            return null;
        }

        int cmp = node.key.compareTo(key);
        if (cmp > 0) {
            node.left = remove(node.left, key);
            shiftN(node);
            return node;
        } else if (cmp < 0) {
            node.right = remove(node.right, key);
            shiftN(node);
            return node;
        } else {
            if (node.left == null) { 
                ///待删除结点左子树为空
                Node nodeRight = node.right;
                node.right = null;
                return nodeRight;
            } else if (node.right == null) { 
                ///待删除结点右子树为空的情况
                Node nodeLeft = node.left;
                node.left = null;
                return nodeLeft;
            } else {
                ///待删除结点左右子树均不为空
                //找到比待删除结点大的最小结点, 即待删除结点右子树的最小结点
                //用这个结点顶替待删除结点的位置
                Node t = node;
                node = getMin(t.right);
                node.right = removeMin(t.right);
                node.left = t.left;
                shiftN(node);
                return node;
            }
        }
    }

    /**
     * 找到排名为 k 的键，即有 k 个小于它的键，排名从0开始
     */
    public Key select(int k) {
        return select(root, k).key;
    }

    /**
     * 返回排名为 k 的结点
     */
    private Node select(Node node, int k) {
        if (node == null) {
            return null;
        }

        int t = size(node.left);
        if (t > k) {
            return select(node.left, k);
        } else if (t < k) {
            return select(node.right, k - t - 1);
        } else {
            return node;
        }
    }

    /**
     * 找到 key 的排名，排名从0开始
     */
    public int rank(Key key) {
        return rank(root, key);
    }

    /**
     * 返回以 node 以根结点的子树中小于 node.key 的数量
     */
    private int rank(Node node, Key key) {
        if (node == null) {
            return 0;
        }

        int cmp = key.compareTo(node.key);
        if (cmp < 0) {
            return rank(node.left, key);
        } else if (cmp > 0) {
            return rank(node.right, key) + size(node.left) + 1;
        } else {
            return size(node.left);
        }
    }

    /**
     * 使各结点以本结点为根结点的子树中结点的个数正确
     */
    private void shiftN(Node node) {
        if (node.left == null && node.right == null) {
            node.n = 1;
        } else if (node.left == null) {
            node.n = node.right.n + 1;
        } else if (node.right == null) {
            node.n = node.left.n + 1;
        } else {
            node.n = node.left.n + node.right.n + 1;
        }
    }
}


