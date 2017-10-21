package sortingBasic.insertionSort;

import java.util.Arrays;
import sortingBasic.sortTestHelper.SortTestHelper;

public class Main {
    //比较插入排序和选择排序性能
    public static void main(String[] args) {
        Integer[] integers1 = SortTestHelper
                .generateRandomArray(10, 0, 1000);
        Integer[] integers2 = Arrays.copyOf(integers1, integers1.length);

        System.out.print("初始数组：");
        SortTestHelper.printArray(integers1);
        System.out.println("使用插入排序");
        SortTestHelper.testSort(integers1, "sortingBasic.insertionSort.InsertionSort");
        System.out.println("使用选择排序");
        SortTestHelper.testSort(integers2, "sortingBasic.selectionSort.SelectionSort");
    }
}

