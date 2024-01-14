import pygame
import sys
import math
from settings import *
from shooter import Shooter
from functions import *
from ball import Ball

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set up the game clock
clock = pygame.time.Clock()

# Create the shooter object
shooter = Shooter((WIDTH - 30) // 2, HEIGHT - 90, 30, 60, screen)
ball = Ball(WIDTH // 2, HEIGHT - 60)


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # On mouse click, shoot a ball from the shooter towards the cursor
            ball.shoot(*pygame.mouse.get_pos(), speed=10)

    screen.fill((0, 0, 0))

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Update the shooter's angle
    shooter.update_angle(mouse_pos)

    # Draw the shooter
    shooter.draw(screen)

    # Update and draw the ball
    ball.update()  # Add an update method to Ball class
    ball.draw(screen)

    # Display the game version at the top-left corner
    draw_text(screen, GAME_VERSION, (255, 255, 255), 20, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
