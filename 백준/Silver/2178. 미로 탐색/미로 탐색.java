// BFS Algorithm
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Main {
	static int[] dx = {0,0,-1,1};
	static int[] dy = {1,-1,0,0};
	static int[][] A;
	static int n, m;
	
	public static void main(String[] args) {
		// input
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt(); m = sc.nextInt();
		A = new int[n][m];
		for (int i=0; i<n; i++) {
			String line = sc.next();
			for (int j=0; j<m; j++) {
				A[i][j] = Integer.parseInt(line.substring(j, j+1));
			}
		}
		// bfs
		BFS(0,0);
		// output
		System.out.println(A[n-1][m-1]);
	}

	static void BFS(int i, int j) {
		Queue<int[]> q = new LinkedList<>();
		q.offer(new int[] {i,j});
		while (!q.isEmpty()) {
			int[] now = q.poll();
			// 상하좌우
			for (int k=0; k<4; k++) {
				int x = now[0] + dx[k], y = now[1] + dy[k];
				if (x>=0 && y>=0 && x<n && y<m && !(x==0&&y==0)) { // 좌표 유효성
					if (A[x][y]==1) {
						A[x][y] = A[now[0]][now[1]] + 1;
						q.add(new int[] {x,y});
					}
				}
			}
		}
	}
}