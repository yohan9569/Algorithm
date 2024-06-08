// Merge Sort Algorithm
import java.io.*;

class Main {
	public static int[] A, tmp;
	public static long result;
	
	public static void main(String[] args) throws IOException {
		var br = new BufferedReader(new InputStreamReader(System.in));
		var bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		A = new int[n];
		tmp = new int[n];
		for (int i=0; i<n; i++) A[i] = Integer.parseInt(br.readLine());
		br.close();
		
		mergeSort(0, n-1);
		for (int i=0; i<n; i++) bw.write(A[i] + "\n");
		bw.flush();
		bw.close();
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
			if (tmp[idx1] > tmp[idx2]) A[k++] = tmp[idx2++];
			else A[k++] = tmp[idx1++];
		}
		// remaining elements
		while (idx1 <= m) A[k++] = tmp[idx1++];
		while (idx2 <= e) A[k++] = tmp[idx2++];
	}
}