import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();

    if (N == 1) {
      System.out.println(0);
      return;
    }

    int maxX = -10000, minX = 10000, maxY = -10000, minY = 10000;
    for (int i = 0; i < N; i++) {
      int x = sc.nextInt(), y = sc.nextInt();
      if (maxX < x) maxX = x;
      if (minX > x) minX = x;
      if (maxY < y) maxY = y;
      if (minY > y) minY = y;
    }

    int answer = (maxX - minX) * (maxY - minY);

    System.out.println(answer);
  }
}