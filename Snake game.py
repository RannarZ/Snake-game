from textwrap import fill
import pygame
import Taust_asjad as ta
import sys
import Mängija
import Õunad
import random
import Saba


active_sprite_list = pygame.sprite.Group()

player = Mängija.Mangija(30, 30)
apple = Õunad.Vaenlane(30, 30)
snake = [player]

apple.rect.x = 60
apple.rect.y = 270
player.rect.x = 300
player.rect.y = 300

active_sprite_list.add(player)
active_sprite_list.add(apple)

clock = pygame.time.Clock()


def drawGrid():
    square_size = 30
    for x in range(30, ta.window_width - 30, square_size):
        for y in range(30, ta.window_height - 30, square_size):
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
    movement = ""
    points = 0

    def gen_enemy_pos():
        x_coordinate = 30 * random.randint(2, 17)
        y_coordinate = 30 * random.randint(2, 17)
        if x_coordinate != player.rect.x and y_coordinate != player.rect.y:
            apple.rect.x = x_coordinate
            apple.rect.y = y_coordinate
        else:
            gen_enemy_pos()

    while True:
        if apple.rect.x == player.rect.x and apple.rect.y == player.rect.y:
            gen_enemy_pos()
            points += 1
            tail = Saba.Saba(30, 30)
            active_sprite_list.add(tail)
            tail.rect.x = points * 35
            snake.append(tail)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_LEFT and movement != "E" and movement != "W":
                    player.move_left(15)
                    movement = "W"
                if event.key == pygame.K_RIGHT and movement != "W" and movement != "E":
                    player.move_right(15)
                    movement = "E"
                if event.key == pygame.K_UP and movement != "S" and movement != "N":
                    player.move_up(15)
                    movement = "N"
                if event.key == pygame.K_DOWN and movement != "N" and movement != "S":
                    player.move_down(15)
                    movement = "S"

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
