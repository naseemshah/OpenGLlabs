# This code includes refernces using
# unique reference code so that you can 
# search, find and understand each line
# of code. Please visit 
# https://github.com/naseemshah/OpenGLlabs/tree/master/Refrences
# and search for refernce code there.

# First Import necessary dependencies

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 

# Now we write an Initilisation Function
def init(): #Initialisation Function
    glClearColor(0.0,0.0,0.0,1.0) # RE1009 This is to clear the screen and set a color
    gluOrtho2D(-1.0,1.0,-1.0,1.0) # RE1010 Since we are working in 2D, we set up a two-dimensional orthographic viewing region.

# Now we need to make saperate function 
# for different Lines.

# Function to plot Horizontal Line
# on a given X-cordinate range 
# and of a specific Y-cordinate level
def hLine(xmin,xmax,y):
    glClear(GL_COLOR_BUFFER_BIT) # RE1002 This is to clear everything we previously drawn, if any
    glColor3f(1.0,0.0,0.0) # RE1007 This will set color RGB(1,0,0) which is red
    glPointSize(10.0) # RE1011 this will set the point with a specific radius that we give
    glBegin(GL_POINTS) # RE1001 We begin plotting point
    x = xmin
    while(x <= xmax): # this loop iterates from the xmin to xmax points
        glVertex2f(x,y) # this will plot the x,y points
        x = x + 0.05 # incerement along x by 0.05 (decrease this to get non dotted line)
    glEnd() # RE1001
    glFlush() # RE1012

# Function to plot Vertical Line
# on a given y-cordinate range 
# and of a specific x-cordinate level
def vLine(ymin,ymax,x):
    glClear(GL_COLOR_BUFFER_BIT) # RE1002 This is to clear everything we previously drawn, if any
    glColor3f(1.0,0.0,0.0) # RE1007 This will set color RGB(1,0,0) which is red
    glPointSize(10.0) # RE1011 this will set the point with a specific radius that we give
    glBegin(GL_POINTS) # RE1001 We begin plotting point
    y = ymin
    while(y <= ymax): # this loop iterates from the ymin to ymax points
        glVertex2f(x,y) # this will plot the x,y points
        y = y + 0.05 # incerement along y by 0.05 (decrease this to get non dotted line)
    glEnd() # RE1001
    glFlush() # RE1012


# now we define function to
# plot daigonal line
def diagonalLine(x,y):
    glClear(GL_COLOR_BUFFER_BIT) # RE1002 This is to clear everything we previously drawn, if any
    glColor3f(1.0,0.0,0.0) # RE1007 This will set color RGB(1,0,0) which is red
    glPointSize(10.0) # RE1011 this will set the point with a specific radius that we give
    glBegin(GL_POINTS) # RE1001 We begin plotting point
    while(x <= y): # this loop iterates from the (x,x) to (y,y) points
        glVertex2f(x,x) # this will plot the (x,x) points
        x = x + 0.05 # incerement along x by 0.05 (decrease this to get non dotted line)
    glEnd() # RE1001
    glFlush() # RE1012



def main():
    choice = input("Enter Choice: ")
    if(int(choice) == 1):
        xmin = float(input("Enter x start range: "))
        xmax = float(input("Enter x end range: "))
        y = float(input("Enter Y offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot Horizontal Line | Naseem's OpenGLlabs")
        glutDisplayFunc(lambda: hLine(xmin,xmax,y)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: hLine(xmin,xmax,y))
        init()
        glutMainLoop()
    elif (int(choice) == 2):
        ymin = float(input("Enter y start range: "))
        ymax = float(input("Enter y end range: "))
        x = float(input("Enter x offset: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot Vertical Line | Naseem's OpenGLlabs")
        glutDisplayFunc(lambda: vLine(ymin,ymax,x)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: vLine(ymin,ymax,x))
        init()
        glutMainLoop()
    elif (int(choice) == 3):
        x = float(input("Enter start cordinate(x,x) as x: "))
        y = float(input("Enter end cordinate(y,y) as y: "))
        print("starting window....")
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500,500)
        glutInitWindowPosition(0,0)
        glutCreateWindow("Plot diagonal Line | Naseem's OpenGLlabs")
        glutDisplayFunc(lambda: diagonalLine(x,y)) # Refer RE1013 for why the use of lambda
        glutIdleFunc(lambda: diagonalLine(x,y))
        init()
        glutMainLoop()
    else: 
        print("Invalid choice");



main()
