import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *

# inicializa o Pygame
pygame.init()
tamanho_da_janela = (800, 600)
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

cor_atual = (0.0, 1.0, 0.0)  # começa com a cor verde
tamanho_do_ponto = 5  # tamanho inicial dos pontos
forma_atual = 'ponto'

# metodo para desenhar os pontos e linhas
def desenhar():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # desenhar linhas conectando os pontos
    glColor3f(1.0, 1.0, 1.0)  # cor das linhas: branco
    glBegin(GL_LINE_STRIP)
    for ponto in pontos:
        glVertex2fv(ponto[0:2])
    glEnd()

    # desenhar pontos
    glPointSize(tamanho_do_ponto)
    glBegin(GL_POINTS)
    for ponto in pontos:
        glColor3fv(ponto[2])  # define a cor do ponto
        glVertex2fv(ponto[0:2])
    glEnd()

    pygame.display.flip()

# metodo para adicionar uma forma geométrica
def adicionar_forma(x, y):
    if forma_atual == 'ponto':
        pontos.append((x, y, cor_atual))
    elif forma_atual == 'triangulo':
        pontos.append((x, y, cor_atual))
        pontos.append((x + 20, y, cor_atual))
        pontos.append((x + 10, y + 20, cor_atual))
    elif forma_atual == 'quadrado':
        pontos.append((x, y, cor_atual))
        pontos.append((x + 20, y, cor_atual))
        pontos.append((x + 20, y + 20, cor_atual))
        pontos.append((x, y + 20, cor_atual))

# loop para manter a aplicação rodando
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            rodando = False
        elif evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:  # Botão esquerdo do mouse
                x, y = evento.pos
                y = tamanho_da_janela[1] - y  # Ajustar a coordenada y para corresponder à janela do OpenGL
                adicionar_forma(x, y)
            elif evento.button == 3:  # Botão direito do mouse
                pontos = []  # Limpa todos os pontos
        elif evento.type == KEYDOWN:
            if evento.key == K_c:  # Tecla 'C' para mudar a cor dos pontos
                cor_atual = (pygame.mouse.get_pos()[0] / tamanho_da_janela[0],
                             pygame.mouse.get_pos()[1] / tamanho_da_janela[1],
                             1.0)
            elif evento.key == K_UP:  # Tecla 'UP' para aumentar o tamanho dos pontos
                tamanho_do_ponto += 1
            elif evento.key == K_DOWN:  # Tecla 'DOWN' para diminuir o tamanho dos pontos
                tamanho_do_ponto = max(1, tamanho_do_ponto - 1)  # o tamanho mínimo do ponto é 1
            elif evento.key == K_t:  # Tecla 'T' para desenhar triângulos
                forma_atual = 'triangulo'
            elif evento.key == K_q:  # Tecla 'Q' para desenhar quadrados
                forma_atual = 'quadrado'
            elif evento.key == K_p:  # Tecla 'P' para desenhar pontos
                forma_atual = 'ponto'

    desenhar()

pygame.quit()
