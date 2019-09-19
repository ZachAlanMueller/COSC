import java.util.Scanner;

public class Adder {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        int n = 1;
        int total = 0;
        while(n != 0){
            System.out.printf("Please enter number to add: ");
            n = sc.nextInt();
            total+=n;
        }
    	System.out.printf("Summation: " + total + "\n");    	
    }
}