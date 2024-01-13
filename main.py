import pygame
import sys
import math
from settings import *

# Function to draw the shooter

# Initialize Pygame
pygame.init()

# Shooter properties
shooter = {
    'width': 30,
    'height': 60,
}

# Load the shooter image
shooter_image = pygame.image.load("shooter.png")

# Initial position of the shooter
shooter['x'] = (WIDTH - shooter['width']) // 2
shooter['y'] = HEIGHT - shooter['height'] * 2

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Set up the game clock
clock = pygame.time.Clock()

# draw shooter object
def draw_shooter(screen, shooter, angle):
    rotated_shooter = pygame.transform.rotate(shooter_image, angle)
    rotated_rect = rotated_shooter.get_rect(center=(shooter['x'] + shooter['width'] // 2, shooter['y'] + shooter['height'] // 2))
    screen.blit(rotated_shooter, rotated_rect.topleft)

# calculate angle between shooter's center and mouse cursor
def calculate_angle(shooter, mouse_pos):
    dx = mouse_pos[0] - (shooter['x'] + shooter['width'] // 2)
    dy = mouse_pos[1] - (shooter['y'] + shooter['height'] // 2)
    return math.degrees(math.atan2(dx, dy))+180

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw
    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with a white background color, adjust as needed

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Calculate the angle between the shooter's center and mouse cursor
    deg = calculate_angle(shooter, mouse_pos)

    # Call the draw_shooter function with the calculated angle
    draw_shooter(screen, shooter, deg)

    # Refresh the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame and close the program
pygame.quit()
sys.exit()
