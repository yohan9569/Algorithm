import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String jh = sc.next();
    String dr = sc.next();
    String answer = jh.length() >= dr.length() ? "go" : "no";
    System.out.println(answer);
  }
}