import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		int n = sc.nextInt(), ans = 0, i = n - ("" + n).length() * 9;
		sc.close();

		for (; i<n; i++) {
			int tmp = i, sum = i;
			for (; tmp > 0; sum += tmp % 10, tmp /= 10);
			if (n==sum) {
			    ans = i;
			    break;
			}
		}

		System.out.println(ans);
	}
}