
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-500,500,-500,500) 

def plotLine(x1,y1,x2,y2):
   
    m = 2 * (y2 - y1)
    pk = m - (x2 - x1)
    y=y1 

    glColor3f(1.0,0.0,0.0) 
    glPointSize(2.0) 
    glBegin(GL_POINTS)

    for x in range(x1,x2+1):
        glVertex2f(x,y)
        pk =pk + m
        if (pk>= 0):
            y=y+1
            pk =pk - 2 * (x2 - x1)
    glEnd() 
    

def scene():
    glClear(GL_COLOR_BUFFER_BIT)
    plotLine(-100,0,100,0)
    plotLine(-100,0,-50,1000)
    glFlush() 

# driver function
def main():
    
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Plot Line using Bresenham Algorithm | Naseem's OpenGLlabs")
    glutDisplayFunc(scene) 
    glutIdleFunc(scene)
    init()
    glutMainLoop()

main()





