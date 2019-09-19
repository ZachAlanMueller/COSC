import java.util.Scanner;
import java.lang.Math;

public class Divisors {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter side a number: ");
        int x = sc.nextInt();
        for(int i = 1; i <= x; i++){
        	if (x % i == 0){
        		System.out.print(i + " ");
        	}
       	}
       	System.out.print("\n");
    }
}