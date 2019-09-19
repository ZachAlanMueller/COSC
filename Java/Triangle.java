import java.util.Scanner;
import java.lang.Math;

public class Triangle {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter side x: ");
        int x = sc.nextInt();
        System.out.printf("Please enter side y: ");
        int y = sc.nextInt();
            
    	System.out.printf("Side Z is: " + (Math.sqrt(x*x+y*y)) + "\n");    	
    }
}