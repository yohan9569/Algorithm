import java.util.*;

public class Main {
	public static void main(String[] args) {
		var sc = new Scanner(System.in);
		var str = sc.nextLine(); sc.close();
		var arr = Arrays.stream(str.split(" ")).mapToInt(Integer::parseInt).toArray();
		Integer a=arr[0], b=arr[1], c=arr[2], d=arr[3], e=arr[4], f=arr[5],
				x=(c*e-b*f)/(a*e-b*d), y=(a*f-d*c)/(a*e-b*d);
		
		System.out.println(x + " " + y);
	}
}