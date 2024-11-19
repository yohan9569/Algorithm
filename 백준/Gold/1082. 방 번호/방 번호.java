// Greedy
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    TreeMap<Integer, Integer> map = new TreeMap<>(); // 가격 별 최고 수

    // 입력
    int n = sc.nextInt();

    for (int i = 0; i < n; i++) {
      int p = sc.nextInt();
      map.put(p, i);
    }

    int m = sc.nextInt();

    // 최대 자리수로 숫자 구성
    int cheapestPrice = map.firstKey();
    int cheapestNum = map.get(cheapestPrice);

    int nextPrice, nextNum;
    if (cheapestNum == 0 && map.size() > 1) {
      nextPrice = map.higherKey(cheapestPrice);
      nextNum = map.get(nextPrice);
    } else {
      nextPrice = cheapestPrice;
      nextNum = cheapestNum;
    }

    StringBuilder number = new StringBuilder();
    if (m >= nextPrice) {
      m -= nextPrice;
      number.append(nextNum);
    }
    while (m >= cheapestPrice) {
      m -= cheapestPrice;
      number.append(cheapestNum);
    }

    // 중간 점검
    if (number.charAt(0) == '0') {
      System.out.println(0);
      return;
    }
    if (m == 0) {
      System.out.println(number);
      return;
    }

    // 업그레이드
    char[] digits = number.toString().toCharArray();
    for (int i = 0; i < digits.length; i++) {
      int currentDigit = digits[i] - '0';

      for (Map.Entry<Integer, Integer> entry : map.descendingMap().entrySet()) {
        int price = entry.getKey();
        int num = entry.getValue();

        if (num > currentDigit && m >= price - (i == 0 ? nextPrice : cheapestPrice)) {
          m -= (price - (i == 0 ? nextPrice : cheapestPrice)); // 추가 비용 지불
          digits[i] = (char) ('0' + num); // 숫자 업그레이드
          break;
        }
      }
    }

    // 결과 출력
    System.out.println(new String(digits));
  }
}