import java.util.Scanner;
import java.math.BigDecimal;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    BigDecimal a = new BigDecimal(sc.next());
    BigDecimal b = new BigDecimal(sc.next());
    sc.close();

    System.out.println(a.add(b));
    System.out.println(a.subtract(b));
    System.out.println(a.multiply(b));
  }
}