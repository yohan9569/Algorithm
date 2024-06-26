// Binary Search
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine()); // input1
    int n = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine()); // input2
    int[] a = new int[n];
    for (int i = 0; i < n; i++)
      a[i] = Integer.parseInt(st.nextToken());
    Arrays.sort(a); // sort
    st = new StringTokenizer(br.readLine()); // input3
    int m = Integer.parseInt(st.nextToken());
    st = new StringTokenizer(br.readLine()); // input4
    // Binary Search
    for (int i = 0; i < m; i++) {
      int x = Integer.parseInt(st.nextToken());
      int start = 0, end = n - 1;
      boolean flag = false;
      while (start <= end) {
        int mid = (start + end) / 2;
        if (a[mid] < x)
          start = mid + 1;
        else if (a[mid] > x)
          end = mid - 1;
        else {
          flag = true;
          break;
        }
      }
      System.out.println(flag ? 1 : 0);
    }
  }
}