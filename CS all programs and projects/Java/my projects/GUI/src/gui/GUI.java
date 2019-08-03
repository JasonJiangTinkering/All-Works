/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author jason
 */
package gui;
import javax.swing.*;
import java.awt.*;
import javax.swing.JFrame;

public class GUI {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        JFrame myFrame = new JFrame();
        myFrame.setTitle("SetTitle");
        myFrame.setSize(300,200);
        myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ColorPanel panel = new ColorPanel(Color.red);
        Container pane = myFrame.getContentPane();
        pane.add(panel);
        myFrame.setVisible(true);
        
    }
    
}
