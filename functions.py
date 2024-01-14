import pygame
def draw_text(screen, text, color, font_size, position):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)