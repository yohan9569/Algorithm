import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    long n = sc.nextLong();
    long m = sc.nextLong();
    long ans = n - m;
    if (ans < 0) ans = ans * -1;
    System.out.println(ans);
  }
}