/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cipher;

/**
 *
 * @author jason
 */
import java.util.Scanner;
import java.lang.String;

public class Cipher{


        public static void main(String[] args) {


        Scanner myObj = new Scanner(System.in);
        System.out.println("hello world");

        System.out.println("Enter email");

            int move = myObj.nextInt();
            String email = myObj.nextLine();
            String myFinal = "This is your email:";
            char[] myList = email.toCharArray();

            for(char y = 1; y < myList.length; y++){
               int z = Character.getNumericValue(myList[y]);
              int p = 6;
               if(z == p){
                myFinal = myFinal + " ";

               }
               else{
                 z = z + move + 55;
                  System.out.println(z);
                  String t = Character.toString((char)z);
                  System.out.println(t);
                  myFinal = myFinal + t;

               }


}

            System.out.print(myFinal);

}
}

