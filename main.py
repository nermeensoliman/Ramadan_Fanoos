from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np  # for circle
import math  # for circle and bresenham line algo


def myInit():
    glClearColor(1.0, .9, 0.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2)
    gluOrtho2D(0, 500, 0, 500)


def drawBresenhamLine(x1, y1, x2, y2):
    """Draw a line using the Bresenham algorithm."""
    glColor3f(1.0, 0.8, 0)
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = abs(dy/dx) if dx != 0 else 0
    xinc = 1 if x2 > x1 else -1
    yinc = 1 if y2 > y1 else -1

    if slope <= 1:
        p0 = 2 * dy - dx
        for k in range(0, dx+1):
            glVertex2f(x1, y1)
            if p0 < 0:
                p0 = p0 + 2 * dy
                x1 = x1 + xinc
            else:
                p0 = p0 + 2 * dy - 2 * dx
                y1 = y1 + yinc
                x1 = x1 + xinc

    else:
        p0 = 2 * dx - dy
        for k in range(0, dy+1):
            glVertex2f(x1, y1)
            if p0 < 0:
                p0 = p0 + 2 * dx
                y1 = y1 + yinc
            else:
                p0 = p0 + 2 * dx - 2 * dy
                x1 = x1 + xinc
                y1 = y1 + yinc


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # elmorb3 ellabany
    glBegin(GL_QUADS)
    glColor3f(0, 1, 1)
    glVertex2f(0, 250)  # ta7t shmal
    glVertex2f(500, 250)  # ta7t ymeen
    glVertex2f(500, 500)  # fo2 ymeen
    glVertex2f(0, 500)  # fo2 shmal
    glEnd()
    # elmorb3 elly tahto
    glBegin(GL_QUADS)
    glColor3f(1, 0.7, 0)
    glVertex2f(0, 0)  # ta7t shmal
    glVertex2f(500, 0)  # ta7t ymeen
    glVertex2f(500, 250)  # fo2 ymeen
    glVertex2f(0, 250)  # fo2 shmal
    glEnd()

    # morb3 elkbeer (elbeet)
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.5, 0.05)
    glVertex2f(50, 50)  # ta7t shmal
    glVertex2f(200, 50)  # ta7t ymeen
    glVertex2f(200, 200)  # fo2 ymeen
    glVertex2f(50, 200)  # fo2 shmal    
    glEnd()

    # rectangle gowa elbeet
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.6, 0.4)
    glVertex2f(125, 50)  # ta7t shmal
    glVertex2f(175, 50)  # ta7t ymeen
    glVertex2f(175, 135)  # fo2 ymeen
    glVertex2f(125, 135)  # fo2 shmal
    glEnd()

    # morb3 gowa elbeet
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glVertex2f(65, 135)  # ta7t shmal
    glVertex2f(115, 135)  # ta7t ymeen
    glVertex2f(115, 185)  # fo2 ymeen
    glVertex2f(65, 185)  # fo2 shmal
    glEnd()

    # mosalas
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50, 200)  # ta7t shmal
    glVertex2f(200, 200)  # ta7t ymeen
    glVertex2f(125, 275)  # fel nos
    glEnd()

    # shamssss
    glBegin(GL_POLYGON)
    glColor3f(1.0, 1.0, 0)

    x_centre = 475
    y_centre = 475
    r_inner = 25
    num_segments = 20  # number of segments to approximate the circle
    for i in range(num_segments):
        angle = 2.0 * math.pi * i / num_segments
        x = r_inner * math.cos(angle) + x_centre
        y = r_inner * math.sin(angle) + y_centre
        glVertex2f(x, y)
    glEnd()

    # khamas khtot elshams
    glBegin(GL_POINTS)
    drawBresenhamLine(407, 450, 450, 475)
    glEnd()

    glBegin(GL_POINTS)
    drawBresenhamLine(410, 430, 452, 465)
    glEnd()

    glBegin(GL_POINTS)
    drawBresenhamLine(410, 420, 455, 460)
    glEnd()

    glBegin(GL_POINTS)
    drawBresenhamLine(430, 410, 460, 455)
    glEnd()

    glBegin(GL_POINTS)
    drawBresenhamLine(440, 400, 470, 450)
    glEnd()

    glFlush()


glutInit()  # for displaying window
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # for lines and colors
glutInitWindowSize(500, 500)  # for size of window
glutCreateWindow("YAYA VIEW")
myInit()
glutDisplayFunc(display)  # for displaying the shape
glutMainLoop()  # for continue viewing
