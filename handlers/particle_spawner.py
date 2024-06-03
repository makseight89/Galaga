import pygame
import random


class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()
        self.width = random.randrange(1, 6)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = random.randrange(-16, 16)
        self.vel_y = random.randrange(-16, 16)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1


class ParticleSpawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()

    def spawn_particles(self, pos):
        random_number = random.randrange(3, 30)
        for num_particles in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = pos[0]
            new_particle.rect.y = pos[1]
            self.particle_group.add(new_particle)
