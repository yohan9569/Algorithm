import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt();
    while (a != 0) {
      String ans;

      if (a % b == 0)
        ans = "multiple";
      else if (b % a == 0)
        ans = "factor";
      else
        ans = "neither";
      System.out.println(ans);

      a = sc.nextInt();
      b = sc.nextInt();
    }
  }
}