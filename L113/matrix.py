from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *
from random import randint

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 500.0, 0, 500.0)

def multiply(X,Y):
	return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

def subdivide(a,b,t):
    c = point(0,0)
    c.x = a.x +(b.x-a.x)*t
    c.y = a.y +(b.y-a.y)*t
    return c

def bezier(points,t):
    subpoint = []
    for i in range(len(points)-1):
        subpoint.append(subdivide(points[i],points[i+1],t))
    if len(subpoint)==1:
        return subpoint[0]
    return bezier(subpoint,t)

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def translate(self,tx,ty):
		mat1 = [[1,0,tx],[0,1,ty],[0,0,1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def rotate(self,theta):
		mat1 = [[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def scale(self,sx,sy):
		mat1 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def ptranslate(self,tx,ty,x0,y0):
		self.translate(-x0,-y0)
		self.translate(tx,ty)
		self.translate(x0,y0)

	def protate(self,theta,x0,y0):
		self.translate(-x0,-y0)
		self.rotate(theta)
		self.translate(x0,y0)

	def pscale(self,sx,sy,x0,y0):
		self.translate(-x0,-y0)
		self.scale(sx,sy)
		self.translate(x0,y0)

class scene:
	def __init__(self, subject):
		self.subject = subject

	def draw(self):
		#specify ur scence

		#static elements
		self.bresline(0,20,500,20)  #floor

		#dynamic elements
		#bro
		self.breshell(5,5,self.subject[0].x,self.subject[0].y) #head Circle
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[3].x,self.subject[3].y) #leg joint to left leg
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[2].x,self.subject[2].y) #shoulder to leg joint
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[4].x,self.subject[4].y) #leg joint to right leg
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[5].x,self.subject[5].y) #shoulder to left hand
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[6].x,self.subject[6].y) #shoulder to right hand

		#bmw
		self.breshell(10, 10, self.subject[7].x, self.subject[7].y)  # back wheel
		self.breshell(10, 10, self.subject[8].x, self.subject[8].y)  # front wheel
		self.bresline(self.subject[8].x, self.subject[8].y, self.subject[9].x, self.subject[9].y)  #handle
		self.bresline(self.subject[7].x, self.subject[7].y, self.subject[17].x, self.subject[17].y)  #suspension
		self.bresline(self.subject[10].x, self.subject[10].y, self.subject[14].x, self.subject[14].y)  #tank
		self.bresline(self.subject[14].x, self.subject[14].y, self.subject[15].x, self.subject[15].y)  #tank
		self.bresline(self.subject[15].x, self.subject[15].y, self.subject[16].x, self.subject[16].y)  #tank
		self.bresline(self.subject[16].x, self.subject[16].y, self.subject[10].x, self.subject[10].y)  # tank


		points = self.subject[10:11]
		points.extend([self.subject[11], self.subject[11], self.subject[11]])
		points.extend([self.subject[12],self.subject[12],self.subject[12]])
		points.extend(self.subject[13:14])
		points.append(self.subject[10])
		for  i in range(0,100+50*len(points)):
			t = i/(99.0+50*len(points))
			p = bezier(points,t)
			glVertex2f(p.x,p.y)

		for i in range(1,8):
			self.bresline(self.subject[18].x, self.subject[18].y, self.subject[18+i].x, self.subject[18+i].y)  # tank
		glVertex2f(self.subject[18].x,self.subject[18].y)
		glVertex2f(self.subject[19].x, self.subject[19].y)
		glVertex2f(self.subject[20].x, self.subject[20].y)
		glVertex2f(self.subject[21].x, self.subject[21].y)
		glVertex2f(self.subject[22].x, self.subject[22].y)
		glVertex2f(self.subject[23].x, self.subject[23].y)
		glVertex2f(self.subject[24].x, self.subject[24].y)
		glVertex2f(self.subject[25].x, self.subject[25].y)

	def animate(self):
		#specify animation for each point
		global flag
		global angle
		global t
		global reached
		global smoke
		global stop

		if(self.subject[6].x < 400 and flag == False):
			for i in self.subject:
				i.translate(3,0)
		elif(angle < pi/3 and reached == False):
			angle += 0.1
			for i in self.subject:
				i.protate(0.1,self.subject[8].x,self.subject[8].y)
		elif(angle > 0.1 and not smoke):
			reached = True
			angle -= 0.1
			for i in self.subject:
				i.protate(-0.1,self.subject[8].x,self.subject[8].y)

		elif not stop:
			smoke = True
			for i in self.subject[19:26]:
				r1 = randint(-2,1)
				r = randint(-2,2) if i.y>20 else randint(0,2)

				i.translate(r1,r)

				if i.x<300:
					stop = True




	def bresline(self, x0, y0, x1, y1):
		dx = x1 - x0
		dy = y1 - y0
		xsign = 1 if dx > 0 else -1
		ysign = 1 if dy > 0 else -1
		dx = abs(dx)
		dy = abs(dy)
		if dx > dy:
			xx, xy, yx, yy = xsign, 0, 0, ysign
		else:
			dx, dy = dy, dx
			xx, xy, yx, yy = 0, ysign, xsign, 0
		D = 2 * dy - dx
		y = 0
		for x in range(int(dx + 1)):
			glVertex2f(x0 + x * xx + y * yx, y0 + x * xy + y * yy)
			if D >= 0:
				y += 1
				D -= 2 * dx
			D += 2 * dy

	def breshell(self,r1,r2,xc,yc):
		a = r1 * r1
		b = r2 * r2
		fa = 4*a
		fb = 4*b
		x = 0
		y = r2
		sigma = 2*b+a*(1-2*r2)
		while b*x <= a*y:
			glVertex2f(xc + x, yc + y)
			glVertex2f(xc - x, yc + y)
			glVertex2f(xc + x, yc - y)
			glVertex2f(xc - x, yc - y)
			if sigma >= 0:
				sigma += fa * (1 - y)
				y -= 1
			sigma += b * ((4 * x) + 6)
			x += 1

		x = r1
		y = 0
		sigma = 2 * a + b * (1 - 2 * r1)
		while a*y <= b*x:
			glVertex2f(xc + x, yc + y)
			glVertex2f(xc - x, yc + y)
			glVertex2f(xc + x, yc - y)
			glVertex2f(xc - x, yc - y)
			if sigma >= 0:
				sigma += fb * (1 - x)
				x -= 1
			sigma += a * ((4 * y) + 6)
			y += 1

def initial():
	subject = []
	#bro
	subject.append(point(30,85)) #head [0]
	subject.append(point(30,80)) #shoulder [1]
	subject.append(point(30,60)) #leg joint [2]
	subject.append(point(20,50)) #left leg [3]
	subject.append(point(40,50)) #right leg [4]
	subject.append(point(20,70)) #left hand [5]
	subject.append(point(40,70)) #right hand [6]
	#bmw
	subject.append(point(10,30))  #back wheel [7]
	subject.append(point(70,30))  #front wheel [8]
	subject.append(point(55,60))  #handle [9]
	subject.append(point(30,40))  #seat joint [10]
	subject.append(point(20,50))  #seat point [11]
	subject.append(point(10,50))  # seat point [12]
	subject.append(point(10,40))  # seat point [13]
	subject.append(point(40,50))  # tank point [14]
	subject.append(point(60,50))  # tank point [15]
	subject.append(point(60,40))  # tank point [16]
	subject.append(point(20,40))  # suspension [17]

	subject.append(point(10, 20)) # smoke [18]
	subject.append(point(10, 20)) #19
	subject.append(point(10, 20))
	subject.append(point(10, 20))
	subject.append(point(10, 20))
	subject.append(point(10, 20))
	subject.append(point(10, 20))
	subject.append(point(10, 20)) #25


	global sc
	sc = scene(subject)
	global flag
	global angle
	global t
	global reached
	global smoke
	global stop
	stop = False
	smoke = False
	reached = False
	flag = False
	angle = 0
	t = 0

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	sc.draw()
	sc.animate()
	glEnd()
	glFlush()
	time.sleep(0)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(1000, 1000)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Animation")
	initial()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()