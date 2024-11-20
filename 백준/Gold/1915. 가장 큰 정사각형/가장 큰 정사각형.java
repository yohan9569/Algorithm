// DP

import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    char[][] grid;
    int[][] dp;

    int n = sc.nextInt(), m = sc.nextInt();
    grid = new char[n+1][m+1];
    for (int i = 1; i <=n; i++) {
      String line = sc.next();
      for (int j=1; j <= m; j++) {
        grid[i][j] = line.charAt(j-1);
      }
    }

    int ans = 0;
    dp = new int[n+1][m+1];
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if(grid[i][j]=='1') {
          int cell = Math.min(dp[i-1][j-1], Math.min(dp[i][j-1], dp[i-1][j])) + 1;
          dp[i][j] = cell;
          if (ans < cell) ans = cell;
        }
      }
    }

    System.out.println(ans*ans);
  }
}