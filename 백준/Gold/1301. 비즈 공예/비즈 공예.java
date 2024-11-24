import java.util.*;

public class Main {
    static HashMap<String, Long> dp = new HashMap<>();
    static int n, arr[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new int[5];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        long ans = dfs(5, 5, Arrays.toString(arr)); // 시작 상태를 문자열로 변환하여 저장
        System.out.println(ans);
    }

    static long dfs(int last, int next, String state) {
        // 구슬을 모두 사용한 경우
        if (Arrays.stream(arr).sum() == 0) return 1;

        // DP에 값이 있다면 반환
        String key = last + "," + next + "," + state;
        if (dp.containsKey(key)) return dp.get(key);

        long cnt = 0;
        for (int i = 0; i < n; i++) {
            if (arr[i] > 0 && i != last && i != next) {
                arr[i]--;
                cnt += dfs(i, last, Arrays.toString(arr)); // 현재 상태를 문자열로 저장
                arr[i]++;
            }
        }

        dp.put(key, cnt); // 결과를 DP에 저장
        return cnt;
    }
}