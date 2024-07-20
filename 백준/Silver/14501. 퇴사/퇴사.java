// Dynamic Programming Alogrithm
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] t = new int[n + 1];
    int[] p = new int[n + 1];
    for (int i = 1; i <= n; i++) {
      t[i] = sc.nextInt();
      p[i] = sc.nextInt();
    }
    sc.close();

    int[] d = new int[n + 2];
    d[n+1] = 0;
    for (int i = n; i > 0; i--) {
      if (i + t[i]  >  n + 1)
        d[i] = d[i + 1];
      else
        d[i] = Math.max(d[i + 1], d[i + t[i]] + p[i]);
    }

    System.out.println(d[1]);
  }
}