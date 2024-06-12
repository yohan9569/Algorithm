// DFS Algorithm
import java.io.*;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main {
	static ArrayList<Integer>[] A;
	static boolean[] visited;
	
	public static void main(String[] args) throws IOException {
		var br = new BufferedReader(new InputStreamReader(System.in));
		var st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
		
		visited = new boolean[n+1];
		A = new ArrayList[n+1];
		for (int i=1; i<=n; i++) A[i] = new ArrayList<Integer>();
		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken());
			A[s].add(e); A[e].add(s);
		}
		
		// dfs
		int cnt = 0;
		for (int i=1; i<=n; i++) {
			if (!visited[i]) {
				cnt++;
				DFS(i);
			}
		}
		
		System.out.println(cnt);
	}

	private static void DFS(int i) {
		if (visited[i]) return;
		visited[i] = true;
		for (int e:A[i]) DFS(e);
	}
}