import pygame
import sys

# Liang-Barsky algorithm
def liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax):
    t0, t1 = 0, 1
    dx, dy = x2 - x1, y2 - y1

    p = [-dx, dx, -dy, dy]
    q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]

    for i in range(4):
        if p[i] == 0:
            if q[i] < 0:
                return None
        else:
            t = q[i] / p[i]
            if p[i] < 0 and t > t0:
                t0 = t
            elif p[i] > 0 and t < t1:
                t1 = t

    if t0 < t1:
        clipped_x1 = x1 + t0 * dx
        clipped_y1 = y1 + t0 * dy
        clipped_x2 = x1 + t1 * dx
        clipped_y2 = y1 + t1 * dy
        return clipped_x1, clipped_y1, clipped_x2, clipped_y2
    else:
        return None

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Liang-Barsky Line Clipping Algorithm")
clock = pygame.time.Clock()

# Line coordinates
x1, y1 = 50, 100
x2, y2 = 300, 300

# Window boundaries
xmin, ymin = 100, 80
xmax, ymax = 300, 280

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.line(screen, (0, 0, 255), (x1, y1), (x2, y2), 1)

    pygame.draw.rect(screen, (255, 0, 0), (xmin, ymin, xmax - xmin, ymax - ymin), 1)

    result = liang_barsky(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
    if result is not None:
        clipped_x1, clipped_y1, clipped_x2, clipped_y2 = result
        pygame.draw.line(screen, (255, 0, 0), (clipped_x1, clipped_y1), (clipped_x2, clipped_y2), 1)

    pygame.display.flip()
    clock.tick(60)
