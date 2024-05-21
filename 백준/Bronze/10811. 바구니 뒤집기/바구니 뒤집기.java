import java.util.*;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(), M = sc.nextInt(), arr[] = IntStream.rangeClosed(1, N).toArray();
        
        for (int i=0; i<M; i++) {
        	int a = sc.nextInt()-1, b = sc.nextInt()-1;
            
        	while (a<b) {
        		int tmp = arr[a];
        		arr[a++] = arr[b];
        		arr[b--] = tmp;	
        	}
        }
        
        for (int e : arr) System.out.print(e + " ");
    }
}