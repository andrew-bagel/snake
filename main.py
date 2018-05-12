# Pygame Template
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initialize pygame
pygame.init()
# pygame.mixer handles sound
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

#Game Loop - While Loop that needs a stop to it
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw / render
    screen.fill(BLACK)

    # do this last, after drawing everything, flip display
    pygame.display.flip()

pygame.quit()