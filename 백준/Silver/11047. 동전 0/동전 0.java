// Greedy Alogrithm
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), k = sc.nextInt(), a[] = new int[n];
    for (int i = 0; i < n; i++)
      a[i] = sc.nextInt();
    sc.close();

    int cnt = 0;
    while (k > 0) {
      n--;
      if (k >= a[n]) {
        cnt += k / a[n];
        k %= a[n];
      }
    }

    System.out.println(cnt);
  }
}