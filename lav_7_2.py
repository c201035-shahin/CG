import pygame
import math

def rotate_point(x, y, cx, cy, angle):
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)

    translated_x = x - cx
    translated_y = y - cy

    rotated_x = translated_x * cos_angle - translated_y * sin_angle
    rotated_y = translated_x * sin_angle + translated_y * cos_angle

    return rotated_x + cx, rotated_y + cy

pygame.init()

WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = pygame.Color('white')
CENTER_COLOR = pygame.Color('black')
POINT_COLOR = pygame.Color('red')
ROTATED_POINT_COLOR = pygame.Color('yellow')

window = pygame.display.set_mode((WIDTH, HEIGHT))

center_x = WIDTH // 2
center_y = HEIGHT // 2

point_x = 250
point_y = 150

angle = math.pi / 4

rotated_point_x, rotated_point_y = rotate_point(point_x, point_y, center_x, center_y, angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    pygame.draw.circle(window, CENTER_COLOR, (center_x, center_y), 5)

    pygame.draw.circle(window, POINT_COLOR, (point_x, point_y), 5)

    pygame.draw.circle(window, ROTATED_POINT_COLOR, (int(rotated_point_x), int(rotated_point_y)), 5)

    pygame.display.flip()

pygame.quit()
