from ij import IJ
from java.awt import Color
from java.awt import Font
import time
import random

def demoFunction(name="Scott"):
    """just print some silly stuff in the console"""
    for fruit in ["orange","apple","pear","mango"]:
        print("%s loves %ss..."%(name,fruit))
        
def demo_create_image():
    """
    Create a gradient image and loop in some blur, noise, and words.
    This is nearly identical to java with the semicolons removed.
    """
    imp = IJ.createImage("testPic", "RGB ramp", 500, 200, 1);
    imp.show() # show it upfront so it's special
    ip = imp.getProcessor();
    for i in range(10):
        IJ.run(imp, "Gaussian Blur...", "sigma=1")
        IJ.run(imp, "Add Noise", "")
        fontSize=random.randint(20,200)
        ip.setFont(Font("Arial", Font.BOLD, fontSize)) 
        ip.setColor(Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        ip.drawString("Python", random.randint(0,250), random.randint(100,200))
        imp.updateAndDraw() # force a screen update
        time.sleep(.2) # wait for a redraw
    imp.changes = False # don't prompt to save when it's time to close
        
if __name__=="__main__":
    print("don't run me directly!")
    
    
     

