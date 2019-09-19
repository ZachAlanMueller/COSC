import java.util.Scanner;
import java.lang.Math;

public class Rectangle {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter side: ");
        int x = sc.nextInt();
        System.out.printf("Please enter side: ");
        int y = sc.nextInt();
        
       	System.out.print("Rectangle area: "+x*y+"\n");
    }
}