import java.util.Scanner;

public class Summation {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);

        System.out.printf("Please enter n: ");
    	int n = sc.nextInt();
    	int total = 0;
        for(int i = 0; i <= n; i++){
        	total += i;
        }
    	System.out.printf("Summation: " + total + "\n");    	
    }
}