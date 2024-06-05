import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        String[] arr = new String[5];
        for (int i=0; i<5; i++) arr[i] = sc.next();
        for (int i=0; i<15; i++) {
            for (String e:arr) {
                if (i<e.length()) System.out.print(e.charAt(i));
            }
        }
    }
}