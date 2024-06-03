import pygame
import random
from objects import constans as c


class CelestialBody(pygame.sprite.Sprite):
    def __init__(self):
        super(CelestialBody, self).__init__()
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.top > c.DISPLAY_HEIGHT:  # Reset position when it goes off screen
            self.reset_pos()

    def reset_pos(self):
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)
        self.rect.y = random.randrange(-20, -5)
        self.vel_y = random.randrange(1, 8)


class Star(CelestialBody):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 4)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)
        self.rect.y = random.randrange(0, c.DISPLAY_HEIGHT)
        self.vel_y = random.randrange(1, 4)

    def reset_pos(self):
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)
        self.rect.y = random.randrange(-20, -5)
        self.vel_y = random.randrange(1, 4)


class Planet(CelestialBody):
    def __init__(self):
        super(Planet, self).__init__()
        self.planet_1 = pygame.image.load('images/planet_1.png').convert_alpha()
        self.planet_2 = pygame.image.load('images/planet_2.png').convert_alpha()
        self.img_planets = [self.planet_1, self.planet_2]
        self.num_planets = len(self.img_planets)
        self.image = self.get_random_planet_image()
        self.rect = self.image.get_rect()
        self.reset_pos()

    def get_random_planet_image(self):
        img_index = random.randrange(self.num_planets)
        image = self.img_planets[img_index]
        scale_value = random.uniform(0.25, 0.9)
        scaled_image = pygame.transform.scale(image, (int(image.get_width() * scale_value // 2),
                                                      int(image.get_height() * scale_value // 2)))
        return scaled_image

    def reset_pos(self):
        self.image = self.get_random_planet_image()  # Ensure a new random planet image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-c.DISPLAY_HEIGHT, -self.rect.height)
        self.vel_y = random.uniform(0.5, 1.5)
