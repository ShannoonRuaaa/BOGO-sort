import java.util.Arrays;
import java.util.Scanner;
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


    public static int nxtInt(Scanner console) {
        int nxtInt = 0;
        while (true) {
            try {
                nxtInt = console.nextInt();
                break; // If input is valid, exit the loop
            } catch (Exception e) {
                System.out.print("Invalid input. Enter a number!");
                console.nextLine(); // Consume the invalid input
            }
        }
        return nxtInt;
    }

    public static void main(String[] args) {
        Scanner scanner= new Scanner(System.in);

        System.out.println("Type in the number of elements in the array: ");
        int len = nxtInt(scanner);
        int[] arr = new int[len];

        for (int i = 0; i < len; i++) {
            System.out.print("Enter a number: ");
            arr[i] = nxtInt(scanner);
        }
        System.out.println("Sorting....");
        System.out.println(Arrays.toString(BOGO(arr)));
    }

}