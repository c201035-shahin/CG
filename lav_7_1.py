import pygame
import math

def rotate_point(x, y, angle):
    newX = x * math.cos(angle) - y * math.sin(angle)
    newY = x * math.sin(angle) + y * math.cos(angle)
    return newX, newY

pygame.init()

WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = pygame.Color('white')
POINT_COLOR = pygame.Color('red')
ROTATED_POINT_COLOR = pygame.Color('yellow')

window = pygame.display.set_mode((WIDTH, HEIGHT))

pointX = 150
pointY = 100

angle = math.pi / 4

rotatedPointX, rotatedPointY = rotate_point(pointX, pointY, angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    pygame.draw.circle(window, POINT_COLOR, (pointX, pointY), 10)

    pygame.draw.circle(window, ROTATED_POINT_COLOR, (int(rotatedPointX), int(rotatedPointY)), 10)

    pygame.display.flip()

pygame.quit()
