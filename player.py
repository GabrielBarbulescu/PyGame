import pygame
from pygame.sprite import Group


from laser import Laser


class Player(pygame.sprite.Sprite):
    lasers: Group

    def __init__(self, pos, constraint, min_constrait, speed, fly):
        super().__init__()
        self.image = pygame.image.load("1234.png")
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.fly = fly
        self.max_x_constraint = constraint
        self.min_x_constrait = min_constrait
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 100

        self.lasers = pygame.sprite.Group()

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x += -self.speed
        if keys[pygame.K_UP]:
            self.rect.y += -self.fly
        elif keys[pygame.K_DOWN]:
            self.rect.y += self.fly
        if keys[pygame.K_SPACE]:
            self.shoot_laser()


    def constraint_left(self):

        if self.rect.x <= self.min_x_constrait:
            self.rect.x = self.max_x_constraint-64
        if self.rect.top <= self.max_x_constraint/1.5:
            self.rect.top = self.max_x_constraint/1.5
        if self.rect.bottom > self.max_x_constraint:
            self.rect.bottom = self.max_x_constraint

    def constrait_right(self):
        if self.rect.x >= self.max_x_constraint:
            self.rect.x = self.min_x_constrait

    def shoot_laser(self):
        if self.ready:
            self.lasers.add(Laser(self.rect.center))
        self.ready = False
        self.laser_time = pygame.time.get_ticks()
    def recharge(self):
        if not self.ready:  # verifica daca ready = false
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True



    def update(self):
        self.get_input()
        self.constraint_left()
        self.constrait_right()
        self.recharge()
        self.lasers.update()

