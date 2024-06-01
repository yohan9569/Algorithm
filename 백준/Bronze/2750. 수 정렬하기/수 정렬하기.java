import java.util.*;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), arr[] = new int[n];
        for (int i=0; i<n; arr[i++]=sc.nextInt());
        
        for (int i=0; i<n; i++) {
            int cnt = 0;
            for (int j=0; j<n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    int tmp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = tmp;
                    cnt++;
                }
            }
            if (cnt==0) break;
        }
        
        for (int e:arr) {
            System.out.println(e);
        }
    }
}