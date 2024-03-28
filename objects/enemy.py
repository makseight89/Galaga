import pygame
from Galaga.objects import constans as c
import random


class Enemy(pygame.sprite.     Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.explosion_1 = pygame.image.load('images/explosion_1.png').convert_alpha()
        self.explosion_1 = pygame.transform.scale(self.explosion_1, (self.explosion_1.get_width() // 3,
                                                                     self.explosion_1.get_height() // 3))
        self.explosion_2 = pygame.image.load('images/explosion_2.png').convert_alpha()
        self.explosion_2 = pygame.transform.scale(self.explosion_2, (self.explosion_2.get_width() // 3,
                                                                     self.explosion_2.get_height() // 3))
        self.explosion_3 = pygame.image.load('images/explosion_3.png').convert_alpha()
        self.explosion_3 = pygame.transform.scale(self.explosion_3, (self.explosion_3.get_width() // 3,
                                                                     self.explosion_3.get_height() // 3))
        self.explosion_4 = pygame.image.load('images/explosion_4.png').convert_alpha()
        self.explosion_4 = pygame.transform.scale(self.explosion_4, (self.explosion_4.get_width() // 3,
                                                                     self.explosion_4.get_height() // 3))
        self.explosion_5 = pygame.image.load('images/explosion_5.png').convert_alpha()
        self.explosion_5 = pygame.transform.scale(self.explosion_5, (self.explosion_5.get_width() // 3,
                                                                     self.explosion_5.get_height() // 3))

        self.anim_explosion = [self.explosion_1,
                               self.explosion_2,
                               self.explosion_3,
                               self.explosion_4,
                               self.explosion_5]
        self.anim_index = 0
        self.frame_length_max = 8
        self.frame_length = self.frame_length_max
        self.image = pygame.image.load('images/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.is_destroyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('sounds/snd_hit.mp3')
        self.bullets = pygame.sprite.Group()
        self.hp = 1
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = 5
        self.speed = 2

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroyed:
            max_index = len(self.anim_explosion) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.kill()
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1

    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.hp -= 1
            if self.hp <= 0:
                self.is_invincible = True
                self.is_destroyed = True
                self.vel_y = 0
                self.vel_x = 0
                self.rect.x = self.rect.x - 25
                self.rect.y = self.rect.y - 25
                self.image = self.anim_explosion[self.anim_index]
        else:
            pass
