import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        int N = sc.nextInt();

        for (int i=0; i<N; q.add(++i));

        while (q.size()>1) {
        	q.poll();
        	q.add(q.poll());
        }

        for (int e : q) System.out.print(e + " ");
    }
}