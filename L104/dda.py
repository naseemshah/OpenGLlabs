# This program uses DDA algorithm
# For deeper understanding in DDA
# Refer video by Abdul Bari on Youtube
# https://www.youtube.com/watch?v=W5P8GlaEOSI


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
    gluOrtho2D(0,100,0,100) # RE1010 This will set the origin @ bottom-left corner and 100x100 grid.
    
def plotLine(x1,y1,x2,y2):
    # According to DDA we need to perfom
    # following calclations before plotting
    # 1. Calculate change in X and Y.
    deltaX = x2-x1
    deltaY = y2-y1
    # 2. Calculate Steps. 
    steps = 0
    if(abs(deltaX)>abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    # 3. Calculate X & Y increment.
    Xincrement = deltaX/steps
    Yincrement = deltaY/steps

    # Finally we start ploting line :)

    glClear(GL_COLOR_BUFFER_BIT) # RE1002 This is to clear everything we previously drawn, if any
    glColor3f(1.0,0.0,0.0) # RE1007 This will set color RGB(1,0,0) which is red
    glPointSize(10.0) # RE1011 this will set the point with a specific radius that we give
    glBegin(GL_POINTS) # RE1001 sets point mode

    for step in range(1,steps+1): # Loops from 1 to n for n steps
        glVertex2f(x1,y1) # Plot the point at (x1,y1)
        x1 = x1 + Xincrement # update x1 to next X cordinate
        y1 = y1 + Yincrement # update y1 to next Y cordinate
    
    glEnd() # RE1001
    glFlush() # RE1012
        


# driver function
def main():
    # Ask for choice
    choice = 0
    while (choice != 2):
        choice = input("Please Choose \n\t1. Plot a New line\n\t2. Exit\n")
        if int(choice) == 1:
            x1 = int(input("Enter x1: "))
            y1 = int(input("Enter y1: "))
            x2 = int(input("Enter x2: "))
            y2 = int(input("Enter y2: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Line using DDA | Naseem's OpenGLlabs")
            glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2)) # Refer RE1013 for why the use of lambda
            glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))
            init()
            glutMainLoop()
        else: 
            print("Invalid choice")
            choice = 0

main()





