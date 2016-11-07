import javax.swing.JOptionPane;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.utils.ArrayList;

class graphics{
	class draw_object{
		int x1;
		int y1;
		int x2;
		int y2;
		boolean filled;
		int r1;
		public create_line

		String drawing_type;
		public draw_object(String type){
			switch type{
				case "line":
					drawing_type = "line";
					break;
				default:
					System.out.println("[" + type + "] is not an accepted drawing type.")
			}
		}
	}
	class Display extends JFrame{
		ArrayList<ArrayList> renderList = new ArrayList<ArrayList>();
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
	public static void main(String[] args){
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
