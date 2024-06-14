// DFS Algorithm
import java.util.*;

class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int n = sc.nextInt(), singles[] = {2,3,5,7};
		for (int s: singles) DFS(s, n);
	}

	static void DFS(int prime, int n) {
		int v = prime/(int)Math.pow(10, n-1);
		if (v>0 && v<9) System.out.println(prime);
		for (int i=1; i<10; i++) {
			int tmp = prime * 10 + i;
			if (isPrime(tmp)) DFS(tmp, n);
		}
	}
	
	static boolean isPrime(int x) {
		for (int i=2; i*i<=x; i++) {
			if (x%i == 0) return false;
		}
		return true;
	}
}