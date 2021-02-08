
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

ANGLE_HAND = 40
HAND_ANIM_DIR = 1
IS_ILFTED = True


box_x1 = GLOBAL_X_POSTION+130
box_y1 = GLOBAL_Y_POSTION-250
box_x2 = box_x1+400
box_y2 = box_y1
box_x3 = box_x2
box_y3 = box_y1+400
box_x4 = box_x1
box_y4 = box_y3
IS_BOX_LEFT = False


def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE) 

def update(value):
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global TARGET_FPS
    global SPINE_START_X
    global SPINE_START_Y
    global SPINE_END_X
    global SPINE_END_Y
    global ANGLE_HAND
    global HAND_ANIM_DIR
    global GLOBAL_X_DIR
    global box_x1
    global box_y1
    global box_x2
    global box_y2
    global box_x3
    global box_y3
    global box_x4
    global box_y4
    global IS_BOX_LEFT
    if(GLOBAL_X_POSTION==WINDOW_SIZE):
        GLOBAL_X_DIR = -1
    elif (GLOBAL_X_POSTION == -WINDOW_SIZE):
        GLOBAL_X_DIR = 1
    
    if(GLOBAL_X_DIR == 1):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION
    elif(GLOBAL_X_DIR == -1):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION

    if(IS_ILFTED):
        box_x1 = GLOBAL_X_POSTION-200
        box_y1 = GLOBAL_Y_POSTION+230
        box_x2 = box_x1+400
        box_y2 = box_y1
        box_x3 = box_x2
        box_y3 = box_y1+400
        box_x4 = box_x1
        box_y4 = box_y3
        
    else:
        if(IS_BOX_LEFT):
            box_x1 = GLOBAL_X_POSTION-520
        else:
            box_x1 = GLOBAL_X_POSTION+130
        box_y1 = GLOBAL_Y_POSTION-250
        box_x2 = box_x1+400
        box_y2 = box_y1
        box_x3 = box_x2
        box_y3 = box_y1+400
        box_x4 = box_x1
        box_y4 = box_y3
        
    





    
    SPINE_START_X= GLOBAL_X_POSTION
    SPINE_START_Y= GLOBAL_Y_POSTION
    SPINE_END_X= SPINE_START_X
    SPINE_END_Y= SPINE_START_Y-200

    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,0)


def plotLineDDA(x1,y1,x2,y2):
    deltaX = x2-x1
    deltaY = y2-y1
    steps = 0
    if(abs(deltaX)>abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    Xincrement = deltaX/steps
    Yincrement = deltaY/steps
    glColor3f(1.0,0.0,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    for step in range(1,steps+1):
        glVertex2f(round(x1),round(y1))
        x1 = x1 + Xincrement
        y1 = y1 + Yincrement
    glEnd()
    glFlush()

def drawBox():
    global GLOBAL_X_POSTION
    global GLOBAL_Y_POSTION
    global box_x1
    global box_y1
    global box_x2
    global box_y2
    global box_x3
    global box_y3
    global box_x4
    global box_y4
    plotLineDDA(box_x1,box_y1,box_x2,box_y2)
    plotLineDDA(box_x2,box_y2,box_x3,box_y3)
    plotLineDDA(box_x3,box_y3,box_x4,box_y4)
    plotLineDDA(box_x4,box_y4,box_x1,box_y1)



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
    drawBox()
    glutSwapBuffers()



def getInputArrows(key,b,c):
    global IS_ILFTED
    global GLOBAL_X_POSTION
    global IS_BOX_LEFT

    
    if(key==GLUT_KEY_UP):
        IS_ILFTED = True
        print("ARROW UP IS PRESSED")
    elif(key==GLUT_KEY_DOWN):
        IS_ILFTED = False
        print("ARROW DOWN IS PRESSED")
    elif(key==GLUT_KEY_LEFT):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION - 50
        IS_BOX_LEFT = True
        print("ARROW LEFT IS PRESSED")
    elif(key==GLUT_KEY_RIGHT):
        GLOBAL_X_POSTION = GLOBAL_X_POSTION + 50
        IS_BOX_LEFT = False
        print("ARROW RIGHT IS PRESSED")


def main():
    print("Man Animation. Starting Window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("BOY MOVING | Naseem's OpenGLlabs")
    glutSpecialFunc(getInputArrows)
    glutDisplayFunc(drawScene)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawScene)
    
    init()
    glutMainLoop()
  


main()
