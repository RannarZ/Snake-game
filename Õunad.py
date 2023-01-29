import pygame


class Ounad(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0
