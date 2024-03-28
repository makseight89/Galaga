import pygame
from Galaga.objects import constans as c
import random
from Galaga.objects.bullet import Bullet


class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()
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
        self.image = pygame.image.load('images/enemy_2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 5, self.image.get_height() // 5))
        self.is_destroyed = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('sounds/snd_hit.mp3')
        self.hp = 1
        self.bullets = pygame.sprite.Group()
        self.bullet_timer_max = 60
        self.bullet_timer = self.bullet_timer_max
        self.states = {'FLY_DOWN': 'FLY_DOWN',
                       'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.score_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 4)

    def update(self):
        self.bullets.update()
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
            self.state_attack()
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

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= 200:
            self.state = self.states['ATTACK']
            self.init_state = True

    def state_attack(self):
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(-4, 4)
            self.init_state = False
        if self.bullet_timer == 0:
            self.shoot()
            self.bullet_timer = self.bullet_timer_max
        else:
            self.bullet_timer -= 1
        if self.rect.x <= 0:
            self.vel_x *= -1
        elif self.rect.x + self.rect.width >= c.DISPLAY_WIDTH:
            self.vel_x *= -1

    def shoot(self):
        new_bullet = Bullet()
        new_bullet.vel_y = 4
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)

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
