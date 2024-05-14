import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(), cnt = 0;
        int[] arr = new int[N];
        
        for (int i=0; i<N; i++) {
        	arr[i] = sc.nextInt();
        }
        
        for (int j=0; j<N-1; j++) {
        	for (int k=j+1; k<N; k++) {
        		if (arr[j] + arr[k] == M) cnt++;
        	}
        }
        
        System.out.println(cnt);
    }
}