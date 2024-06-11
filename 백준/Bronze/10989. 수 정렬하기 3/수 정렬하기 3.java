// Radix Sort Algorithm
import java.io.*;
import java.util.StringTokenizer;

class Main {
	public static int[] A;
	public static long result;
	
	public static void main(String[] args) throws IOException {
		var br = new BufferedReader(new InputStreamReader(System.in));
		var bw= new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		
		// input
		A = new int[n];
		for (int i=0; i<n; i++) A[i] = Integer.parseInt(br.readLine());
		br.close();
		
		// sorting
		radixSort(A, 5);
		
		// output
		for (int i=0; i<n; i++) bw.write(A[i] + "\n");
		bw.flush();
		bw.close();
	}
	
	public static void radixSort(int[] A, int maxSize) {
		int[] output = new int[A.length];
		int place = 1, cnt = 0;
		
		while (cnt != maxSize) { 
			int[] bucket = new int[10];
			for (int i=0; i<A.length; i++) bucket[(A[i] / place) % 10]++;
			for (int i=1; i<10; i++) bucket[i] += bucket[i-1];
			for (int i=A.length-1; i>=0; i--) {
				output[bucket[(A[i] / place % 10)] -1] = A[i];
				bucket[(A[i] / place) % 10]--;
			}
			for (int i=0; i<A.length; i++) A[i] = output[i];
			place *= 10;
			cnt++;
		}
	}
}