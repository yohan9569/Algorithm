import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int N = sc.nextInt();
		int s = 0, m = 0, tmp;
		for (int i=0; i<N; i++) {
			tmp = sc.nextInt();
			if (m < tmp) m = tmp;
			s += tmp;
		}
		System.out.print(s*100.0/m/N);
	}
}