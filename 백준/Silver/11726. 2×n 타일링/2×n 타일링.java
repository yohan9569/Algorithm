// Dynamic Programming Alogrithm
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    sc.close();
    long d[] = new long[1001];
    d[1] = 1;
    d[2] = 2;
    for (int i = 3; i <= n; i++)
      d[i] = (d[i - 1] + d[i - 2]) % 10007;
    System.out.println(d[n]);
  }
}