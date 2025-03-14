import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), i = 1;

    for (; i<n; i++) System.out.println("*".repeat(i));
    for (; i>0; i--) System.out.println("*".repeat(i));
  }
}