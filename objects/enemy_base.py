import pygame
import random
from objects import constans as c


class Bullet(pygame.sprite.Sprite):
    def __init__(self, vel_y=-5, color=(255, 255, 255)):
        super().__init__()
        self.width = 8
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


class Shooter:
    def __init__(self, bullet_color=(255, 255, 255), bullet_vel_y=-5):
        self.bullet_color = bullet_color
        self.bullet_vel_y = bullet_vel_y
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('sounds/snd_bullet.mp3')

    def shoot(self, x, y):
        self.snd_shoot.play()
        new_bullet = Bullet(vel_y=self.bullet_vel_y, color=self.bullet_color)
        new_bullet.rect.x = x
        new_bullet.rect.y = y
        self.bullets.add(new_bullet)

    def update(self):
        self.bullets.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0 or bullet.rect.y >= c.DISPLAY_HEIGHT:
                self.bullets.remove(bullet)


class EnemyBase(pygame.sprite.Sprite):
    def __init__(self, img_path, explosion_paths, hp, score_value, vel_x, vel_y, bullet_color=(255, 255, 255)):
        super().__init__()
        self.image = self.load_and_scale_image(img_path)
        self.rect = self.image.get_rect()
        self.hp = hp
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.explosion_images = [self.load_and_scale_image(path) for path in explosion_paths]
        self.anim_explosion = self.explosion_images
        self.anim_index = 0
        self.frame_length_max = 8
        self.frame_length = self.frame_length_max
        self.is_destroyed = False
        self.is_invincible = False
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('sounds/snd_hit.mp3')
        self.hp = hp
        self.score_value = score_value
        self.shooter = Shooter(bullet_color=bullet_color, bullet_vel_y=5)  # Пули летят вниз

    def load_and_scale_image(self, path):
        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(image, (image.get_width() // 5, image.get_height() // 5))

    def update(self):
        self.shooter.update()
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

    def shoot(self):
        bullet_x = self.rect.x + (self.rect.width // 2) - 4  # Центр пули
        bullet_y = self.rect.y + self.rect.height  # Низ врага
        self.shooter.shoot(bullet_x, bullet_y)


class Enemy(EnemyBase):
    def __init__(self):
        explosion_paths = ['images/explosion_1.png', 'images/explosion_2.png', 'images/explosion_3.png']
        super().__init__('images/enemy.png', explosion_paths, hp=1, score_value=100, vel_x=0, vel_y=2,
                         bullet_color=(255, 0, 0))
        self.shooter = Shooter(bullet_color=(255, 0, 0), bullet_vel_y=5)

    def update(self):
        super().update()
        self.shooter.update()
        if random.randrange(0, 100) < 1:
            self.shoot()

    def shoot(self):
        bullet_x = self.rect.x + (self.rect.width // 2) - 4  # Центр пули
        bullet_y = self.rect.y + self.rect.height  # Низ врага
        self.shooter.shoot(bullet_x, bullet_y)

    @property
    def bullets(self):
        return self.shooter.bullets


class Enemy2(EnemyBase):
    def __init__(self):
        explosion_paths = ['images/explosion_1.png', 'images/explosion_2.png', 'images/explosion_3.png']
        super().__init__('images/enemy_2.png', explosion_paths, hp=1, score_value=100, vel_x=random.choice([-2, 2]),
                         vel_y=2, bullet_color=(
                255, 0, 0))  # Выбирает случайное значение -2 или 2 для начальной скорости по горизонтали
        self.shooter = Shooter(bullet_color=(255, 255, 255), bullet_vel_y=5)
        self.states = {'FLY_DOWN': 'FLY_DOWN', 'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True

    def update(self):
        super().update()
        self.shooter.update()
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        if random.randrange(0, 100) < 1:
            self.shoot()

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= 200:
            self.state = self.states['ATTACK']
            self.init_state = True

    def shoot(self):
        bullet_x = self.rect.x + (self.rect.width // 2) - 4
        bullet_y = self.rect.y + self.rect.height
        self.shooter.shoot(bullet_x, bullet_y)

    @property
    def bullets(self):
        return self.shooter.bullets
