import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Drawing and Text Example")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Draw a line
line_start = (50, 50)
line_end = (200, 100)
line_color = red
pygame.draw.line(screen, line_color, line_start, line_end, 5)

# Draw a circle
circle_center = (300, 150)
circle_radius = 50
circle_color = green
pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

# Draw a rectangle
rect_rect = pygame.Rect(400, 50, 100, 80)
rect_color = blue
pygame.draw.rect(screen, rect_color, rect_rect)

# Draw text
font = pygame.font.Font(None, 36)
text = font.render("Hello world!", True, white)
text_rect = text.get_rect(center=(width // 1.5, height // 2))
screen.blit(text, text_rect)

# Load and display an image
image_path = "Only Logo.png"  # Replace with the actual path to your image
try:
    image = pygame.image.load(image_path)
    image_rect = image.get_rect(center=(width // 4, height // 2 + 100))
    screen.blit(image, image_rect)
except pygame.error as e:
    print(f"Error loading image: {e}")

# Update the display
pygame.display.flip()

# Event loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
