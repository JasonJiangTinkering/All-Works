/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package gui;
import javax.swing.*;
import java.awt.*;
/**
 *
 * @author jason
 */
public class ColorPanel extends JPanel{
    
    public ColorPanel(Color mybackground){
        setBackground(mybackground);
    }
    public void paintComponent(Graphics g){
        super.paintComponent(g);
        int x = getWidth() / 2 - 60;
        int y = getHeight() / 2;
        g.setColor(Color.blue);
        g.drawRect(x,y,120, 20);
        Font myFont = new Font("Times New Roman", Font.ITALIC, 20);
        g.setFont(myFont);
        g.drawString("Hello World", x +10, y+15);
        
    }
}
