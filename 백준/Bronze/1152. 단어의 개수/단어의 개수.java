import java.util.Scanner;
import java.util.StringTokenizer;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        // String[] arr = sc.nextLine().split(" "); // input " " -> 1
        var s = sc.nextLine();
        var st = new StringTokenizer(s, " ");
        System.out.print(st.countTokens());
    }
}