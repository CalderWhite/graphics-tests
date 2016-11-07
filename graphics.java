import javax.swing.JOptionPane;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.util.ArrayList;
import java.util.List;

class gui{
	class drawing{
		/* Proper input of respective types:
		 * LINE:
		 *	[X1,Y1,X2,Y2,WIDTH,COLOR]
		 *	types:
		 *	[int,int,int,int,int,java.awt.Color]
		 * RECTANGLE (RECT):
		 *	[X,Y,WIDTH,HEIGHT,FILLED,COLOR]
		 *	types:
		 *	[int,int,int,int,boolean,java.awt.Color]
		*/
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
			for(i : renderList){
				switch(i.drawing_type){
					case "line":
						break;
					case "rect":
						g.setColor(i.build[5])
						if(i.build[4]){
							g.fillRect(i.build[0],i.build[1],i.build[2],i.build[3])
						}
						else{
							g.drawRect(i.build[0],i.build[1],i.build[2],i.build[3])
						}
						
				}
			}
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
