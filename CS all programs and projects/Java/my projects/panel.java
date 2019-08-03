import javax.swing.*;
import java.awt.*;


public class panel{

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
  pane.add(myPanel, BorderLayout.CENTER);
  pane.add(myBottom, BorderLayout.SOUTH);
  pane.add(myLeft, BorderLayout.WEST);

  pane.add(myTop, BorderLayout.NORTH);
  pane.add(myRight, BorderLayout.EAST);




  }


}
