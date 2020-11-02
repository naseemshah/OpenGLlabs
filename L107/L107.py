
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init(): 
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(0,100,0,100) 

def drawPixel(x,y):
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()
    glFlush()

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


def non_polar_circle(xc, yc, radius):
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    x = xc - radius
    target = xc + radius
    glVertex2f(x, yc)
    glVertex2f(target, yc)
    factor = 7500
    incr = 1 / factor
    x += incr
    while x < target:
        adder = math.sqrt(radius * radius - (x - xc) * (x - xc))
        glVertex2f(x, yc + adder)
        glVertex2f(x, yc - adder)
        x += incr
    glEnd()
    glFlush()

def polar_circle(xc, yc, radius):
    theta = 0
    factor = 500
    incr = 1 / factor
    target = math.pi / 4
    glColor3f(0.0,1.0,0.5)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    while (theta <= target):
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x + xc, y + yc)
        glVertex2f(-x + xc, -y + yc)
        glVertex2f(-x + xc, y + yc)
        glVertex2f(x + xc, -y + yc)
        glVertex2f(y + xc, x + yc)
        glVertex2f(-y + xc, -x + yc)
        glVertex2f(-y + xc, x + yc)
        glVertex2f(y + xc, -x + yc)
        theta += incr
    glEnd()
    glFlush()



def main():
    choice = 0
    while (choice != -1):
        choice = input("Please Choose \n\t1. Plot a new Circle\n\t2. Non Polar Circle\n\t3.Polar Circle\n\t4. Exit\n")
        if int(choice) == 1:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Circle using Midpoint Circle Drawing Algorithm")
            glutDisplayFunc(lambda: midPointCircleDraw(x,y,r)) 
            glutIdleFunc(lambda: midPointCircleDraw(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 2:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Circle using Non Polar Circle")
            glutDisplayFunc(lambda: non_polar_circle(x,y,r)) 
            glutIdleFunc(lambda: non_polar_circle(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 3:
            x = int(input("\nEnter center:\n\tx: "))
            y = int(input("\n\ty: "))
            r = int(input("\nRadius: "))
            print("starting window....")
            glutInit(sys.argv)
            glutInitDisplayMode(GLUT_RGB)
            glutInitWindowSize(500,500)
            glutInitWindowPosition(0,0)
            glutCreateWindow("Plot Circle using Polar Circle")
            glutDisplayFunc(lambda: polar_circle(x,y,r)) 
            glutIdleFunc(lambda: polar_circle(x,y,r))
            init()
            glutMainLoop()
        elif int(choice) == 4:
            choice = -1
        else: 
            print("Invalid choice")
            choice = 0

main()
