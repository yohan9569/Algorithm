import java.util.*;

public class Main {
    static Map<Integer, int[]> dict = new HashMap<Integer, int[]>() {{
        put(0, new int[] {10});
        put(1, new int[] {1});
        put(2, new int[] {6, 2, 4, 8});
        put(3, new int[] {1, 3, 9, 7});
        put(4, new int[] {6, 4});
        put(5, new int[] {5});
        put(6, new int[] {6});
        put(7, new int[] {1, 7, 9, 3});
        put(8, new int[] {6, 8, 4, 2});
        put(9, new int[] {1, 9});
    }};
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        for (int i=0; i<T; i++) {
            int a = sc.nextInt() % 10, b = sc.nextInt();
            int[] curDict = dict.get(a);
            int ans = curDict[b % curDict.length];
            System.out.println(ans);
        }
    }
}