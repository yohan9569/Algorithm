import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // input
        Scanner sc = new Scanner(System.in);
        Integer t1 = Integer.valueOf(sc.next());
        Integer t2 = Integer.valueOf(sc.next());
        
        // calc
        t2 -= 45;
        if (t2 < 0) {
            t1 -= 1;
            t2 += 60;
        }
        t1 = t1 < 0 ? t1 += 24 : t1;
        
        // print
        System.out.println(t1 + " " + t2);
    }
}