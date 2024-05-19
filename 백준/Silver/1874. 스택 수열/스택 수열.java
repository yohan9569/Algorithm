import java.util.*;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), arr[] = new int[n], next = 1;
        for (int i=0; i<n; arr[i++]=sc.nextInt());
        var stack = new Stack<Integer>();
        var ans = new StringBuffer();

        for (int i=0; i<arr.length; i++) {
            int elem = arr[i];

            while (next <= elem) {
                stack.push(next++);
                ans.append("+\n");
            }
            int top = stack.pop();
            if (top == elem) ans.append("-\n");
            else {
                System.out.print("NO");
                return;
            }
        }

        System.out.print(ans.toString());
    }
}