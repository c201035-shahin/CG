import pygame
import sys

# Sutherland-Hodgman algorithm for line clipping
def sutherland_hodgman(points, xmin, ymin, xmax, ymax):
    result = []
    clip_edges = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]

    for edge_start, edge_end in zip(clip_edges, clip_edges[1:] + [clip_edges[0]]):
        result = []
        for i in range(len(points)):
            p1, p2 = points[i], points[(i + 1) % len(points)]
            if is_inside(p1[0], p1[1], edge_start[0], edge_start[1], edge_end[0], edge_end[1]):
                if is_inside(p2[0], p2[1], edge_start[0], edge_start[1], edge_end[0], edge_end[1]):
                    result.append(p2)
                else:
                    intersection = get_intersection(p1, p2, edge_start, edge_end)
                    result.append(intersection)
            elif is_inside(p2[0], p2[1], edge_start[0], edge_start[1], edge_end[0], edge_end[1]):
                intersection = get_intersection(p1, p2, edge_start, edge_end)
                result.append(intersection)

        points = result

    return result

def is_inside(x, y, xmin, ymin, xmax, ymax):
    return xmin <= x <= xmax and ymin <= y <= ymax

def get_intersection(p1, p2, edge_start, edge_end):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = edge_start
    x4, y4 = edge_end

    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denom == 0:
        return None

    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    intersection_x = x1 + t * (x2 - x1)
    intersection_y = y1 + t * (y2 - y1)

    return (intersection_x, intersection_y)

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Sutherland-Hodgman Line Clipping Algorithm")
clock = pygame.time.Clock()

x1, y1 = 50, 100
x2, y2 = 300, 300

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

    clipped_line = sutherland_hodgman([(x1, y1), (x2, y2)], xmin, ymin, xmax, ymax)
    if clipped_line:
        pygame.draw.line(screen, (255, 0, 0), clipped_line[0], clipped_line[1], 1)

    pygame.display.flip()
    clock.tick(60)
