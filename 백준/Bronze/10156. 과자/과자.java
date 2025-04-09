import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int k = sc.nextInt(), n = sc.nextInt(), m = sc.nextInt(), more = k * n - m;
    System.out.println(more > 0 ? more : 0);
  }
}