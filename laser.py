import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed=15):
        super().__init__()
        self.image = pygame.image.load("batarang.png")
        self.speed = speed
        self.rect = self.image.get_rect(center = pos)

    def update(self):
        self.rect.y -= self.speed

python