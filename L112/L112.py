# Experiment VIII: Seed filling algorithms
# Write a program to implement seed filling using
# a)flood fill
# b)boundary fill

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
sys.setrecursionlimit(15000)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)


def setPixel(x, y, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def boundaryFill(x, y, boundaryColor, fillColor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color != boundaryColor).any() and (color != fillColor).any():
        setPixel(x, y, fillColor)
        boundaryFill(x+1, y, boundaryColor, fillColor)
        boundaryFill(x-1, y, boundaryColor, fillColor)
        boundaryFill(x, y+1, boundaryColor, fillColor)
        boundaryFill(x, y-1, boundaryColor, fillColor)


def floodFill(x, y, backgroundColor, fillcolor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color == backgroundColor).all() and (color != fillcolor).any():
        setPixel(x, y, fillcolor)
        floodFill(x+1, y, backgroundColor, fillcolor)
        floodFill(x-1, y, backgroundColor, fillcolor)
        floodFill(x, y+1, backgroundColor, fillcolor)
        floodFill(x, y-1, backgroundColor, fillcolor)


def mouse(btn, state, x, y):
    y = 500 - y
    if btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fillcolor = [1, 1, 1]
        boundaryColor = [0, 1, 1]
        boundaryFill(x, y, boundaryColor, fillcolor)

    elif btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        fillcolor = [0, 0, 1]
        backgroundColor = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
        floodFill(x, y, backgroundColor, fillcolor)


def display():
    glLineWidth(2)
    # glPointSize(1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 1)

    glBegin(GL_LINE_LOOP)
    glVertex2i(200, 200)
    glVertex2i(250, 200)
    glVertex2i(250, 250)
    glVertex2i(200, 250)
    glEnd()

    glFlush()


def main():
    print("Click left mouse button flood filling in the desired area.")
    print("Click right mouse button boundary filling in the desired area.")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Fill Algorithms")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()


main()
