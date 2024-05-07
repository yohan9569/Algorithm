import java.util.*;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(); //remains just after it.
        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = sc.nextInt();
        }
        
        int ans = 0;
        for (int i=0; i<N; i++) {
            for (int j=i+1; j<N; j++) {
                for (int k=j+1; k<N; k++) {
                    int sum = arr[i] + arr[j] + arr[k];
                    if (sum>ans && sum<=M) ans=sum;
                }
            }
        }
        System.out.print(ans);
    }
}