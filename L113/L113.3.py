
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math
import numpy
import random

WINDOW_SIZE = 2000
ANGLE= 40



GLOBAL_X_POSTION = 0
GLOBAL_Y_POSTION = 0
GLOBAL_X_DIR = 1
TARGET_FPS=60
RADIUS = 100
FRAMES = 0

SPINE_START_X= GLOBAL_X_POSTION
SPINE_START_Y= GLOBAL_Y_POSTION
SPINE_END_X= SPINE_START_X
SPINE_END_Y= SPINE_START_Y-200

ANGLE_HAND = 1.0
HAND_ANIM_DIR = 1


def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE) 

def update(value):
    global GLOBAL_X_POSTION
    global TARGET_FPS
    global SPINE_START_X
    global SPINE_START_Y
    global SPINE_END_X
    global SPINE_END_Y
    global ANGLE_HAND
    global HAND_ANIM_DIR
    global GLOBAL_X_DIR
    if(GLOBAL_X_POSTION==WINDOW_SIZE):
        GLOBAL_X_DIR = -1
    elif (GLOBAL_X_POSTION == -WINDOW_SIZE):
        GLOBAL_X_DIR = 1
    
    if(GLOBAL_X_DIR == 1):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION + 10
    elif(GLOBAL_X_DIR == -1):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION - 10



    
    SPINE_START_X= GLOBAL_X_POSTION
    SPINE_START_Y= GLOBAL_Y_POSTION
    SPINE_END_X= SPINE_START_X
    SPINE_END_Y= SPINE_START_Y-200
    if(ANGLE_HAND==45.0):
        HAND_ANIM_DIR = -1
    elif(ANGLE_HAND==-45.0):
        HAND_ANIM_DIR = 1
    
    if(HAND_ANIM_DIR == 1):
        ANGLE_HAND = ANGLE_HAND + 1.0
    elif(HAND_ANIM_DIR == -1):
        ANGLE_HAND = ANGLE_HAND - 1.0

    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,0)



def drawHead(x,y):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)
    for i in numpy.arange(0, 360.0, 1.0):
        glColor3f(0,1,1) 
        glVertex2f(RADIUS*math.cos(math.pi * (i) / 180.0) + x, RADIUS*math.sin(math.pi * (i) / 180.0) + y)
    glEnd()

def drawSpine():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(0.0,1.0,0.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(SPINE_START_X,SPINE_START_Y)
    glVertex2f(SPINE_END_X,SPINE_END_Y)
    glEnd()

def drawLegL():
    global SPINE_END_X
    global SPINE_END_Y
    global SPINE_START_X
    global SPINE_START_Y
    glColor3f(1.0,1.0,1.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(SPINE_END_X,SPINE_END_Y)
    glVertex2f(SPINE_END_X-100*math.sin(math.radians(ANGLE_HAND)),SPINE_END_Y-100*math.cos(math.radians( ANGLE_HAND)))

    glEnd()



def drawLegR():
    global SPINE_END_X
    global SPINE_END_Y
    global SPINE_START_X
    global SPINE_START_Y
    global ANGLE_HAND
    glColor3f(1.0,1.0,0.0) 
    glLineWidth(2)
    glBegin(GL_LINES),
    glVertex2f(SPINE_END_X,SPINE_END_Y)
    glVertex2f(SPINE_END_X+100*math.sin(math.radians(ANGLE_HAND)),SPINE_END_Y-100*math.cos(math.radians( ANGLE_HAND)))
    glEnd()

def drawHandL():
    
    global SPINE_START_X
    global SPINE_START_Y
    glColor3f(1.0,1.0,1.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(SPINE_START_X,SPINE_START_Y-100)
    glVertex2f(SPINE_START_X-100*math.sin(math.radians(ANGLE_HAND)),SPINE_START_Y-100*math.cos(math.radians( ANGLE_HAND)))

    # glVertex2f(SPINE_START_X-100*math.sin(math.radians(45)),SPINE_START_Y-100*math.cos(math.radians(45)))
    glEnd()

def drawHandR():
    
    global SPINE_START_X
    global SPINE_START_Y
    glColor3f(1.0,1.0,1.0) 
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(SPINE_START_X,SPINE_START_Y-100)
    glVertex2f(SPINE_START_X-100*math.sin(math.radians(-ANGLE_HAND)),SPINE_START_Y-100*math.cos(math.radians(-ANGLE_HAND)))
    glEnd()

def drawScene():
    global SPINE_START_X
    global SPINE_START_Y
    drawSpine()
    drawHead(SPINE_START_X,SPINE_START_Y+RADIUS)
    drawLegL()
    drawLegR()
    drawHandL()
    drawHandR()
    glutSwapBuffers()




def main():
    print("Man Animation. Starting Window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB  | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Man | Naseem's OpenGLlabs")
    glutDisplayFunc(drawScene)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawScene)

    init()
    glutMainLoop()
  


main()
