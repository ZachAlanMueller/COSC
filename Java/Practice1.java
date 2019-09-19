import java.util.Scanner;

public class Practice1 {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);

        System.out.printf("Please enter your name: ");
    	String name = sc.nextLine();
    	System.out.println("Your name is " + name);
        //This is so damn easy

    	System.out.printf("Please enter your age: ");
    	int age = sc.nextInt();
        System.out.printf("Your age is %d%n", age);

    	
    }
}