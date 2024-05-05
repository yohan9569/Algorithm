import java.util.Scanner;
import java.util.HashSet; 

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        
        for (int i = 0; i < n; i++) {
            var set = new HashSet<Character>();
            var str = sc.next();
            char last = 'a';
            var flag = true;
            for (char e : str.toCharArray()) {
                if (set.contains(e) && last != e) {
                    flag = false;
                    break;
                }
                set.add(e);
                last = e;
            }
            if (flag)
                cnt += 1;
        }
        
        System.out.println(cnt);
    }
}