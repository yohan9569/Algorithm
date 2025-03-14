import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      System.out.println(" ".repeat(i) + "*".repeat(2 * n - 2 * i - 1));
    }
  }
}