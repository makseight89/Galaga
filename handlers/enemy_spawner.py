import random
import pygame
from objects import constans as c
from objects.enemy_base import Enemy, Enemy2


class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.enemy_group.update()
        for enemy in self.enemy_group:
            if enemy.rect.y >= c.DISPLAY_HEIGHT:
                enemy.kill()  # Удаляем врага, если он выходит за границу экрана
        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(30, 120)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
        random_number = random.randrange(0, 100)
        if random_number <= 75:
            new_enemy = Enemy()
        elif random_number >= 76:
            new_enemy = Enemy2()
        self.enemy_group.add(new_enemy)


    def clear_enemies(self):
        self.enemy_group.empty()
        