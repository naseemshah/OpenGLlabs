from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
w, h = 500,500



GLOBAL_X = 500
GLOBAL_Y = 500
FPS = 60.0

### ABSTRACTIONS
## Transformations

class Transform:
    def __init__(self, points):
        self.points = points

    def translate(self,offsetX,offsetY):
        points = self.points  
        newpoints=[]
        for point in points:
            newpoints.append([point[0]+offsetX,point[1]+offsetY])
        self.points = newpoints
        # print(self.points)

    def rotate(self,theta):
        points=self.points
        newpoints=[]
        for point in points:
            newpoints.append([round(point[0]* math.cos(theta) - point[1] * math.sin(theta)), round(point[0] * math.sin(theta) + point[1] * math.cos(theta))])
        self.points = newpoints
        # print(self.points)
    
    def scale(self,scaleX,scaleY):
        print(scaleX,scaleY)
        points=self.points
        newpoints=[]
        for point in points:
            newpoints.append([point[0]*scaleX,point[1]*scaleX])
        self.points = newpoints

    def apply(self):
        return self.points




print("global X:"+ str(GLOBAL_X))
print("global Y:" + str(GLOBAL_Y))

def square():
    global GLOBAL_X
    global GLOBAL_Y
    points = [[GLOBAL_X,GLOBAL_Y],[GLOBAL_X+100,GLOBAL_Y],[GLOBAL_X+100,GLOBAL_Y+100],[GLOBAL_X,GLOBAL_Y+100]]
    sqtransform = Transform(points)
    sqtransform.translate(-400,-400)
    sqtransform.scale(5,5)
    points = sqtransform.apply()
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 3.0)
    glVertex2f(points[0][0], points[0][1])
    glVertex2f(points[1][0], points[1][1])
    glVertex2f(points[2][0], points[2][1])
    glVertex2f(points[3][0], points[3][1])
    glEnd()

def update(value):
    global GLOBAL_X
    global GLOBAL_Y
    global FPS
    glutPostRedisplay()
    glutTimerFunc(int(1000/FPS),update,int(0))
    # transform = Transform([[GLOBAL_X,GLOBAL_Y]])
    # transform.translate(100,0.0)
    # transform.rotate(30)
    # GLOBAL_X = transform.apply()[0][0]
    # GLOBAL_Y = transform.apply()[0][1]
    


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2000, 0.0, 2000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    square()
    glutSwapBuffers()
  


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE) 
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)

wind = glutCreateWindow("Draw a Square | Naseem's OpenGLlabs")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutTimerFunc(int(0),update,int(0))
glutMainLoop()