from textwrap import fill
import pygame
import Taust_asjad as ta
import sys
import Mängija
import Õunad
import random


active_sprite_list = pygame.sprite.Group()

player = Mängija.Mangija(30, 30)
player.rect.x = 300
player.rect.y = 300
active_sprite_list.add(player)
clock = pygame.time.Clock()


def drawGrid():
    square_size = 30
    for x in range(0, ta.window_width, square_size):
        for y in range(0, ta.window_height, square_size):
            if x == 30 or y == 30:
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(ta.screen, (0, 0, 255), rect, 1)
            elif x == 540 or y == 540:
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(ta.screen, (0, 0, 255), rect, 1)
            else:
                rect = pygame.Rect(x, y, square_size, square_size)
                pygame.draw.rect(ta.screen, ta.white, rect, 1)


def main():
    pygame.init()
    while True:
        drawGrid()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT:
                    player.change_x = -15
                    player.change_y = 0
                if event.key == pygame.K_RIGHT:
                    player.change_x = 15
                    player.change_y = 0
                if event.key == pygame.K_UP:
                    player.change_y = -15
                    player.change_x = 0
                if event.key == pygame.K_DOWN:
                    player.change_y = 15
                    player.change_x = 0

        player.rect.x += player.change_x
        player.rect.y += player.change_y
        active_sprite_list.update()
        ta.screen.fill((0, 0, 0))
        drawGrid()
        active_sprite_list.draw(ta.screen)
        clock.tick(10)
        if player.rect.x <= 30 or player.rect.x >= 540:
            pygame.quit()
            sys.exit()
        if player.rect.y <= 30 or player.rect.y >= 540:
            pygame.quit()
            sys.exit()

        pygame.display.update()


main()
