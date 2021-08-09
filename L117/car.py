from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys
import random

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-200.0, 200.0, -200.0, 200.0)


def glutFunct():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Animations")
    init()


def polarCircle(r, xc, yc):
    """
    The function takes radius and center of the circle as parameters.
    It finds the points to be plotted using 'polar circle drawing algorithm'.
    """

    xPoints = []
    yPoints = []
    pi = math.pi

    # The code for polar circle algorithm begins here
    for i in range(45):
        x = r * math.cos(pi/180*i)
        y = r * math.sin(pi/180*i)

        xPoints = xPoints + [x+xc, -x+xc, y +
                             xc, -y+xc, -y+xc, y+xc, -x+xc, x+xc]
        yPoints = yPoints + [y+yc, -y+yc, x +
                             yc, -x+yc, x+yc, -x+yc, y+yc, -y+yc]

    # The code for polar circle algorithm end here

    points = list(list())
    for i in range(len(xPoints)):
        points += [[xPoints[i], yPoints[i]]]

    return points


class Car:
    def __init__(self, point):
        self.refPoint = point       # the bottom left point of the car
        self.length = 100
        self.height = 75
        self.radius = self.length * 0.1

    def drawCar(self):
        # Vertices of car body
        vertices = [
            [self.refPoint[0], self.refPoint[1]],
            [self.refPoint[0], self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length*0.75, self.refPoint[1] + self.height],
            [self.refPoint[0] + self.length, self.refPoint[1] + self.height * 0.40],
            [self.refPoint[0] + self.length, self.refPoint[1]]
        ]

        # Centres of car tyres
        tyres = [
            [self.refPoint[0] + self.length * 0.20, self.refPoint[1]],
            [self.refPoint[0] + self.length * 0.80, self.refPoint[1]]
        ]

        glClear(GL_COLOR_BUFFER_BIT)
        glLineWidth(2.0)
        
        # Car body
        glBegin(GL_POLYGON)

        for i in vertices:
            glVertex2fv(i)

        glEnd()

        # Car tyres
        glBegin(GL_LINES)

        for i in tyres:
            points = polarCircle(self.radius, i[0], i[1])
            for p in points:
                glVertex2fv(p)

        glEnd()

        glutSwapBuffers()

    def update(self, value):
        self.refPoint[0] += 1
        glutPostRedisplay()
        glutTimerFunc(int(1000/60), self.update, (0))


def main():
    car = Car([-200, -50])
    glutFunct()
    glutDisplayFunc(car.drawCar)
    glutTimerFunc(0, car.update, 0)
    glutIdleFunc(car.drawCar)
    glutMainLoop()


main()