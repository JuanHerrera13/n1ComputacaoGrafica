import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin

# método para desenhar um círculo
def desenha_circulo(raio, num_segmentos):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)
    for i in range(num_segmentos + 1):
        angle = 2.0 * 3.1415926 * i / num_segmentos
        x = raio * cos(angle)
        y = raio * sin(angle)
        glVertex2f(x, y)
    glEnd()

# método para desenhar o sol
def desenha_sol():
    glColor3f(1.0, 1.0, 0.0)  # cor amarela
    desenha_circulo(0.3, 50)

    num_rays = 12
    ray_length = 0.6
    glColor3f(1.0, 1.0, 0.0)  # cor amarela
    for i in range(num_rays):
        glPushMatrix()
        glRotatef(360 * i / num_rays, 0, 0, 1)
        glBegin(GL_LINES)
        glVertex2f(0, 0)
        glVertex2f(0, ray_length)
        glEnd()
        glPopMatrix()

# método principal
def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluOrtho2D(-1, 1, -1, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        desenha_sol()

        pygame.display.flip()
        pygame.time.wait(10)

main()
