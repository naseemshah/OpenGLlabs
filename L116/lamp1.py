from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import sys
import math
sys.setrecursionlimit(1000000000)

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(0, 500, 0, 500)

def bresenham(x1,y1,x2,y2):
 if (x1>x2):
  xinc=-1
 else:
  xinc=1
  
 if (y1>y2):
  yinc=-1
 else:
  yinc=1
 
 dx=abs(x2-x1)
 dy=abs(y2-y1)
 p=2*dy-dx
 
 x=x1
 y=y1
 glVertex2f(x,y)
 
 
 while (x<=x2):
  x= x + xinc
  if p<0:
   p=p+2*dy
  else:
   y=y+yinc
   p=p+2*dy-2*dx
  glVertex2f(x,y)
  


def mouse(btn, state, x, y):
    y=500-y
    if btn == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        
     glClear(GL_COLOR_BUFFER_BIT)
     glColor3f(1, 1, 1)
     glBegin(GL_POINTS)
     edges,points=getPolygon()
     bresenham(100,200,150,400)
     bresenham(150,400,250,400)
     bresenham(250,400,300,200)
     bresenham(300,200,100,200)
     
     glEnd()
     glFlush()
        
      
def drawPolygons(edges, points):
    for e in edges:
        for v in e:
            glVertex2fv(points[v])

def circle():
 x1=450
 y1=450
 r=10
 for i in range(0,361):
  glVertex2f(x1+r*math.cos(i),y1+r*math.sin(i))

def display(edges, points):
    glLineWidth(2)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 0)
    glBegin(GL_POINTS)
    bresenham(100,200,150,400)
    bresenham(150,400,250,400)
    bresenham(250,400,300,200)
    bresenham(300,200,100,200)

    circle()
    glEnd()
    glFlush()

def getPolygon():
    n = 4
    edges = list(list())
    points = list(list())

    for i in range(n):
        edges += [[i, (i+1) % n]]

    points += [[100.0, 200.0]]
    points += [[150.0, 400.0]]
    points += [[250.0, 400.0]]
    points += [[300.0, 200.0]]
    

    return edges, points

def main():
    edges, points = getPolygon()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Lamp")
    init()
    glutDisplayFunc(lambda: display(edges,points))
    glutMouseFunc(mouse)
    glutMainLoop()


main()
