import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# inicializa o Pygame
pygame.init()
tamanho_da_janela = (500, 400)
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

cor_atual = (0.0, 1.0, 0.0)  # começa com verde
tamanho_do_ponto = 5  # tamanho inicial dos pontos

# metodo para desenhar os pontos
def desenhar_pontos():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPointSize(tamanho_do_ponto)
    glBegin(GL_POINTS)
    for ponto in pontos:
        glColor3fv(ponto[2])  # Define a cor do ponto
        glVertex2fv(ponto[0:2])
    glEnd()
    pygame.display.flip()

# loop para manter a aplicação rodando
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo do mouse
                x, y = evento.pos
                y = tamanho_da_janela[1] - y
                pontos.append((x, y, cor_atual))  # Adiciona o ponto com a cor atual
            elif evento.button == 3:  # Botão direito do mouse para limpar os pontos
                pontos = []  # deixa a lista dos pontos vazia
        elif evento.type == KEYDOWN:
            if evento.key == K_c:  # Tecla 'C' para mudar a cor dos pontos
                cor_atual = (pygame.mouse.get_pos()[0] / tamanho_da_janela[0],
                             pygame.mouse.get_pos()[1] / tamanho_da_janela[1],
                             1.0)
            elif evento.key == K_UP:  # Tecla 'UP' para aumentar o tamanho dos pontos
                tamanho_do_ponto += 1
            elif evento.key == K_DOWN:  # Tecla 'DOWN' para diminuir o tamanho dos pontos
                tamanho_do_ponto = max(1, tamanho_do_ponto - 1)  # O tamanho mínimo é 1

    desenhar_pontos()

pygame.quit()
