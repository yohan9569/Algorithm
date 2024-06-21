// BFS Algorithm
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	static ArrayList<int[]>[] A;
	static boolean[] visited;
	static int[] distance;
	static int max;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		A = new ArrayList[n+1];
		for (int i=1; i<=n; i++) {
			A[i] = new ArrayList<int[]>();
		}
		for (int i=1; i<=n; i++) {
			int s = sc.nextInt();
			while (true) {
				int e = sc.nextInt();
				if (e==-1) break;
				int v = sc.nextInt();
				A[s].add(new int[] {e,v}); // 입력이 어차피 양방향으로 들어옴.
			}
		}
		distance = new int[n+1];
		visited = new boolean[n+1];
		max = 0;
		BFS(1);
		
		distance = new int[n+1];
		visited = new boolean[n+1];
		BFS(max);
		
		System.out.print(distance[max]);
	}
	
	static void BFS(int i) {
		Queue<Integer> q = new LinkedList<>();
		q.add(i);
		visited[i] = true;
		while (!q.isEmpty()) {
			int now = q.poll();
			for (int[] node : A[now]) {
				int e = node[0];
				int v = node[1];
				if (!visited[e]) {
					visited[e] = true;
					q.add(e);
					distance[e] = distance[now] + v;
					if (distance[max] < distance[e]) max = e;
				}
			}
		}
	}
}