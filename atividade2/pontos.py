import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# inicializa o Pygame
pygame.init()
tamanho_da_janela = (400, 350)
pygame.display.set_mode(tamanho_da_janela, DOUBLEBUF | OPENGL)

# configura o viewport
glViewport(0, 0, tamanho_da_janela[0], tamanho_da_janela[1])
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluOrtho2D(0, tamanho_da_janela[0], 0, tamanho_da_janela[1])
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# lista com os valores dos pontos
pontos = []

# metodo para desenhar os pontos
def desenhar_pontos():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    for ponto in pontos:
        glVertex2fv(ponto)
    glEnd()
    pygame.display.flip()

# loop para manter a aplicação rodando
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:  # botão esquerdo do mouse
                x, y = evento.pos
                y = tamanho_da_janela[1] - y  # ajustar a coordenada y para corresponder à janela do OpenGL
                pontos.append((x, y))

    desenhar_pontos()

pygame.quit()
