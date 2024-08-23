// Combination Algorithm

import java.util.Scanner;

public class Main {
  static int N, K, D[][];
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    N = sc.nextInt();
    K = sc.nextInt();
    D = new int[11][11];
    // 초기화
    for (int i =0; i<=N; i++) {
      D[i][i] = 1;
      D[i][0] = 1;
      D[i][1] = i;
    }
    // 점화식으로 배열 완성
    for (int i=2; i<=N; i++){
      for (int j=1; j<i; j++) {
        D[i][j] = D[i-1][j] + D[i-1][j-1];
      }
    }
    System.out.println(D[N][K]);
  }
}