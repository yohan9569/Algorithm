import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
    static int[][] grid;
    static ArrayList<int[]> zeros;
    static boolean[][] rowUsed, colUsed, boxUsed;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력
        grid = new int[9][9];
        zeros = new ArrayList<>();
        rowUsed = new boolean[9][10];
        colUsed = new boolean[9][10];
        boxUsed = new boolean[9][10];

        for (int i = 0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
                if (grid[i][j] == 0) {
                    zeros.add(new int[] { i, j });
                } else {
                    int num = grid[i][j];
                    rowUsed[i][num] = true;
                    colUsed[j][num] = true;
                    boxUsed[getBoxIndex(i, j)][num] = true;
                }
            }
        }

        // dfs
        if (dfs(0)) {
            // 출력
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(grid[i][j]).append(" ");
                }
                sb.append("\n");
            }
            System.out.println(sb);
        }
    }

    static boolean dfs(int d) {
        if (d == zeros.size())
            return true;

        int r = zeros.get(d)[0], c = zeros.get(d)[1];
        int boxIdx = getBoxIndex(r, c);

        for (int i = 1; i <= 9; i++) {
            if (!rowUsed[r][i] && !colUsed[c][i] && !boxUsed[boxIdx][i]) {
                // 숫자 배치
                grid[r][c] = i;
                rowUsed[r][i] = true;
                colUsed[c][i] = true;
                boxUsed[boxIdx][i] = true;

                // 다음 depth
                if (dfs(d + 1))
                    return true;

                // 백트래킹
                grid[r][c] = 0;
                rowUsed[r][i] = false;
                colUsed[c][i] = false;
                boxUsed[boxIdx][i] = false;
            }
        }
        return false;
    }

    static int getBoxIndex(int r, int c) {
        return (r / 3) * 3 + (c / 3);
    }
}