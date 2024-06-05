import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), side = 3;
        for (int i=1; i<n; i++) side = side*2 -1;
        System.out.print(side*side);
    }
}