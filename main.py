import pygame
from objects import constans as c
from objects.background import Star, Planet
from objects.ship import Ship
from handlers.enemy_spawner import EnemySpawner
from handlers.particle_spawner import ParticleSpawner
from handlers.event_handler import EventHandler

# Инициализация Pygame и настройки звука
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# Настройка дисплея
display = pygame.display.set_mode(c.DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# Настройка объектов
event_handler = EventHandler()
bg_group = pygame.sprite.Group()


for _ in range(50):
    star = Star()
    bg_group.add(star)

for _ in range(5):
    planet = Planet()
    bg_group.add(planet)

player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
alert_box_group = pygame.sprite.Group()

# Настройка музыки
pygame.mixer.music.load('sounds/msk_level.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=True)

running = True


def create_alert_box(message):
    font = pygame.font.SysFont('Times New Roman', 50)
    text = font.render(message, True, (255, 0, 0))
    text_rect = text.get_rect(center=(c.DISPLAY_WIDTH // 2, c.DISPLAY_HEIGHT // 2))
    alert_box = pygame.Surface((text_rect.width + 20, text_rect.height + 20))
    alert_box.fill((0, 0, 0))
    alert_box.blit(text, (10, 10))
    alert_box_rect = alert_box.get_rect(center=(c.DISPLAY_WIDTH // 2, c.DISPLAY_HEIGHT // 2))

    display.blit(alert_box, alert_box_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Ожидание в течение 2 секунд

    alert_box_group.empty()


def display_game_over():
    global running
    enemy_spawner.clear_enemies()
    create_alert_box("Game Over")
    running = False


while running:
    clock.tick(fps)

    # Handle events
    event_handler.handle_events(player)

    # Update objects
    sprite_group.update()
    bg_group.update()
    enemy_spawner.update()
    particle_spawner.update()
    alert_box_group.update()

    # Check collisions
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemies in collided.items():
        for enemy in enemies:
            enemy.get_hit()
            player.hud.score.update_score(enemy.score_value)
            if not enemy.is_invincible:
                particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))

    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemies in collided.items():
        for enemy in enemies:
            if not enemy.is_invincible and not player.is_invincible:
                player.get_hit()
                enemy.hp = 0
                enemy.get_hit()

    for enemy in enemy_spawner.enemy_group:
        if hasattr(enemy, 'bullets'):
            collided = pygame.sprite.groupcollide(sprite_group, enemy.bullets, False, False)
            for player, bullets in collided.items():
                if not player.is_invincible:
                    player.get_hit()

    if not player.is_alive:
        display_game_over()

    # Draw all objects
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        if hasattr(enemy, 'bullets'):
            enemy.bullets.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.icons_group.draw(display)

    pygame.display.flip()
