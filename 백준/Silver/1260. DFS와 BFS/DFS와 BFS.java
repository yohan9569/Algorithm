// DFS & BFS Algorithm
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	static boolean[] visited;
	static ArrayList<Integer>[] A;
	
	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt(), m = sc.nextInt(), v = sc.nextInt();
		A = new ArrayList[n+1];
		for (int i=1; i<=n; i++) {
			A[i] = new ArrayList<Integer>();
		}
		for (int i=0; i<m; i++) {
			int a = sc.nextInt(), b = sc.nextInt();
			A[a].add(b); A[b].add(a);
		}
		// sort
		for (int i=1; i<=n; i++) {
			Collections.sort(A[i]);
		}
		
		// dfs
		visited = new boolean[n+1];
		DFS(v);
		System.out.println();
		// bfs
		visited = new boolean[n+1];
		BFS(v);
		
	}

	static void DFS(int i) {
		if (visited[i]) return;
		visited[i] = true;
		System.out.print(i + " ");
		for (int j : A[i]) DFS(j);
	}
	
	static void BFS(int i) {
		Queue<Integer> q = new LinkedList<>();
		q.add(i);
		while (!q.isEmpty()) {
			int now = q.poll();
			if (!visited[now]) {
				visited[now] = true;
				System.out.print(now + " ");
				for (int j : A[now]) {
					q.add(j);
				}
			}
		}
	}
}