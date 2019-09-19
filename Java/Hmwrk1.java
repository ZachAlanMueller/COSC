import java.util.Scanner;
import java.lang.Math;

public class Hmwrk1 {
    public static void main(String args[]) {
    	Scanner sc = new Scanner(System.in);
        
        System.out.printf("Please enter price of beer: ");
        double x = sc.nextDouble();
        System.out.printf("Please enter available money: ");
        double y = sc.nextDouble();
        int currentBeers = 0;
        while(true){
            double nextBeerPrice = (((currentBeers+1)*x)*1.1) + ((((currentBeers+1)*x)*1.1) * .2);
            if(nextBeerPrice < y){
                currentBeers++;
            }
            else{
                nextBeerPrice = (((currentBeers)*x)*1.1) + ((((currentBeers)*x)*1.1) * .2);
                System.out.printf("If a beer costs $%.2f, Johnny can have %d beers for $%.2f (he will pay $%.2f).", x, currentBeers, y, nextBeerPrice);
                return;
            }
        }
    }
}