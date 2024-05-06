import java.util.*;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt();
        int ans = 0;
        
        while (n-- > 0) {
            int x = sc.nextInt();
            int cnt = 0;
            
            if (x==1) continue;
            for (int i=1; i*i <= x; i++) {
                if (x%i == 0) cnt++;
            }

            if (cnt==1) ans += 1;
        }

        System.out.print(ans);
    }
}