import pygame
from game.player import Player
from game.enemy import Enemy
from game.bullet import Bullet
from game.background import Background
from game.constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
import random

def spawn_enemies(level, screen):
    """
    Tworzy listę przeciwników na podstawie poziomu gry.

    Args:
        level: Numer poziomu gry. Określa liczbę przeciwników.
        screen: Ekran, na którym przeciwnicy będą rysowani.

    Returns:
        list: Lista obiektów klasy Enemy reprezentujących przeciwników.
    """
    enemies = []
    for _ in range(level):
        x = random.randint(0, SCREEN_WIDTH - 80)
        y = random.randint(0, 100)
        enemies.append(Enemy(screen, x, y))
    return enemies

def display_game_over(screen):
    """
    Wyświetla komunikat "GAME OVER" na ekranie i czeka na wciśnięcie dowolnego klawisza.

    Args:
        screen: Ekran, na którym wyświetlany jest komunikat.

    Returns:
        None
    """
    font = pygame.font.SysFont(None, 72)
    game_over_text = font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Obiekty gry
    background = Background(screen)
    player = Player(screen)
    bullets = []
    enemy_bullets = []
    level = 1
    enemies = spawn_enemies(level, screen)
    enemies_destroyed = 0
    player_lives = 3

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Strzelanie
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(Bullet(screen, player.x + 40, player.y, direction=-1))

        # Aktualizacja
        background.update()
        screen.fill((0, 0, 0))
        background.draw()
        player.update()
        for bullet in bullets:
            bullet.update()
        for enemy in enemies:
            enemy.update()
            if enemy.can_shoot():
                enemy_bullets.append(Bullet(screen, enemy.x + 40, enemy.y + 60, direction=1))

        for bullet in enemy_bullets:
            bullet.update()

        # Kolizje
        for bullet in bullets[:]:
            if not bullet.is_on_screen():
                bullets.remove(bullet)
                continue
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    enemies_destroyed += 1
                    break

        for bullet in enemy_bullets[:]:
            if bullet.rect.colliderect(player.rect):
                enemy_bullets.remove(bullet)
                player_lives -= 1
                if player_lives == 0:
                    display_game_over(screen)
                    running = False

        # Sprawdzanie zakończenia poziomu
        if not enemies:
            level += 1
            enemies = spawn_enemies(level, screen)

        # Wyświetlanie licznika zestrzelonych przeciwników
        score_text = font.render(f"Zestrzeleni: {enemies_destroyed}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - 200, 10))

        # Wyświetlanie liczby żyć
        heart_image = pygame.image.load("assets/heart.png").convert_alpha()
        heart_image = pygame.transform.scale(heart_image, (30, 30))
        for i in range(player_lives):
            screen.blit(heart_image, (SCREEN_WIDTH - 50 - i * 40, 50))

        # Rysowanie
        player.draw()
        for bullet in bullets:
            bullet.draw()
        for bullet in enemy_bullets:
            pygame.draw.rect(screen, (255, 0, 0), bullet.rect)  # Czerwony pocisk
        for enemy in enemies:
            enemy.draw()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
