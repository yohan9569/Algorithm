//Quik Sort Algorithm
import java.io.*;
import java.util.StringTokenizer;

class Main {
 public static void main(String[] args) throws IOException {
     var br = new BufferedReader(new InputStreamReader(System.in));
     var st = new StringTokenizer(br.readLine());
     int n = Integer.parseInt(st.nextToken());
     int k = Integer.parseInt(st.nextToken());
     
     int[] A = new int[n];
     st = new StringTokenizer(br.readLine());
     for (int i=0; i<n; i++) {
         A[i] = Integer.parseInt(st.nextToken());
     }
     
     quikSort(A, 0, n-1, k-1);
     System.out.println(A[k-1]);
 }
 
 public static void quikSort(int[] A, int start, int end, int k) {
     if (start<end) {
         int pivot = partition(A, start, end);
         if (pivot==k) return;
         else if (k<pivot) quikSort(A, start, pivot-1, k);
         else quikSort(A, pivot+1, end, k);
     }
 }
 
 public static int partition(int[] A, int start, int end){
     if (start+1 == end) {
         if (A[start] > A[end]) swap(A, start, end);
         return end;
     }
     int mid = (start + end) / 2;
     swap(A, start, mid);
     int pivot = A[start];
     int i = start + 1, j = end;
     while (i<=j) {
         while (pivot<A[j] && j>0) j--;
         while (pivot>A[i] && i<A.length-1) i++;
         if (i<=j) swap(A, i++, j--);
     }
     A[start] = A[j];
     A[j] = pivot;
     return j;
 }
 
 public static void swap(int[] A, int i, int j) {
     int temp = A[i];
     A[i] = A[j];
     A[j] = temp;
 }
}