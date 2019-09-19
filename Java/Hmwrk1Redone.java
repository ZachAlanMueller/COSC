import java.util.Scanner;
import java.lang.Math;

public class Hmwrk1Redone {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter price of beer: ");
        double x = sc.nextDouble();
        System.out.printf("Please enter available money: ");
        double y = sc.nextDouble();
        double priceBeerTotal = x*1.1;
        priceBeerTotal *= 1.2;
        double answer = y/priceBeerTotal;
        answer = Math.floor(answer);
        System.out.printf("If a beer costs $%.2f, Johnny can have %d beers for $%.2f (he will pay $%.2f).", x, (int)answer, y, answer*priceBeerTotal);
    }
}