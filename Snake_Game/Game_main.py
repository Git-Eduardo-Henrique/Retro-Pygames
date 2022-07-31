import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
# ==========================================================================================
# Configurações de tela
Resolution = (720, 480)
window = pygame.display.set_mode((Resolution[0], Resolution[1]))
pygame.display.set_caption('PySnake')
# ==========================================================================================
# Cores em rgb
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 204, 0)
black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)
# ==========================================================================================
# sons e musicas
'''music = pygame.mixer.music.load('')
pygame.mixer.music.play(-1)'''
score_sound = pygame.mixer.Sound('score.wav')
# ==========================================================================================
# posições
x_snake = 16
y_snake = 16
x_apple = randint(0, Resolution[0] - 16)
y_apple = randint(0, Resolution[1] - 16)
list_snake = []
# ==========================================================================================
# pontuações e outras variaveis
score = 0
# ==========================================================================================
# fonts e textos
font = pygame.font.SysFont('arial', 20, True, True)
# ==========================================================================================
fps = pygame.time.Clock()  # fps do jogo
# ==========================================================================================


def increase(list_xy):
    for pos in list_xy:
        pygame.draw.circle(window, green, (pos[0], pos[1]), 16)


while True:  # loop principal
    fps.tick(30)
    window.fill(black)  # preenche a tela com a cor preta
    list_pos = []
    # --------------------------------------------------------------------------------------
    # eventos no pygame
    for event in pygame.event.get():  # checar eventos
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                y_snake -= 25
            elif event.key == K_s:
                y_snake += 25
            elif event.key == K_d:
                x_snake += 25
            elif event.key == K_a:
                x_snake -= 25
    # --------------------------------------------------------------------------------------
    # desenha objetos na tela
    snake = pygame.draw.circle(window, green, (x_snake, y_snake), 16)
    apple = pygame.draw.circle(window, red, (x_apple, y_apple), 8)
    # --------------------------------------------------------------------------------------
    # listas
    list_pos.append(x_snake)
    list_pos.append(y_snake)
    list_snake.append(list_pos)
    # --------------------------------------------------------------------------------------
    # colições de objetos
    if snake.colliderect(apple):  # colição com a maça
        score_sound.play()  # toca o som de coleta
        x_apple = randint(0, Resolution[0] - 16)
        y_apple = randint(0, Resolution[1] - 16)
        score += 1
    # --------------------------------------------------------------------------------------
    # carrega os textos na tela
    text_point = font.render(f'SCORE: {score}', False, white)
    window.blit(text_point, (550, 0))
    # --------------------------------------------------------------------------------------
    increase(list_snake)   # aumenta o tamanho da cobra

    pygame.display.update()
