import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        sc.close();

        long code1Count = (n * (n - 1)) / 2;
        System.out.println(code1Count);
        System.out.println(2);
    }
}