

import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, speed=5):
        super().__init__()
        self.image = pygame.image.load("joker.png")
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.max_x_constraint = constraint
        self.curent_time = 0
        self.enemy_spown_time = 3000
        self.ready_enem = True

        self.enemys = pygame.sprite.Group()



    def move(self):
        self.rect.x += self.speed
        if self.rect.x <= 0 or self.rect.x >= self.max_x_constraint - 32:
            self.speed = - self.speed
            self.rect.y += 90
        if self.rect.y>= self.max_x_constraint:
            self.rect.y = 64




    def update(self):

        self.move()

