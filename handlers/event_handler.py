import pygame
from objects import constans as c


class EventHandler:
    def __init__(self):
        pygame.joystick.init()
        self.num_joysticks = pygame.joystick.get_count()
        print(self.num_joysticks)
        self.joystick = None
        if self.num_joysticks:
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()

    def handle_events(self, actor):
        for event in pygame.event.get():
            self.check_quit_event(event)
            self.check_keyboard_event(event, actor)
            self.check_joystick_event(event, actor)

    @staticmethod
    def check_quit_event(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    def check_keyboard_event(self, event, actor):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                actor.vel_x = -actor.speed
            elif event.key == pygame.K_RIGHT:
                actor.vel_x = actor.speed
            if event.key == pygame.K_SPACE:
                actor.shoot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                actor.vel_x = 0
            elif event.key == pygame.K_RIGHT:
                actor.vel_x = 0

    def check_joystick_event(self, event, actor):
        if event.type == pygame.JOYHATMOTION:
            if self.joystick.get_hat(0) == c.XB_HAT_LEFT:
                actor.vel_x = -actor.speed
            elif self.joystick.get_hat(0) == c.XB_HAT_RIGHT:
                actor.vel_x = actor.speed
            if self.joystick.get_hat(0) == c.XB_HAT_NEUTRAL:
                actor.vel_x = 0

        if event.type == pygame.JOYBUTTONDOWN:
            if self.joystick.get_button(c.XB_A):
                actor.shoot()
