import java.util.*;
class Main {
  public static void main(String[] args) {
    var sc = new Scanner(System.in);
    int n = sc.nextInt() - sc.nextInt();
    String a = new String();
    if (n>0) a = ">";
    else if (n<0) a = "<";
    else a = "==";
    System.out.print(a);
  }
}