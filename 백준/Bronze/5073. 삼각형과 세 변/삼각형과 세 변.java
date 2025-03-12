import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
    int maxNum = Math.max(a, Math.max(b, c));
    String answer;

    while (!(a == 0 && b == 0 && c == 0)) {
      if (a + b + c <= maxNum * 2) answer = "Invalid";
      else if (a == b && b == c) answer = "Equilateral";
      else if (a != b && b != c && a != c) answer = "Scalene";
      else answer = "Isosceles";
      System.out.println(answer);
      a = sc.nextInt(); b = sc.nextInt(); c = sc.nextInt();
      maxNum = Math.max(a, Math.max(b, c));
    }
  }
}