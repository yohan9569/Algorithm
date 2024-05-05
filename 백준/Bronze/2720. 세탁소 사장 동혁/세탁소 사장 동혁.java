import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int i=0; i<T; i++){
		    int C=sc.nextInt();
		    int[] arr = {0,0,0,0};
		    int[] divisors = {25,10,5,1};
		    
		    for (int j=0; j<4; j++) {
		        arr[j] += (int)C/divisors[j];
		        C %= divisors[j];
		        System.out.print(arr[j] + " ");
		    }
		    System.out.println();
		}
	}
}