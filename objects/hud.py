import pygame
from Galaga.objects import constans as c
from Galaga.objects.health_bar import HealthBar
from Galaga.objects.heart_icon import HeartIcon
from Galaga.objects.score import Score
from Galaga.objects.lives import Lives


class HUD(pygame.sprite.Sprite):
    def __init__(self, hp, num_lives):
        super(HUD, self).__init__()
        self.image = pygame.image.load('images/hud.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.vel_x = 0
        self.vel_y = 0
        self.health_bar = HealthBar(hp)
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = c.DISPLAY_HEIGHT - self.health_bar.rect.height - 35
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.heart_icon = HeartIcon()
        self.lives = Lives(num_lives)
        self.lives.rect.x = 260
        self.lives.rect.y = c.DISPLAY_HEIGHT - 50
        self.icons_group = pygame.sprite.Group()
        self.icons_group.add(self.heart_icon)
        self.icons_group.add(self.lives)

    def update(self):
        self.health_bar_group.update()
        self.icons_group.update()
        self.score_group.update()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
