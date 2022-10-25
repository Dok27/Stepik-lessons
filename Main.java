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





//        int[][] mas = new int[n][n];
//        int[][] mas2 = new int[n][n];
//        for (int i = 0; i<n; i++){
//            for (int j = 0; j<n; j++){
//                mas[i][j] = sc.nextInt();
//            }
//        }
//        for (int i = 0; i<n; i++){
//            for (int j = 0; j<n; j++){
//                mas2[j][i] = mas[i][j];
//            }
//        }
//        for (int i = 0; i<n; i++){
//            for (int j = 0; j<n; j++){
//                System.out.print(mas2[i][j]+" ");
//            }
//            System.out.println();
//        }
//    }


