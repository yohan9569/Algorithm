import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    long ab = Long.parseLong(sc.next() + sc.next());
    long cd = Long.parseLong(sc.next() + sc.next());
    long answer = ab + cd;

    System.out.println(answer);
  }
}