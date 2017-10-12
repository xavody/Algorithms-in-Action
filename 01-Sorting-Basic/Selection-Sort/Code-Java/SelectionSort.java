import java.util.Arrays;

/**
 * 选择排序（升序）
 */
public class SelectionSort {
    public static void newSort(Comparable[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j].compareTo(arr[minIndex]) < 0)
                    minIndex = j;
            }
            swap(arr, i, minIndex);
        }
    }

    //交换数组中两个数
    public static void swap(Object[] arr, int index1, int index2) {
        Object temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }

    //选择排序算法测试
    public static void main(String[] args) {
//        //测试 Integer
//        Integer[] a = {10,9,8,7,6,5,4,3,2,1};
//        SelectionSort.newSort(a);
//        System.out.println(Arrays.toString(a));
//
//        //测试 Double
//        Double[] b = {4.4, 3.3, 2.2, 1.1};
//        SelectionSort.newSort(b);
//        System.out.println(Arrays.toString(b));
//
//        //测试 String
//        String[] c = {"D", "C", "B", "A"};
//        SelectionSort.newSort(c);
//        System.out.println(Arrays.toString(c));
//
//        //测试自定义类 People
//        People[] people = new People[4];
//        people[0] = new People("A", 23);
//        people[1] = new People("D", 22);
//        people[2] = new People("C", 26);
//        people[3] = new People("B", 22);
//        SelectionSort.newSort(people);
//        System.out.println(Arrays.toString(people));

        Integer[] arr = SortTestHelper.generateRandomArray(20, 5, 10);
        System.out.print("初始数组：");
        SortTestHelper.printArray(arr);
        SortTestHelper.testSort(arr);
    }
}
