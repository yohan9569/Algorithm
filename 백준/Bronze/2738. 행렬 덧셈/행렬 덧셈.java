import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        int n = sc.nextInt(), m = sc.nextInt();
        
        //creating matrices
        int a[][] = new int[n][m], b[][] = new int[n][m], c[][] = new int[n][m];
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                a[i][j] = sc.nextInt();
            }
        }
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                b[i][j] = sc.nextInt();
            }
        }
        
        //adding and printing addition of 2 matrices
        for (int i=0; i<n; i++) {
            for (int j=0; j<m; j++) {
                c[i][j] = a[i][j] + b[i][j];
                System.out.print(c[i][j] + " ");
            }
            System.out.println();
        }
    }
}