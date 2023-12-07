import pygame
import sys

def scale_point(x, y, scale_x, scale_y):
    scaled_x = x * scale_x
    scaled_y = y * scale_y
    return scaled_x, scaled_y

pygame.init()

# Set up display
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scale Point About Origin")
clock = pygame.time.Clock()

# Original point coordinates
point_x, point_y = 50, 50

# Scaling factors
scale_x, scale_y = 2, 1.5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Scale the point about the origin
    scaled_point = scale_point(point_x, point_y, scale_x, scale_y)

    # Draw the original point
    pygame.draw.circle(screen, (0, 0, 255), (point_x, point_y), 5)
    font = pygame.font.Font(None, 20)
    label = font.render('Original Point', True, (0, 0, 0))
    screen.blit(label, (point_x, point_y - 15))

    # Draw the scaled point
    pygame.draw.circle(screen, (255, 0, 0), (int(scaled_point[0]), int(scaled_point[1])), 5)
    label = font.render('Scaled Point', True, (0, 0, 0))
    screen.blit(label, (scaled_point[0], scaled_point[1] - 15))

    pygame.display.flip()
    clock.tick(60)
