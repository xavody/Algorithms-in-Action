import java.lang.reflect.Method;
import java.util.Arrays;

/**
 * 随机生成数组
 */
public class SortTestHelper {
    private SortTestHelper(){}

    // 生成 n 个元素的整型数组，每个元素取值范围为 [minRange, maxRange]
    public static Integer[] generateRandomArray(int n, int minRange, int maxRange) {
        assert minRange <= maxRange; //使用断言检查 minRange 不大于 maxRange

        Integer[] integers = new Integer[n];

        for (int i = 0; i < n; i++) {
            integers[i] = (int)(Math.random() * (maxRange + 1 - minRange) + minRange);
        }
        return integers;
    }

    // 打印数组
    public static void printArray(Object arr[]) {
        System.out.println(Arrays.toString(arr));
    }

    // 判断数组排序后是否有序
    public static boolean isSorted(Comparable[] arr) {
        for (int i = 0; i < arr.length - 1; i++)
            if (arr[i].compareTo(arr[i + 1]) > 0)
                return false;
        return true;
    }


    // 用 Java 反射机制测试排序算法运行的正确性及所用时间
    public static void testSort(Comparable[] arr, String sortClassName) {
        try {
            // 获得排序类
            Class c = Class.forName(sortClassName);
            // 获得排序方法
            Method method = c.getMethod("newSort", new Class[]{Comparable[].class});

            Object[] params = new Object[]{arr};

            long beginTime = System.nanoTime();
            // 调用排序方法
            method.invoke(null, params);
            long endTime = System.nanoTime();

            //使用断言检查排序算法运行成功
            assert isSorted(arr);
            System.out.print("排序结果：");
            printArray(arr);
            System.out.println("排序运算时间：" + (endTime - beginTime) + "ns");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
