import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int N = sc.nextInt(), M = sc.nextInt(), s = 0;
		int[] arr = new int[N];
		int[] S = new int[N];
		
		for (int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
			S[i] = s += arr[i];
		}
		
		while (M-->0) {
			int j = sc.nextInt()-2, k = sc.nextInt()-1;
			System.out.println(j>=0? S[k] - S[j] : S[k]);
		}
		
	}
}