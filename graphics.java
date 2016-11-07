import javax.swing.JOptionPane;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.util.ArrayList;
import java.util.List;

class gui{
	class drawing{
		String draw_type;
		List build;
		public drawing(String type, List drawing_build){
			switch(type){
				case "line":
					draw_type = type;
					build = drawing_build;
					break;
				case "rect":
					draw_type = type;
					build = drawing_build;
					break;
				default:
					System.out.println("[" + type + "] is not an accepted draw type.");
			}
		}
	}
	class Display extends JFrame{
		List renderList = new ArrayList();
		public Display(){
			repaint();

		}
		public void refresh(){
			repaint();
		}
		public void paint(Graphics g){
			g.setColor(new Color(0,255,0));
			g.fillRect(0,0,200,100);
			//for()
		}
	}
	public void run(){
		//define Display parameters
		Display screen = new Display();
		screen.setTitle("Test");
		screen.setSize(640,480);
		screen.setBackground(Color.WHITE);
		screen.setVisible(true);
		screen.setDefaultCloseOperation(screen.EXIT_ON_CLOSE);
		//draw things
	}
}
class graphics{
	public static void main(String[] args){
		gui g = new gui();
		g.run()
	}
}
