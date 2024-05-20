import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(), arr[] = new int[N];
        
        for (int i=0; i<M; i++) {
        	int a = sc.nextInt()-1, b = sc.nextInt(), c = sc.nextInt();
        	Arrays.fill(arr, a, b, c);
        }
        
        for (int e : arr) System.out.print(e + " ");
    }
}