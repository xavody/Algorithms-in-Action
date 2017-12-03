package binarySearchTree;

import java.util.Arrays;

/**
 * 非递归的二分查找算法
 */
public class BinarySearch {
    // 在有序序列 lst 中, 查找 target
    // 如果找到 target, 返回相应的索引 index，否则返回 -1
    // 非递归方法
    public static int find(Comparable[] arr, Comparable target) {
        int l = 0;
        int r = arr.length;
        while (l <= r) {
            // 防止整形溢出，不使用 int mid = (l + r) / 2
            int mid = l + (r - l) / 2;
            if (arr[mid].compareTo(target) == 0)
                return mid;
            if (arr[mid].compareTo(target) > 0)
                r = mid - 1;
            else
                l = mid + 1;
        }
        return -1;
        // TODO:
    }

    // 递归方法
    public static int find2(Comparable[] arr, Comparable target, int l, int r) {
        if (l > r) return -1;
        int mid = l + (r - l) / 2;
        if (arr[mid].compareTo(target) == 0)
            return mid;
        else if (arr[mid].compareTo(target) > 0)
            return find2(arr, target, l, mid - 1);
        else return find2(arr, target, mid + 1, r);
    }
}
