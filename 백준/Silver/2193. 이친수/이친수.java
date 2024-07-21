// Dynamic Programming Alogrithm
import java.util.Scanner;

public class Main {
  static int n;
  static long d[][];

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    n = sc.nextInt();
    d = new long[n + 1][2]; // [각 자리수][0인 경우, 1인 경우]

    d[1][0] = 0;
    d[1][1] = 1;

    for (int i = 2; i <= n; i++) {
      d[i][0] = d[i - 1][0] + d[i - 1][1];
      d[i][1] = d[i - 1][0];
    }

    System.out.println(d[n][0] + d[n][1]);
  }
}