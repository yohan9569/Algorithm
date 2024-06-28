// Binary Search
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    int[] a = new int[n];
    
    int start = 0, end = 0; // max, sum
    for (int i = 0; i < n; i++) {
      a[i] = sc.nextInt();
      if (start < a[i]) start = a[i];
      end += a[i];
    }
    sc.close();

    // binary search
    while (start <= end) {
      int blu = (start + end) / 2;
      int sum =0, cnt = 0;
      // count blu-ray
      for (int i = 0; i < n; i++) {
        sum += a[i];
        if (sum > blu) { // Exceed
          cnt++;
          sum = a[i];
        }
      }
      if (sum != 0) cnt++;
      if (cnt > m) start = blu + 1;
      else end = blu - 1;
    }

    System.out.println(start); // start>end
  }
}