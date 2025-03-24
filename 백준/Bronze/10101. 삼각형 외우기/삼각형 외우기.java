import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt(), sum = a+b+c;
    String ans;
    if (sum == 180) {
      if (a==b && b==c) ans = "Equilateral";
      else if(a==b || b==c || a==c) ans = "Isosceles";
      else ans = "Scalene";
    } else {
      ans = "Error";
    }

    System.out.println(ans);
  }
}