import java.util.Scanner;
import java.lang.Math;

public class Average {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter how many numbers: ");
        int n = sc.nextInt();
        int total = 0;
        for(int i = 0; i < n; i++){
        	System.out.printf("Please enter grade: ");
        	int y = sc.nextInt();
        	total += y;
        }
        System.out.printf("Average: " + (total/n) + "\n");
    }
}