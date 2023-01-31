import pygame


class Saba(pygame.sprite.Sprite):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((230, 0, 0))
        self.rect = self.image.get_rect()
