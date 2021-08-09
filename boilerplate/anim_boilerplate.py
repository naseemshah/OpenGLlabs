from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

w, h = 500,500



GLOBAL_X = 0.0 
FPS = 60.0



def square():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 3.0)
    glVertex2f(GLOBAL_X, 100)
    glVertex2f(GLOBAL_X +100, 100)
    glVertex2f(GLOBAL_X +100, 200)
    glVertex2f(GLOBAL_X, 200)
    glEnd()

def update(value):
    global GLOBAL_X
    global FPS
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),update,int(0))
    GLOBAL_X = GLOBAL_X + 1.0
    


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2000, 0.0, 2000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    square()
    glutSwapBuffers()
  


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE) 
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)

wind = glutCreateWindow("Draw a Square | Naseem's OpenGLlabs")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutTimerFunc(int(0),update,int(0))
glutMainLoop()