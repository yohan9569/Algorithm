// UnionFind Algorithm

import java.util.Scanner;

public class Main {
  static int[] parent;

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    parent = new int[n + 1];
    // 초기화
    for (int i = 0; i <= n; i++)
      parent[i] = i;
    // 질의 계산
    for (int i = 0; i < m; i++) {
      int query = sc.nextInt();
      int a = sc.nextInt(), b = sc.nextInt();
      if (query == 0)
        union(a, b);
      else {
        boolean res = checkSame(a, b);
        if (res)
          System.out.println("YES");
        else
          System.out.println("NO");
      }
    }
  }

  static void union(int a, int b) {
    // 대표 노드 찾아서 연결
    a = find(a);
    b = find(b);
    if (a != b)
      parent[b] = a;
  }

  static int find(int a) { // 재귀
    if (a == parent[a])
      return a;
    else // 경로 압축
      return parent[a] = find(parent[a]);
  }

  static boolean checkSame(int a, int b) {
    a = find(a);
    b = find(b);
    if (a == b)
      return true;
    return false;
  }
}