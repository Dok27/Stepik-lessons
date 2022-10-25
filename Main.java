import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int x = 0;
        int [] array = new int[n];
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }
        for (int j = 0; j < n; j++) {
            for (int i = 1; i < n; i++) {
                if (array[i - 1] > array[i]) {
                    x = array[i - 1];
                    array[i - 1] = array[i];
                    array[i] = x;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.print(array[i] + " ");
        }
    }
}

