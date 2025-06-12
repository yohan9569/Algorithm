import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    final int N = sc.nextInt();
    int sumation = 0;
    for (int i = 0; i < N; i++) {
      sumation += sc.nextInt();
    }
    int answer = sumation - N + 1;
    System.out.println(answer);
  }
}