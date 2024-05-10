import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int N = sc.nextInt(), M = sc.nextInt();
		var change = new ArrayList<Integer>();
		String[] chess = new String[N];
		
		sc.nextLine();
		for (int i=0; i<N; i++) {
		    chess[i] = sc.nextLine();
		}
		sc.close();
		
		for (int i=0; i<N-7; i++) {
		    for (int j=0; j<M-7; j++) {
		        check(chess, change, i, j);
		    }
		}
		System.out.println(Collections.min(change));
	}
	
	
	static void check(String[] chess, ArrayList<Integer> change, int a, int b) {
		int bw = 0, wb = 0;
		for (int i=a; i<a+8; i++) {
			for (int j=b; j<b+8; j++) {
				if ((i%2==0 && j%2==0)||(i%2==1 && j%2==1)) {
					if (chess[i].charAt(j)=='W') bw++;
					else wb++;
				} else {
					if (chess[i].charAt(j)=='B') bw++;
					else wb++;
				}
			}
		}
		change.add(bw);
		change.add(wb); // call by address
	}
}