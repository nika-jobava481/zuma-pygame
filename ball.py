# ball.py

import pygame
from random import choice
from settings import WIDTH, HEIGHT

class Ball:
    def __init__(self):
        # Set initial position (you can adjust this as needed)
        self.x = WIDTH // 2
        self.y = HEIGHT // 2

        # Set size
        self.size = 15

        # Set color randomly from red, green, blue, or yellow
        self.color = choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
