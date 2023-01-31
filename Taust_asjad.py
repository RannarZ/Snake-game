import pygame

white = (200, 200, 200)
window_height = 600
window_width = 600
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((window_height, window_width))
prev_pos = None
backgroundsqr = pygame.Surface((30, 30))
