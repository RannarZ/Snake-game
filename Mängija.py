import pygame
import Taust_asjad

white = (200, 200, 200)
red = (255, 0, 0)
vec = pygame.math.Vector2


class Mangija(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.change_x = 0
        self.change_y = 0

    def move_right(self, move_x):
        self.change_x += move_x

    def move_left(self, move_x):
        self.change_x -= move_x

    def move_up(self, move_y):
        self.change_y -= move_y

    def move_down(self, move_y):
        self.change_y += move_y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        if self.rect.x < 30:
            self.rect.x = 30
        if self.rect.x > Taust_asjad.window_width - 2 * self.rect.width:
            self.rect.x = Taust_asjad.window_width - 2 * self.rect.width

        if self.rect.y < 30:
            self.rect.y = 30
        if self.rect.y > Taust_asjad.window_height - 2 * self.rect.height:
            self.rect.y = Taust_asjad.window_height - 2 * self.rect.height
