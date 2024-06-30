
// Binary Search
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), k = sc.nextInt();
    sc.close();
    long start = 1, end = k, ans = 1;

    while (start <= end) {
      long mid = (start + end) / 2;
      long cnt = 0;

      for (int i = 1; i <= n; i++)
        cnt += Math.min(mid / i, n);

      if (cnt < k)
        start = mid + 1;
      else {
        end = mid - 1;
        ans = mid;
      }
    }

    System.out.println(ans);
  }
}