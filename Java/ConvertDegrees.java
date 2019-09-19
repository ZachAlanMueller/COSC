import java.util.Scanner;

public class ConvertDegrees {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);

        System.out.printf("Please enter degrees in F: ");
    	double input = sc.nextInt();
        input = (input-32) * 5/9;

    	System.out.printf("That is %.1f degrees in C!\n", input);    	
    }
}