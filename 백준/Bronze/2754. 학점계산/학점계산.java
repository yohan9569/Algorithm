import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String grade = sc.next();
    double score = 0.0;

    if (grade.equals("F")) {
      System.out.println(score);
      return;
    }
    
    switch (grade.charAt(0)) {
      case 'A':
        score += 4;
        break;
      case 'B':
        score += 3;
        break;
      case 'C':
        score += 2;
        break;
      case 'D':
        score += 1;
        break;
    }

    switch (grade.charAt(1)) {
      case '+':
        score += 0.3;
        break;
      case '-':
        score -= 0.3;
        break;
    }

    System.out.println(score);
  }
}