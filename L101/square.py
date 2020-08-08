# I reffered an article for this. Please
# check it if you have trouble understanding this
# Brief Introduction to OpenGL in Python with PyOpenGL
# By Muhammad Junaid Khalid
# https://stackabuse.com/brief-introduction-to-opengl-in-python-with-pyopengl/

# This code includes refernces using
# unique reference code so that you can 
# search, find and understand each line
# of code. Please visit 
# https://github.com/naseemshah/OpenGLlabs/tree/master/Refrences
# and search for refernce code there.


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500,500

def square(): # in this function we define vertices of square to draw
    glBegin(GL_QUADS) # RE1000
    glVertex2f(100, 100) # RE1001 | Coordinates for the bottom left point
    glVertex2f(200, 100) # RE1001 | Coordinates for the bottom right point
    glVertex2f(200, 200) # RE1001 | Coordinates for the top right point
    glVertex2f(100, 200) # RE1001 | Coordinates for the top left point
    glEnd() # RE1000

def showScreen(): #This function we use to show stuff on screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # RE1002 Remove everything from screen
    glLoadIdentity() # RE1003 | Reset all graphic/shape's position
    iterate()
    glColor3f(1.0, 0.0, 3.0) # RE1005 | gives color to following code
    square() # Draw square
    glutSwapBuffers() # RE1004 | Swaps buffers

# However, our code is still not complete. What it currently
# does is draw the square once, and then clear the screen again.
# We don't want that. Actually, we won't even be able to spot the
# moment when it actually draws the square because it would appear
# and disappear in a split second. iterate() is used to avoid this.

def iterate():
    glViewport(0, 0, 500,500) # RE1006
    glMatrixMode(GL_PROJECTION) # RE1007
    glLoadIdentity() # RE1003
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) # RE1008
    glMatrixMode (GL_MODELVIEW) # RE1007
    glLoadIdentity() # RE1003


glutInit()
glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
glutInitWindowSize(500, 500)   # Set the w and h of your window
glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
wind = glutCreateWindow("Draw a Square | Naseem's OpenGLlabs") # Set a window title
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen) # Keeps the window open
glutMainLoop()  # Keeps the above created window displaying/running in a loop