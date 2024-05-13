import java.util.*;

public class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt(), end = 0, s = 0, cnt = 0, tmp;
		int[] arr = new int[N+1];
		
		for (int i=1; i<=N; i++)
			arr[i] = s += i;
			
		for (int start=0; start<N; start++) {
			while (arr[end] - arr[start] < N && end < N) end++;
			if (arr[end] - arr[start] == N) cnt++;
		}
		System.out.println(cnt);
	}
}