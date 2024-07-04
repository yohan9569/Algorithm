// Greedy Alogrithm
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String input = sc.nextLine();
    String[] s = input.split("-");
    sc.close();

    int ans = 0;
    for (int i = 0; i < s.length; i++) {
      String[] t = s[i].split("\\+");
      int sum = 0;
      for (int j = 0; j < t.length; j++) {
        sum += Integer.parseInt(t[j]);
      }
      if (i == 0)
        ans += sum;
      else
        ans -= sum;
    }

    System.out.println(ans);
  }
}