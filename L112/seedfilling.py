# flood fill
#boundary fill

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import sys

sys.setrecursionlimit(1000000000)


def init():
    glClearColor(1.0, 1.0, 1.0, 0.0)
    gluOrtho2D(0, 500, 0, 500)


def setpixel(x, y, color):
    glColor3f(color[0], color[1], color[2])
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()
    glFlush()


def boundfill(x, y, boundaryColor, fillcolor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color != boundaryColor).any() and (color != fillcolor).any():
        boundfill(x+1, y, boundaryColor, fillcolor)
        boundfill(x-1, y, boundaryColor, fillcolor)
        boundfill(x, y+1, boundaryColor, fillcolor)
        boundfill(x, y-1, boundaryColor, fillcolor)
        boundfill(x+1, y+1, boundaryColor, fillcolor)
        boundfill(x-1, y+1, boundaryColor, fillcolor)
        boundfill(x+1, y-1, boundaryColor, fillcolor)
        boundfill(x-1, y-1, boundaryColor, fillcolor)

    else:
        setpixel(x, y, fillcolor)


def floodfill(x, y, backgroundColor, fillcolor):
    color = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
    if (color == backgroundColor).all() and (color != fillcolor).any():
        floodfill(x+1, y, backgroundColor, fillcolor)
        floodfill(x-1, y, backgroundColor, fillcolor)
        floodfill(x, y+1, backgroundColor, fillcolor)
        floodfill(x, y-1, backgroundColor, fillcolor)
        floodfill(x+1, y+1, backgroundColor, fillcolor)
        floodfill(x-1, y+1, backgroundColor, fillcolor)
        floodfill(x+1, y-1, backgroundColor, fillcolor)
        floodfill(x-1, y-1, backgroundColor, fillcolor)

    else:
        setpixel(x, y, fillcolor)


def mouse(btn, state, x, y):
    y = 500 - y
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        fillcolor = [0, 1, 0]
        boundaryColor = [1, 0, 1]
        boundfill(x, y, boundaryColor, fillcolor)

    elif btn == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
        fillcolor = [0, 0, 1]
        backgroundColor = glReadPixels(x, y, 1, 1, GL_RGB, GL_FLOAT)
        floodfill(x, y, backgroundColor, fillcolor)

def drawPolygons(edges, points):
    for e in edges:
        for v in e:
            glVertex2fv(points[v])

def display(edges, points):
    glLineWidth(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)
    glBegin(GL_LINE_LOOP)
    drawPolygons(edges, points)
    glEnd()
    glFlush()

def getPolygon():
    n = int(input("Enter the number of edges : "))
    edges = list(list())
    points = list(list())

    for i in range(n):
        edges += [[i, (i+1) % n]]

    for i in range(n):
        x = float(input("Enter the x-coordinate value of point " + str(i+1) + ": "))
        y = float(input("Enter the y-coordinate value of point " + str(i+1) + ": "))
        points += [[x, y]]

    return edges, points

def main():
    edges, points = getPolygon()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Seed fill")
    init()
    glutDisplayFunc(lambda: display(edges,points))
    glutMouseFunc(mouse)
    glutMainLoop()


main()