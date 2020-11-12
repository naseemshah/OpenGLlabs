from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500,500.0,-500,500.0)

def plotaxes():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(0,-500)
    glVertex2f(0,500)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(500,0)
    glVertex2f(-500,0)
    glEnd()

def plotgrid():
    glColor3f(0.202, 0.202, 0.202)
    for i in range(-500,500,50):
        if i != 0:
            glBegin(GL_LINES)
            glVertex2f(i,500)
            glVertex2f(i,-500)
            glEnd()
            glBegin(GL_LINES)
            glVertex2f(500,i)
            glVertex2f(-500,i)
            glEnd()
        # glBegin(GL_LINES)
        # glVertex2f(-100,x)
        # glVertex2f(100,x)
        # glEnd()
        
def plotTraingle(x1,x2,x3,y1,y2,y3):
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x2,y2)
    glVertex2f(x3,y3)
    glEnd()
    glBegin(GL_LINES)
    glVertex2f(x3,y3)
    glVertex2f(x1,y1)
    glEnd()



def drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([point[0]+tx,point[1]+ty])
    print(newpoints)

    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

def drawScaled(x1,x2,x3,y1,y2,y3,tx,ty):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([point[0]*tx,point[1]*ty])
    print(newpoints)

    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

def drawReflected(x1,x2,x3,y1,y2,y3,ch):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        if(ch==1):
            newpoints.append([point[0], -point[1]])
        elif(ch==2):
            newpoints.append([-point[0], point[1]])
        elif(ch==3):
            newpoints.append([-point[0], -point[1]])
        elif(ch==4):
            newpoints.append([point[1], point[0]])
        elif(ch==5):
            newpoints.append([-point[1], -point[0]])

        
    print(newpoints)

    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

def drawRotated(x1,x2,x3,y1,y2,y3,theta):
    points=[[x1,y1],[x2,y2],[x3,y3]]
    newpoints=[]
    for point in points:
        newpoints.append([round(point[0]* math.cos(theta) - point[1] * math.sin(theta)), round(point[0] * math.sin(theta) + point[1] * math.cos(theta))])
    print(newpoints)

    plotaxes()
    plotgrid()
    glColor3f(0, 0, 1)
    plotTraingle(x1,x2,x3,y1,y2,y3)
    glColor3f(1, 0, 1)
    plotTraingle(newpoints[0][0],newpoints[1][0],newpoints[2][0],newpoints[0][1],newpoints[1][1],newpoints[2][1])
    glFlush()

def rotate(x1,x2,x3,y1,y2,y3):
    theta= (math.pi/180) * int(input("\nEnter Degress to be rotated: "))
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("2D Transformations  | Naseem's OpenGLlabs")
    glutDisplayFunc(lambda: drawRotated(x1,x2,x3,y1,y2,y3,theta))
    init()
    glutMainLoop()

def scale(x1,x2,x3,y1,y2,y3):
    tx= int(input("\nEnter Scale along x: "))
    ty= int(input("\nEnter Scale along y: "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("2D Transformations  | Naseem's OpenGLlabs")
    glutDisplayFunc(lambda: drawScaled(x1,x2,x3,y1,y2,y3,tx,ty))
    init()
    glutMainLoop()

def reflect(x1,x2,x3,y1,y2,y3):
    print("Enter the type of reflection : ")
    ch = int(input("1.Reflection about x axis\n2. Reflection about y axis\n3.Reflection about origin\n4.Reflection about x=y line\n5. Reflection about x=-y line\n"))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("2D Transformations  | Naseem's OpenGLlabs")
    glutDisplayFunc(lambda: drawReflected(x1,x2,x3,y1,y2,y3,ch))
    init()
    glutMainLoop()

def translate(x1,x2,x3,y1,y2,y3,tx,ty):
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("2D Transformations  | Naseem's OpenGLlabs")
    glutDisplayFunc(lambda: drawTranslated(x1,x2,x3,y1,y2,y3,tx,ty))
    init()
    glutMainLoop()

def main():
    print("\nEnter Triangle co-ordinates:")
    x1=float(input("\n\tx1: "))
    y1=float(input("\n\ty1: "))
    side=float(input("\n\tside: "))
    x2=side
    y2=y1
    x3=x1+side/2
    y3=y1+0.86602540378*side
    print("\nChoose Transformations:\n\t1.Translation\n\t2.Rotation\n\t3.Scale\n\t4.Reflection")
    ch=int(input("\nYour Choice: "))
    if ch == 1:
        translationX=int(input("\nX translation: "))
        translationY=int(input("\nY translation: "))
        translate(x1,x2,x3,y1,y2,y3,translationX,translationY)
    elif ch == 2:
        rotate(x1,x2,x3,y1,y2,y3)
    elif ch == 3:
        scale(x1,x2,x3,y1,y2,y3)
    elif ch == 4:
        reflect(x1,x2,x3,y1,y2,y3)
    

main()