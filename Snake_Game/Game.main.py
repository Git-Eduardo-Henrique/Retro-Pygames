import pygame
from pygame.locals import *
Resolution = (480, 360)

pygame.init()
window = pygame.display.set_mode((Resolution[0], Resolution[1]))
pygame.display.set_caption('PySnake')

while True:
    pygame.display.update()
