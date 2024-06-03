// Selection Sort Algorithm
import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        String s = sc.next();
        int[] arr = new int[s.length()];
        for (int i=0; i<s.length(); i++) 
            arr[i] = Integer.parseInt(s.substring(i, i+1));
        
        // Selection Sort
        for (int i=0; i<s.length()-1; i++) {
            int max_idx = i; // not element, for swap
            for (int j=i; j<s.length(); j++) {
                if (arr[max_idx] < arr[j]) max_idx = j;
            }
            if (i!=max_idx) {
                int tmp = arr[i];
                arr[i] = arr[max_idx];
                arr[max_idx] = tmp;
            }
        }
        
        for (int e:arr) System.out.print(e);
    }
}