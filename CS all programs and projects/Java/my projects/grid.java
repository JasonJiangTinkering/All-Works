import javax.swing.*;
import java.awt.*;


public class grid{

  public static void main(String[] args){
JFrame myFrame = new JFrame();

  myFrame.setTitle("myFirstFrame");
  myFrame.setSize(300, 200);
  myFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  myFrame.setVisible(true);
  JPanel myPanel = new JPanel();
  myPanel.setBackground(Color.pink);
  JPanel myLeft = new JPanel();
  myLeft.setBackground(Color.blue);
  JPanel myRight = new JPanel();
  myRight.setBackground(Color.red);
  JPanel myBottom = new JPanel();
  myBottom.setBackground(Color.cyan);
  JPanel myTop = new JPanel();
  myTop.setBackground(Color.green);



  Container pane = myFrame.getContentPane();
  pane.setLayout(new GridLayout(2,3));
  pane.add(myPanel);
  pane.add(myBottom);
  pane.add(myLeft);

  pane.add(myTop);
  pane.add(myRight);
  myPanel.setVisible(true);




  }


}
