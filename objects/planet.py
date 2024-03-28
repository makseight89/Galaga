import pygame
from Galaga.objects import constans as c
import random


class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet_1 = pygame.image.load('images/planet_1.png').convert_alpha()
        self.planet_2 = pygame.image.load('images/planet_2.png').convert_alpha()
        self.planet_3 = pygame.image.load('images/planet_3.png').convert_alpha()
        self.planet_4 = pygame.image.load('images/planet_4.png').convert_alpha()
        self.img_planets = [self.planet_1,
                            self.planet_2,
                            self.planet_3,
                            self.planet_4]
        self.num_planets = len(self.img_planets)
        self.img_index = random.randrange(0, self.num_planets - 1)
        self.image = self.img_planets[self.img_index]
        self.scale_value = random.uniform(0.25, 0.9)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() // 2.5),
                                                         int(self.image.get_height() // 2.5)))

        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = 0 - self.rect.height
        self.pos_x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.pos_y = 0 - self.rect.height
        self.vel_x = 0.0
        self.vel_y = random.uniform(0.9, 1.2)

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.x = int(self.pos_x)
        self.rect.y = int(self.pos_y)
