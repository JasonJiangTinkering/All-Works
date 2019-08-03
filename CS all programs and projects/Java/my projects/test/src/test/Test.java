/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package test;
import javax.swing.JOptionPane;
/**
 *
 * @author jason
 */
public class Test {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        while(true){
            
       
        String inputStr = JOptionPane.showInputDialog("Enter the Radius, type -1 to exit", "" );
        
        if(inputStr == null){
            JOptionPane.showMessageDialog(null, "Error: Enter the Radius");
            continue;
           
        }
        double radius = Double.parseDouble(inputStr);
        if(radius == -1){
            break;
            
        }
        else if(radius < 0){
            JOptionPane.showMessageDialog(null, "Error: Radius must be Positive");
            continue;
        }
        double area = Math.PI * Math.pow(radius, 2);
        JOptionPane.showMessageDialog(null, "The area is:" + area);
        break;
            } 
    }
    
}
