import pygame
import sys

def translate_point(x, y, tx, ty):
    return x + tx, y + ty

# Function to scale a point (x, y) about another point (cx, cy)
def scale_point(x, y, cx, cy, scaleX, scaleY):
    translated = translate_point(x - cx, y - cy, -cx, -cy)
    scaled = translated[0] * scaleX, translated[1] * scaleY
    return translate_point(scaled[0], scaled[1], cx, cy)

# Function to scale a triangle [(x1, y1), (x2, y2), (x3, y3)] about a point (cx, cy)
def scale_triangle(vertices, cx, cy, scaleX, scaleY):
    return [scale_point(vertex[0], vertex[1], cx, cy, scaleX, scaleY) for vertex in vertices]

# Triangle vertices
triangle_vertices = [(100, 100), (150, 200), (200, 100)]

# Center of scaling
scale_center_x = -50
scale_center_y = -50

# Origin Center
origin_center_x = 150
origin_center_y = 150

# Scaling factors
scale_x = 1.5
scale_y = 1.5

# Scale the triangle about the specified center
scaled_triangle = scale_triangle(triangle_vertices, scale_center_x, scale_center_y, scale_x, scale_y)

pygame.init()

screen = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, (0, 0, 255), triangle_vertices, 1)

    pygame.draw.circle(screen, (0, 0, 255), (origin_center_x, origin_center_y), 5)

    pygame.draw.polygon(screen, (255, 120, 0), scaled_triangle, 1)

    pygame.display.flip()
