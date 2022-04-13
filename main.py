import random
import sys
import time
import pygame
from pygame import sprite

from enemy import Enemy
from player import Player


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, minx_point, 5, 5)  # 5=speed of mooving
        self.player = pygame.sprite.GroupSingle(player_sprite)  # make a player object from
        self.enemys = pygame.sprite.Group()

        enemy1 = Enemy((300, 64), screen_width, 3)
        self.enemys.add(enemy1)



        self.nr_total_enemy = 0

    def collisions(self):
        sprite.groupcollide(self.enemys, self.player.sprite.lasers, self.enemys, self.player.sprite.lasers)

    def add_enemy(self):
        a = [-15, -2, -3, -4, 2, 3, 4,15]
        rand = random.choice(a)

        self.score = self.nr_total_enemy - len(self.enemys)
        current_time = pygame.time.get_ticks() / 50
        if current_time % 1.5 == 0:

            enemy1 = Enemy((300, 64), screen_width, rand)
            self.nr_total_enemy += 1
            self.enemys.add(enemy1)

            print("score", self.score)

    def run(self):
        self.collisions()

        self.add_enemy()
        #self.score.draw((screen))

        self.player.sprite.lasers.draw(screen)
        self.player.draw((screen))
        self.player.update()
        self.enemys.draw((screen))

        self.enemys.update()


if __name__ == '__main__':

    pygame.init()
    minx_point = 0
    screen_width = 1000
    screen_height = 1000

    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    joc = Game()  # instance of Game clas rinning inside while

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((30, 80, 30))
        joc.run()
        pygame.display.flip()
        clock.tick(60)
