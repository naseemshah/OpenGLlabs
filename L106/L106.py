    import OpenGL 
    OpenGL.ERROR_ON_COPY = True 

    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    w,h = 500,500

    def init2D(r,g,b):
        glClearColor(r,g,b,0.0)    
        glMatrixMode (GL_PROJECTION)
        gluOrtho2D (0, 500.0, 0, 500.0)

    def midPointAlg(X1,Y1,X2,Y2):  
        dx = X2 - X1  
        dy = Y2 - Y1  
        d = dy - (dx/2)  
        x = X1 
        y = Y1  
        print(x,",",y,"\n") 
        i = 0 
        while (x < X2): 
            x=x+1
            if(d < 0): 
                d = d + dy  
    
            else: 
                d = d + (dy - dx)  
                y=y+1
            
            X[i] = x
            Y[i] = y
            i = i + 1
        
    def plot():
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(4.0)
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POINTS)
        for i in range(length):
            glVertex2i(X[i],Y[i])    
        glEnd()
        glFlush()
            




    x1 = int(input("Enter x1: "))
    x2 = int(input("Enter x2: "))
    y1 = int(input("Enter y1: "))
    y2 = int(input("Enter y2: "))

    global length 
    length = (x2-x1) if (x2-x1) > (y2-y1) else (y2-y1)
    X = [0] * length
    Y = [0] * length
    midPointAlg(x1,y1,x2,y2)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(w, h)
    glutInitWindowPosition(100,100)
    glutCreateWindow('Mid-point Algorithm to plot a Line')
    init2D(0.0,0.0,0.0)
    glutDisplayFunc(plot)
    glutMainLoop()