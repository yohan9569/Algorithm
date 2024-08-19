// UnionFind Algorithm

import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    ArrayList<ArrayList<Integer>> A = new ArrayList<ArrayList<Integer>>();
    for (int i = 0; i <= n; i++) { // 왜 1부터 하면 안 될까? 
      A.add(new ArrayList<Integer>());
    }
    int[] indegree = new int[n + 1];

    for (int i = 0; i < m; i++) {
      int s = sc.nextInt(), e = sc.nextInt();
      A.get(s).add(e);
      indegree[e]++;
    }

    // 위상 정렬 수행
    Queue<Integer> q = new LinkedList<Integer>();
    for (int i = 1; i <= n; i++) {
      if (indegree[i] == 0)
        q.offer(i);
    }
    while (!q.isEmpty()) {
      int now = q.poll();
      System.out.print(now + " ");
      for (int next : A.get(now)) {
        indegree[next]--;
        if (indegree[next] == 0)
          q.offer(next);
      }
    }
  }
}