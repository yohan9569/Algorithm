import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        sc.next();
        var s = sc.next();
        int t = 0;
        for (char e:s.toCharArray()) {
            t += Character.getNumericValue(e);
        }
        System.out.print(t);
    }
}