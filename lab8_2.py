import pygame
import sys

# Function to scale a point (x, y) about the origin (0, 0)
def scale_point(x, y, scaleX, scaleY):
    return x * scaleX, y * scaleY

# Function to scale a triangle [(x1, y1), (x2, y2), (x3, y3)] about the origin
def scale_triangle(vertices, scaleX, scaleY):
    return [scale_point(vertex[0], vertex[1], scaleX, scaleY) for vertex in vertices]

# Triangle vertices
triangle_vertices = [(50, 50), (100, 100), (150, 50)]

# Scaling factors
scale_x = 2
scale_y = 2

# Scale the triangle about the origin
scaled_triangle = scale_triangle(triangle_vertices, scale_x, scale_y)

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 400))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    pygame.draw.polygon(screen, (0, 0, 255), triangle_vertices, 1)
    
    pygame.draw.polygon(screen, (255, 0, 0), scaled_triangle, 1)

    pygame.display.flip()
