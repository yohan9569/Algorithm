import java.util.*;
class Main {
  public static void main(String[] args) {
    var sc = new Scanner(System.in);
    int n = sc.nextInt();
    String longs = "";
    for (int i=0; i<n/4; i++) longs += "long ";
    System.out.print(longs + "int");
  }
}