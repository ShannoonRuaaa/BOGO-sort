import java.lang.reflect.Array;
import java.util.Arrays;

public class main {
public static int[] BOGO(int[] arr) {
    int[] temp = new int[arr.length];
    for (int i = 0; i < arr.length; i++) {
        temp[i] = arr[i];
    }
    while (!isSorted(temp)) {
        for (int i = 0; i < temp.length; i++) {
            int rand = (int) (Math.random() * temp.length);
            int temp2 = temp[i];
            temp[i] = temp[rand];
            temp[rand] = temp2;
        }
    }
    return temp;
}
    public static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
}
    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 6, 5};
        System.out.println(Arrays.toString(BOGO(arr)));
    }
}