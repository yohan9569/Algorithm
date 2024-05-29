import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), i = 0;
        for (; i<n; i++) {
            String s = sc.next();
            System.out.println(s.charAt(0) + s.substring(s.length()-1));
        }
    }
}