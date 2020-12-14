from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500,500,-500,500)
 


def scene():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glVertex2f(100,100)
    glFlush()


def main():   
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("OpenGL")
    glutDisplayFunc(scene)
    glutIdleFunc(scene)
    init()
    glutMainLoop()

main()





