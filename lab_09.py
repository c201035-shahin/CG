import pygame
import sys

# Cohen-Sutherland Line Clipping Algorithm
def cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax):
    INSIDE = 0  # 0000
    LEFT = 1    # 0001
    RIGHT = 2   # 0010
    BOTTOM = 4  # 0100
    TOP = 8     # 1000

    def compute_out_code(x, y):
        code = INSIDE
        if x < xmin:
            code |= LEFT
        elif x > xmax:
            code |= RIGHT
        if y < ymin:
            code |= BOTTOM
        elif y > ymax:
            code |= TOP
        return code

    outcode0 = compute_out_code(x0, y0)
    outcode1 = compute_out_code(x1, y1)
    accept = False

    while True:
        if not (outcode0 | outcode1):
            # Both endpoints inside the clip window
            accept = True
            break
        elif outcode0 & outcode1:
            # Both endpoints outside the clip window, in the same region
            break
        else:
            # Line needs clipping
            x, y = 0, 0
            outcode_out = outcode0 if outcode0 else outcode1

            if outcode_out & TOP:
                # Point is above the clip window
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & BOTTOM:
                # Point is below the clip window
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:
                # Point is to the right of the clip window
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:
                # Point is to the left of the clip window
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if outcode_out == outcode0:
                x0, y0 = x, y
                outcode0 = compute_out_code(x0, y0)
            else:
                x1, y1 = x, y
                outcode1 = compute_out_code(x1, y1)

    if accept:
        pygame.draw.line(screen, (0, 255, 0), (x0, y0), (x1, y1), 1)


# Initialize Pygame
pygame.init()

# Define the clipping window
xmin, ymin = 50, 50
xmax, ymax = 350, 350

# Define the line
x0, y0 = 20, 80
x1, y1 = 300, 400

# Set up the screen
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Cohen-Sutherland Line Clipping Algorithm")
clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the clipping window
    pygame.draw.rect(screen, (0, 0, 255), (xmin, ymin, xmax - xmin, ymax - ymin), 1)

    # Draw the original line
    pygame.draw.line(screen, (255, 255, 255), (x0, y0), (x1, y1), 1)

    # Clip and draw the line using Cohen-Sutherland algorithm
    cohen_sutherland(x0, y0, x1, y1, xmin, ymin, xmax, ymax)

    pygame.display.flip()
    clock.tick(60)
