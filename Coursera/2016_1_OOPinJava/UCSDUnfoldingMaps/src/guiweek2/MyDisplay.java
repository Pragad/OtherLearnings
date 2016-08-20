package guiweek2;

import processing.core.PApplet;

// 1.
// You get the following warning, "
// The serializable class MyDisplay does not declare a static final serialVersionUID field of type long"
// So suppressing it http://stackoverflow.com/questions/2288937/what-does-it-mean-the-serializable-class-does-not-declare-a-static-final-serial

// 2.
// With newer version of "Processing", pApplet does not extend from Applet
// http://stackoverflow.com/questions/34716460/java-error-cannot-cast-to-java-applet-applet-in-eclipse

// 3.
// Declaration of PApplet and why "main" is required
// http://processing.github.io/processing-javadocs/core/index.html?processing/core/PApplet.html
@SuppressWarnings("serial")
public class MyDisplay extends PApplet
{
	public static void main(String... args) 
	{
		String[] pArgs = { "MyPapplet " };
		MyDisplay mp = new MyDisplay();
		PApplet.runSketch(pArgs, mp);
	}

	public void setup()
	{
		size(400, 400);
		background(150, 150, 150);
	}
	
	public void draw()
	{
		// 1. Looks like we have two types of functions. 
		// fill(), noFill() etc that defines what should be done for the next set of methods
		fill(225, 225, 0);
		ellipse(200, 200, 400, 400);
		fill(0, 0 , 0);
		ellipse(120, 130, 50, 30); // Left Eye
		ellipse(280, 130, 50, 30); // Right Eye
		
		// noFill should be before Arc
		noFill();
		arc(200, 280, 75, 75, 0, PI);
	}
}
