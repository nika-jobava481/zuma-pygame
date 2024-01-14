import pygame,math
from settings import *
from functions import draw_text
class Shooter:
    def __init__(self, x, y, width, height, mainSurf):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = 0
        self.image = pygame.image.load("shooter.png")
        self.mainSurf = mainSurf

    def update_angle(self, mouse_pos):
        dx = mouse_pos[0] - (self.x + self.width // 2)
        dy = mouse_pos[1] - (self.y + self.height // 2)
        self.angle = math.degrees(math.atan2(dx, dy)) + 180
        draw_text(self.mainSurf, f"{self.angle:.2f}°", (255, 255, 255), 20, (WIDTH-60, 10))

    def draw(self, screen):
        rotated_shooter = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_shooter.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(rotated_shooter, rotated_rect.topleft)