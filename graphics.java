import javax.swing.JOptionPane;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JFrame;
import java.util.ArrayList;
import java.util.List;

class gui{
	class drawing{
		public drawing(){
			//nothing here
		}
		class rect{
			String type = "rect";
			int x1;
			int y1;
			int width;
			int height;
			boolean filled;
			Color color;
			public rect(int _x1, int _y1, int _width,int _height,boolean _filled,Color _color){
				x1 = _x1;
				y1 = _y1;
				width = _width;
				height = _height;
				filled = _filled;
				color = _color;
			}
		}
		class line{
			String type = "line";
			int x1;
			int y1;
			int x2;
			int y2;
			Color color;
			public line(int _x1, int _y1, int _x2, int _y2, Color _color){
				x1 = _x1;
				y1 = _y1;
				x2 = _x2;
				y2 = _y2;
				color = _color;
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
			for(int i=0;i<renderList.size();i++){
				System.out.println(renderList.get(i));
				//drawing td = renderList.get(i);
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
		drawing d = new drawing();
		drawing.line l = d.new line(10,10,200,100,Color.GREEN);
		screen.renderList.add(l);
	}
}
class graphics{
	public static void main(String[] args){
		gui g = new gui();
		g.run();
	}
}
