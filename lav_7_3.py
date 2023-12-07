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

def rotate_line(x1, y1, x2, y2, cx, cy, angle):
    rotated_start = rotate_point(x1, y1, cx, cy, angle)
    rotated_end = rotate_point(x2, y2, cx, cy, angle)
    return rotated_start, rotated_end

pygame.init()

WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = pygame.Color('black')
LINE_COLOR = pygame.Color('white')
ROTATED_LINE_COLOR = pygame.Color('red')

window = pygame.display.set_mode((WIDTH, HEIGHT))

center_x = WIDTH // 2
center_y = HEIGHT // 2

line_start_x = 150
line_start_y = 150
line_end_x = 250
line_end_y = 150

angle = math.pi / 2.5

rotated_line_start, rotated_line_end = rotate_line(line_start_x, line_start_y, line_end_x, line_end_y, center_x, center_y, angle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BACKGROUND_COLOR)

    pygame.draw.circle(window, LINE_COLOR, (center_x, center_y), 5)

    pygame.draw.line(window, LINE_COLOR, (line_start_x, line_start_y), (line_end_x, line_end_y), 2)

    pygame.draw.line(window, ROTATED_LINE_COLOR, rotated_line_start, rotated_line_end, 2)

    pygame.display.flip()

pygame.quit()
