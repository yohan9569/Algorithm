// Merge Sort Algorithm
import java.io.*;
import java.util.StringTokenizer;

class Main {
	public static int[] A, tmp;
	public static long result;
	
	public static void main(String[] args) throws IOException {
		var br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		var st = new StringTokenizer(br.readLine());
		br.close();
		
		A = new int[n];
		tmp = new int[n];
		for (int i=0; i<n; i++) A[i] = Integer.parseInt(st.nextToken());
		
		result = 0;
		mergeSort(0, n-1);
		System.out.println(result);
	}
	
	public static void mergeSort(int s, int e) {
		if (e-s < 1) return;
		
		int m = (e+s) / 2;
		// recursive
		mergeSort(s, m);
		mergeSort(m+1, e);
		
		for (int i=s; i<=e; i++) tmp[i] = A[i];
		int k = s, idx1 = s, idx2 = m+1;
		// logic for merging with sorting
		while (idx1<=m && idx2<=e) {
			if (tmp[idx1] > tmp[idx2]) {
				A[k++] = tmp[idx2++];
				result += (idx2-k); // overtaking
			}
			else A[k++] = tmp[idx1++];
		}
		// remaining elements
		while (idx1 <= m) A[k++] = tmp[idx1++];
		while (idx2 <= e) A[k++] = tmp[idx2++];
	}
}