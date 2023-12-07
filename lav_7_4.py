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

def rotate_triangle(vertices, cx, cy, angle):
    rotated_vertices = [rotate_point(vertex[0], vertex[1], cx, cy, angle) for vertex in vertices]
    return rotated_vertices

pygame.init()

WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = pygame.Color('black')
TRIANGLE_COLOR = pygame.Color('white')
ROTATED_TRIANGLE_COLOR = pygame.Color('red')

window = pygame.display.set_mode((WIDTH, HEIGHT))

center_x = WIDTH // 2
center_y = HEIGHT // 2

triangle_vertices = [
    (150, 150),
    (200, 100),
    (250, 150)
]

angle = math.pi / 3

rotated_triangle = rotate_triangle(triangle_vertices, center_x, center_y, angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    pygame.draw.circle(window, TRIANGLE_COLOR, (center_x, center_y), 5)

    pygame.draw.polygon(window, TRIANGLE_COLOR, triangle_vertices, 1)

    pygame.draw.polygon(window, ROTATED_TRIANGLE_COLOR, rotated_triangle, 1)

    pygame.display.flip()

pygame.quit()
