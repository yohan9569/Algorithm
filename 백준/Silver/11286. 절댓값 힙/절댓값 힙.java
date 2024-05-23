import java.util.*;

public class Main {
    public static void main(String[] args){
    	// 선언
        Scanner sc = new Scanner(System.in);
        PriorityQueue<Integer> q = new PriorityQueue<>((o1, o2)->{
        	int first = Math.abs(o1), second = Math.abs(o2);
        	if (first==second) return o1-o2;
        	else return first-second;
        });
        int N = sc.nextInt();
        // for 입력받고 처리
        for (int i=0; i<N; i++) {
        	int x = sc.nextInt();
        	// case 0
        	if (x==0) {
        		if (q.isEmpty()) System.out.println(x);
        		else System.out.println(q.poll());
        	} else {
        		q.add(x);
        	}	
        }
    }
}