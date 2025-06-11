// 삼각형의 조건: 가장 긴 변의 길이가 나머지 두 변의 합보다 짧아야 한다.
// 1. 원본 합, 2. 작은 두 변의 합과 그보다 1작은 변의 합 중 작은 수를 출력한다.

import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
    int sumOrigin = a + b + c;
    int maxPole =  Math.max(Math.max(a, b), c);
    int sumAfter = (sumOrigin - maxPole) * 2 - 1;
    int answer = Math.min(sumOrigin, sumAfter);
    System.out.println(answer);
  }
}