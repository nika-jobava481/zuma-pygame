# ball.py

import pygame
from random import choice
from settings import WIDTH, HEIGHT

class Ball:
    def __init__(self,x,y):
        # Set initial position (you can adjust this as needed)
        self.x = x
        self.y = y

        # Set size
        self.size = 15

        # Set color randomly from red, green, blue, or yellow
        self.color = choice([(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)])

        # Set initial velocity
        self.velocity = [0, 0]

        self.shootable = True

    def draw(self, screen):
        # Draw the ball on the screen
        pygame.draw.circle(screen, self.color, (round(self.x), round(self.y)), self.size)

    def shoot(self, target_x, target_y, speed):
        if self.shootable:
        # Calculate the direction vector
            direction_x = target_x - self.x
            direction_y = target_y - self.y

            self.shootable = False


            # Normalize the direction vector
            magnitude = (direction_x**2 + direction_y**2)**0.5
            if magnitude != 0:
                direction_x /= magnitude
                direction_y /= magnitude

            # Set the velocity based on the direction and speed
            self.velocity = [direction_x * speed, direction_y * speed]

    def update(self):
        # Update the ball's position based on its velocity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        # Check if the ball is off-screen, and set shootable to True if it is
        if not (0 <= self.x <= WIDTH and 0 <= self.y <= HEIGHT):
            self.shootable = True
        print(self.x, self.y, self.shootable)