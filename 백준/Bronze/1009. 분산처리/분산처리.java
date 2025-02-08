import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] twoNums = {6, 2, 4, 8}, threeNums = {1, 3, 9, 7}, sevenNums = {1, 7, 9, 3}, eightNums = {6, 8, 4, 2};
        
        for (int i=0; i<T; i++) {
            int a = sc.nextInt() % 10, b = sc.nextInt(), ans = a;
            switch (a) {
                case 0: ans = 10;
                    break;
                case 1: case 5: case 6: ans = a;
                    break;
                case 4: case 9:
                    ans = (b%2==0) ? (a*a) % 10 : a;
                    break;
                case 2: case 8:
                    ans = (a == 2 ? twoNums : eightNums)[b%4];
                    break;
                case 3: case 7:
                    ans = (a == 3 ? threeNums : sevenNums)[b%4];
                    break;
            }
            System.out.println(ans);
        }
    }
}