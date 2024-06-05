import java.util.*;
class Main {
    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        double sum_point = 0, sum_credit = 0;
        Map<String, Double> map = Map.of(
        "A+",4.5, "A0",4.0, "B+",3.5, "B0",3.0, "C+",2.5, "C0",2.0, "D+",1.5, "D0",1.0, "F",0.0);
        
        for (int i=0; i<20; i++) {
            sc.next();
            Double credit = sc.nextDouble();
            String grade = sc.next();
            if (grade.equals("P")) continue;
            sum_credit += credit;
            sum_point += map.get(grade) * credit;
        }
        
        System.out.println(sum_point/sum_credit);
    }
}