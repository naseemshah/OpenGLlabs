
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import * 
import math
import numpy
import random

WINDOW_SIZE = 2000
ANGLE= 40


end_y = 0
leg_offset = 80




def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE) 

def update(value):  
    global end_y
    glutPostRedisplay()
    glutTimerFunc(int(1000/60),update,0)

def drawPixel(x,y):
    glColor3f(1,1.0,1)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()

def midPointCircleDraw(x_centre, y_centre, r): 
    x = r 
    y = 0  
    drawPixel(x+x_centre,y+y_centre)
    if (r > 0) : 
        drawPixel(x+x_centre,-y+y_centre)
        drawPixel(y+x_centre,x+y_centre)
        drawPixel(y+x_centre,x+y_centre)
        drawPixel(-y+x_centre,x+y_centre)
    P = 1 - r  
    while x > y: 
        y += 1
        if P <= 0:  
            P = P + 2 * y + 1
        else:          
            x -= 1
            P = P + 2 * y - 2 * x + 1
        if (x < y): 
            break 
        drawPixel(x+x_centre,y+y_centre)  
        drawPixel(-x+x_centre,y+y_centre)  
        drawPixel(x+x_centre,-y+y_centre)  
        drawPixel(-x+x_centre,-y+y_centre)  
        if x != y: 
            drawPixel(y+x_centre,x+y_centre)  
            drawPixel(-y+x_centre,x+y_centre)  
            drawPixel(y+x_centre,-x+y_centre)  
            drawPixel(-y+x_centre,-x+y_centre) 

def snowMan():
    glClear(GL_COLOR_BUFFER_BIT) 
    midPointCircleDraw(0,0,100)
    midPointCircleDraw(0,-300,200)

def draw_hands_r():
    global end_y
    end_x = 400
    start_x = 150
    start_y = -200
    glColor3f(0.5,0.35,0.05)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2i(start_x,start_y)
    glVertex2i(end_x,end_y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x+80,end_y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x+50,end_y+80)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x+50,end_y-80)
    glEnd()
    glFlush()

def draw_leg_r():
    global leg_offset
    end_y = 0
    end_x = 0
    start_x = +150
    start_y = -450
    end_y = start_y - 200
    end_x = start_x + leg_offset
    print(leg_offset)
    glColor3f(0.5,0.35,0.05)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2i(start_x,start_y)
    glVertex2i(end_x,end_y)
    glEnd()
    glFlush()

def draw_leg_l():
    global leg_offset
    end_y = 0
    end_x = 0
    start_x = -150
    start_y = -450
    end_y = start_y - 200
    end_x = start_x - leg_offset
    glColor3f(0.5,0.35,0.05)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2i(start_x,start_y)
    glVertex2i(end_x,end_y)
    glEnd()
    glFlush()

def draw_hands_l():
    global end_y
    end_x = -450
    start_x = -150
    start_y = -200
    glColor3f(0.5,0.35,0.05)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2i(start_x,start_y)
    glVertex2i(end_x,end_y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x-80,end_y)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x-50,end_y+80)
    glEnd()
    glBegin(GL_LINES)
    glVertex2i(end_x,end_y)
    glVertex2i(end_x-50,end_y-80)
    glEnd()
    glFlush()


def drawScene():
    snowMan()
    draw_hands_r()
    draw_hands_l()
    draw_leg_r()
    draw_leg_l()
    glutSwapBuffers()




def getInputArrows(key,b,c):
    global end_y
    if(key==GLUT_KEY_UP):
        end_y = 0
        leg_offset = 0
        print("ARROW UP IS PRESSED")
    elif(key==GLUT_KEY_DOWN):
        end_y = -300
        leg_offset = 80
        print("ARROW DOWN IS PRESSED")


def main():
    print("Man Animation. Starting Window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Snowman Hands")
    glutSpecialFunc(getInputArrows)
    glutDisplayFunc(drawScene)
    glutTimerFunc(0,update,0)
    glutIdleFunc(drawScene)
    
    init()
    glutMainLoop()
  


main()
