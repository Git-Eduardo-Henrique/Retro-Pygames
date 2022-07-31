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
# ==========================================================================================
# pontuações e outras variaveis
score = 0
# ==========================================================================================
# fonts e textos
font = pygame.font.SysFont('arial', 20, True, True)
# ==========================================================================================
fps = pygame.time.Clock()  # fps do jogo
# ==========================================================================================

while True:  # loop principal
    fps.tick(30)
    window.fill(black)  # preenche a tela com a cor preta
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
    # colições de objetos
    if snake.colliderect(apple):
        score_sound.play()
        x_apple = randint(0, Resolution[0] - 16)
        y_apple = randint(0, Resolution[1] - 16)
        score += 1
    # --------------------------------------------------------------------------------------
    # carrega os textos na tela
    text_point = font.render(f'SCORE: {score}', False, white)
    window.blit(text_point, (550, 40))
    # --------------------------------------------------------------------------------------
    pygame.display.update()
