import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(), cnt = 0, arr[] = new int[N];

        for (int i=0; i<N; i++) {
        	arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);

        int i = 0, j = N-1;
        while (i<j) {
		        if (arr[i] + arr[j] < M) i++;
		        else if (arr[i] + arr[j] > M) j--;
		        else {
				        cnt++; i++; j--;
		        }
        }

        System.out.print(cnt);
    }
}