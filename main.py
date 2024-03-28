import pygame
from Galaga.objects import constans as c
from Galaga.objects import Ship
from Galaga.objects import BG
from Galaga.handlers import EnemySpawner
from Galaga.handlers import ParticleSpawner
from Galaga.handlers.event_handler import EventHandler
from Galaga.objects import AlertBox

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Display Setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# Object Setup
event_handler = EventHandler()
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
alert_box_group = pygame.sprite.Group()

# Music setup
pygame.mixer.music.load('sounds/msk_level.mp3')
pygame.mixer.music.set_volume(.5)
pygame.mixer.music.play(loops=True)

running = True
while running:
    clock.tick(fps)

    # Handle Events
    event_handler.handle_events(player)

    # Update events
    sprite_group.update()
    bg_group.update()
    enemy_spawner.update()
    particle_spawner.update()
    alert_box_group.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        player.hud.score.update_score(enemy[0].score_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0
            enemy[0].get_hit()
    for enemy in enemy_spawner.enemy_group:
        collided = pygame.sprite.groupcollide(sprite_group, enemy.bullets, False, False)
        for player, bullets in collided.items():
            if not player.is_invincible:
                player.get_hit()

    # Check for Game Over
    if not player.is_alive:
        enemy_spawner.clear_enemies()
        alert_box = AlertBox("GAME OVER")
        alert_box_group.add(alert_box)

    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        enemy.bullets.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)
    alert_box_group.draw(display)
    pygame.display.update()
