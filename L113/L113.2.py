
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math
import numpy
import random

WINDOW_SIZE = 2000
ANGLE= float(input("Angle of Inclination: "))
LINE_START_X= -WINDOW_SIZE
LINE_START_Y= -WINDOW_SIZE*math.tan(math.radians(ANGLE))
GLOBAL_X_POSTION = -WINDOW_SIZE
GLOBAL_Y_POSTION = -WINDOW_SIZE*math.tan(math.radians(ANGLE))
TARGET_FPS=60
RADIUS = float(input("Radius of Ball: "))
FRAMES = 0
j=0.0
SPEED_MULTIPLIER = float(input("Speed Mulitplier: "))




def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE) 

def update(value):
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global TARGET_FPS
    global j
    global FRAMES
    global SPEED_MULTIPLIER
    FRAMES = FRAMES + 1
    time = (FRAMES/60.0)
    j=j-(FRAMES/9)
    GLOBAL_X_POSTION = GLOBAL_X_POSTION + SPEED_MULTIPLIER*math.cos(math.radians(ANGLE))*time
    GLOBAL_Y_POSTION = GLOBAL_Y_POSTION - SPEED_MULTIPLIER*math.sin(math.radians(ANGLE))*time
    if GLOBAL_X_POSTION>(WINDOW_SIZE+100) or GLOBAL_X_POSTION<-100 :
        GLOBAL_X_POSTION = -WINDOW_SIZE
        GLOBAL_Y_POSTION = -WINDOW_SIZE*math.tan(math.radians(ANGLE))

    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,0)


def drawCircle(x,y):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)    
    global j
    for i in numpy.arange(0, 360.0, 1.0):
        glColor3f(0,abs(math.sin(i)),abs(math.sin(i))) 
        glVertex2f(RADIUS*math.cos(math.pi * (j+i) / 180.0) + x, RADIUS*math.sin(math.pi * (j+i) / 180.0) + y)
    glEnd()

def drawLine():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0,1.0,0.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(LINE_START_X,LINE_START_Y)
    glVertex2f(WINDOW_SIZE,0)
    glEnd()



def drawScene():
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global RADIUS
    global ANGLE
    drawLine()
    drawCircle(GLOBAL_X_POSTION+RADIUS*math.sin(math.radians(ANGLE)),GLOBAL_Y_POSTION + RADIUS*math.cos(math.radians(ANGLE)))
    glutSwapBuffers()




def main():
    print("Rolling Ball @ "+str(ANGLE)+"deg Starting Window:")    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB  | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pendulum | Naseem's OpenGLlabs")
    glutDisplayFunc(drawScene)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawScene)

    init()
    glutMainLoop()
  


main()
