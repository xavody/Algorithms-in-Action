package sortingBasic.insertionSortAdvance;

import java.util.Arrays;
import sortingBasic.sortTestHelper.SortTestHelper;

public class Main {
    //比较优化后插入排序和选择排序性能
    public static void main(String[] args) {
        Integer[] integers1 = SortTestHelper
                .generateRandomArray(100, 0, 10000);
        Integer[] integers2 = Arrays.copyOf(integers1, integers1.length);

        System.out.print("初始数组：");
        SortTestHelper.printArray(integers1);
        System.out.println("使用优化后插入排序");
        SortTestHelper.testSort(integers1, "sortingBasic.insertionSortAdvance.InsertionSort");
        System.out.println();
        System.out.println("使用选择排序");
        SortTestHelper.testSort(integers2, "sortingBasic.insertionSortAdvance.SelectionSort");
    }
}

