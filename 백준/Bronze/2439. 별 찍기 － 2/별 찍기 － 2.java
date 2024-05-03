import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		// input
		var sc = new Scanner(System.in);
		int n = Integer.valueOf(sc.next());

		// print line by line
		for (int i = 0; i < n; i++) {
			// whitespace
			for (int j = 1; j < n-i; j++) {
				System.out.print(' ');
			}
			// star
			for (int j = n-i; j <= n; j++) {
				System.out.print('*');
			}
			// new line
			System.out.println();
		}
	}
}