import java.util.*;
public class Main {
	public static void main(String[] args) {
		var s=new Scanner(System.in);
		int n=s.nextInt(),m=s.nextInt();
		int arr[][]=new int[n][m];
		for(int k=0;k<2;k++)
			for(int i=0;i<n;i++) {
				for(int j=0;j<m;j++) {
					arr[i][j]+=s.nextInt();
					if (k==1)
    					System.out.print(arr[i][j]+" ");
				}
    			if (k==1)
    			    System.out.println();
		    }
	}
}