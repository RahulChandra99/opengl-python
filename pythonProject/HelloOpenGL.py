import pygame
from pygame.locals import *  # * means everything
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)                      # scale of the window and the coordinates of the window (left,right,bottom,top)

def draw_star(x,y,size):
    glPointSize(size)
    glBegin(GL_POINTS)
    glVertex2i(x,y)
    glEnd()

done = False
init_ortho()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    draw_star(400,50,5)
    draw_star(400, 100, 10)
    draw_star(300, 170, 20)
    draw_star(100, 200, 30)

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()