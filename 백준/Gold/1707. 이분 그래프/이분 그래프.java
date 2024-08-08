import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
  static ArrayList<Integer>[] A;
  static int[] check;
  static boolean[] visited;
  static boolean isEven;

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int testCase = Integer.parseInt(br.readLine());
    for (int t = 0; t < testCase; t++) {
      String[] s = br.readLine().split(" ");
      int v = Integer.parseInt(s[0]), e = Integer.parseInt(s[1]);

      A = new ArrayList[v + 1];
      check = new int[v + 1];
      visited = new boolean[v + 1];
      isEven = true;
      for (int i = 1; i <= v; i++)
        A[i] = new ArrayList<Integer>();
      for (int i = 0; i < e; i++) {
        s = br.readLine().split(" ");
        int start = Integer.parseInt(s[0]), end = Integer.parseInt(s[1]);
        A[start].add(end);
        A[end].add(start);
      }

      for (int i = 1; i <= v; i++) {
        if (isEven)
          DFS(i);
        else
          break;
      }

      if (isEven)
        System.out.println("YES");
      else
        System.out.println("NO");
    }
  }

  static void DFS(int start) {
    visited[start] = true;
    for (int i : A[start]) {
      if (!visited[i]) {
        check[i] = check[start] == 0 ? 1 : 0;
        DFS(i);
      } else if (check[i] == check[start])
        isEven = false;
    }
  }
}