// DFS Algorithm
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class Main {
    static List<List<Integer>> A;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());

        visited = new boolean[n];
        A = new ArrayList<>();
        for (int i=0; i<n; i++) A.add(new ArrayList<Integer>());
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken()), e = Integer.parseInt(st.nextToken());
            A.get(s).add(e);
            A.get(e).add(s);
        }

        // dfs
        int ans = 0;
        for (int i=0; i<n; i++) {
            if (!visited[i]) {
                ans = DFS(i, 1);
                if (ans==1) break;
            }
        }
        
        System.out.println(ans);
    }

    private static int DFS(int i, int d) {
        if (d==5) return 1;
        visited[i] = true;
        for (int e : A.get(i)) {
            if (!visited[e] && DFS(e, d + 1) == 1) {
                return 1;
            }
        }
        visited[i] = false;
        return 0;
    }
}