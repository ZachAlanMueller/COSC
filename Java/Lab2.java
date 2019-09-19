//COSC 2341
//Lab 2
//Andres Seminario
package lab2;
import java.util.ArrayList; 
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Random;
// https://www.geeksforgeeks.org/randomly-select-items-from-a-list-in-java/
class Lab2 {

    public static void main(String[] args) {
    Lab2 obj = new Lab2();
    int[] g_Drawer;
    g_Drawer = new int[]{ 11,11,11,11,11,12,12,12,12,12,21,21,21,21,22,22,22,22,31,31,32,32 };
    int numberOfElements = g_Drawer.length;
    System.out.println(obj.getRandomElement(g_Drawer, numberOfElements));                 
    
    public int getRandomElement(List<Integer> list, int bound) { 
        // ThreadLocalRandom generate a int type number 
        return list.get(ThreadLocalRandom.current() .nextInt(list.size()) % bound);
    }
    Random r = new Random();
    int randomGlove = r.nextInt(g_Drawer.length);
        System.out.println("random glove:" + randomGlove);
    for (int i = 0; i < g_Drawer.length; i++) 
//      System.out.println("Glove number " + i +  " is: "+ g_Drawer[i]); 
    
    for (int empty = 0; empty < g_Drawer.length; ++empty){
        int[] g_picked = null;
        g_picked [empty] = g_Drawer [empty];
        System.out.println("Glove number " + empty +  " is: "+ g_picked[empty]);
        
        
//    System.out.println(g_Drawer[randomGlove]);
        
//    while (empty < 22){
//        gloves_Drawer[randomGlove]
    }

    
        
    
    }
    
}
