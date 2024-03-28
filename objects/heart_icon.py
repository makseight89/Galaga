import pygame
from Galaga.objects import constans as c


class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.img__heart_1 = pygame.image.load('images/heart_1.png').convert_alpha()
        self.img__heart_2 = pygame.image.load('images/heart_2.png').convert_alpha()
        self.img__heart_3 = pygame.image.load('images/heart_3.png').convert_alpha()
        self.img__heart_4 = pygame.image.load('images/heart_4.png').convert_alpha()
        self.anim_list = [self.img__heart_1,
                          self.img__heart_2,
                          self.img__heart_3,
                          self.img__heart_4]
        self.anim_index = 0
        self.max_index = len(self.anim_list) - 1
        self.max_frame_duration = 7
        self.frame_duration = self.max_frame_duration
        self.image = self.anim_list[self.anim_index]
        self.rect = self.image.get_rect()
        self.rect.x = 430
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 650

    def update(self):
        if self.frame_duration == 0:
            self.anim_index += 1
            if self.anim_index > self.max_index:
                self.anim_index = 0
            self.image = self.anim_list[self.anim_index]
            self.frame_duration = self.max_frame_duration
        self.frame_duration -= 1
