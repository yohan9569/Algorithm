import java.util.Scanner;
import java.util.stream.IntStream;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] arr = IntStream.range(1, n+1).toArray();
        int a;
        int b;
        int tmp;
        
        for (int i = 0; i < m; i++) {
            a = sc.nextInt() - 1;
            b = sc.nextInt() - 1;
            tmp = arr[a];
            arr[a] = arr[b];
            arr[b] = tmp;
        }
        for (int e : arr) {
            System.out.print(e);
            System.out.print(" ");
        }
    }
}