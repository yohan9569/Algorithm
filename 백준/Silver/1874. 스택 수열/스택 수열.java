import java.util.*;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), arr[] = new int[n], next = 1;
        for (int i=0; i<n; arr[i++]=sc.nextInt());
        var stack = new Stack<Integer>();
        var ans = new StringBuffer();
        var flag = true;

        for (int i=0; i<arr.length; i++) {
            int elem = arr[i];
            
            if (next <= elem) {
                while (next <= elem) {
                    stack.push(next++);
                    ans.append("+\n");
                }
                stack.pop();
                ans.append("-\n");
            } else {
                int top = stack.pop();
                if (top == elem) ans.append("-\n");
                else {
                    System.out.print("NO");
                    flag = false;
                    break;
                }
            }
        }

        if (flag) System.out.print(ans.toString());
    }
}