import pygame
import sys
from pygame.locals import *

pygame.init()

width, height = 400, 240
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bangladeshi Flag")

green = (0, 128, 0)
red = (204, 0, 0)

screen.fill(green)

pygame.draw.circle(screen, red, (width // 2.2, height // 2), 50)

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
