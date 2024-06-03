import pygame
from objects import constans as c
from objects.hud import HUD


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vel_y=-5, color=(255, 255, 255)):
        super(Bullet, self).__init__()
        self.width = 4
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = vel_y

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


class ShooterBase(pygame.sprite.Sprite):
    def __init__(self):
        super(ShooterBase, self).__init__()
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('sounds/snd_bullet.mp3')

    def shoot(self, bullet_color=(255, 255, 255), bullet_vel_y=-5):
        self.snd_shoot.play()
        new_bullet = Bullet(vel_y=bullet_vel_y, color=bullet_color)
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - (new_bullet.rect.width // 2)
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

    def update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0 or bullet.rect.y >= c.DISPLAY_HEIGHT:
                self.bullets.remove(bullet)


class Ship(ShooterBase):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 20, self.image.get_height() // 20))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.max_hp = 3
        self.lives = 3
        self.hp = self.max_hp
        self.snd_hit = pygame.mixer.Sound('sounds/snd_hit.mp3')
        self.hud = HUD(self.hp, self.lives)
        self.is_alive = True
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.is_invincible = False
        self.max_invincible_timer = 60
        self.invincible_timer = 0
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

    def update(self):
        super().update()
        self.hud_group.update()
        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        self.rect.y += self.vel_y

        if self.invincible_timer >= 0:
            self.invincible_timer -= 1
        else:
            self.is_invincible = False

    def get_hit(self):
        if self.is_alive and not self.is_invincible:
            self.hp -= 1
            self.snd_hit.play()
            self.hud.health_bar.decrease_hp_value()
            if self.hp <= 0:
                self.hp = 0
                self.death()

    def death(self):
        self.lives -= 1
        if self.lives <= 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        self.hud.lives.decrement_live()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer