import pygame
from objects import constans as c


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.font_size = 24
        self.color = (255, 255, 255)
        self.font = pygame.font.Font(None, self.font_size)
        self.x_pad = 20
        self.y_pad = 25
        self.image = self.font.render(f'Score: {self.value}', False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - self.y_pad

    def update_score(self, value):
        self.value += value
        self.image = self.font.render(f'Score: {self.value}', False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH - self.rect.width - self.x_pad
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - self.y_pad
