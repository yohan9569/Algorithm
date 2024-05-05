import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
        List<Integer> a = new ArrayList<>(), b = new ArrayList<>();
        
		for (int i=0; i<3; i++) {
		    int c = sc.nextInt(), d = sc.nextInt();
		    if (a.contains(c))
		        a.remove(Integer.valueOf(c));
		    else 
		        a.add(c);
		    if (b.contains(d))
		        b.remove(Integer.valueOf(d));
		    else
		        b.add(d);
		}

		System.out.print(a.get(0) + " " + b.get(0));
	}
}