import pygame
import random
from game.constants import ENEMY_WIDTH, ENEMY_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, screen, x, y):
        """
        Inicjalizuje przeciwnika z losowym ruchem i grafiką.

        Args:
            screen (pygame.Surface): Powierzchnia, na której przeciwnik jest rysowany.
            x (int): Początkowa pozycja w osi X.
            y (int): Początkowa pozycja w osi Y.
        """
        self.screen = screen
        self.image = pygame.image.load("assets/enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))
        self.x = x
        self.y = y
        self.speed = 2
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])
        self.change_direction_time = random.randint(2000, 5000)  # Czas zmiany kierunku w milisekundach
        self.last_change_time = pygame.time.get_ticks()
        self.last_shot_time = pygame.time.get_ticks()

    def update(self):
        """
        Aktualizuje pozycję przeciwnika i losowo zmienia kierunek ruchu.

        Returns:
            None
        """
        now = pygame.time.get_ticks()
        if now - self.last_change_time > self.change_direction_time:
            self.direction_x = random.choice([-1, 1])
            self.direction_y = random.choice([-1, 1])
            self.last_change_time = now
            self.change_direction_time = random.randint(2000, 5000)

        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y

        # Ograniczenie ruchu do ekranu
        if self.x <= 0 or self.x >= SCREEN_WIDTH - ENEMY_WIDTH:
            self.direction_x *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - ENEMY_HEIGHT:
            self.direction_y *= -1

    def can_shoot(self):
        """
        Sprawdza, czy przeciwnik może wystrzelić pocisk na podstawie czasu od ostatniego strzału.

        Returns:
            bool: True, jeśli przeciwnik może strzelić, False w przeciwnym wypadku.
        """
        now = pygame.time.get_ticks()
        if now - self.last_shot_time > random.randint(2000, 4000):  # Strzał co 2-4 sekundy
            self.last_shot_time = now
            return True
        return False

    def draw(self):
        """
        Rysuje przeciwnika na ekranie w bieżącej pozycji.

        Returns:
            None
        """
        self.screen.blit(self.image, (self.x, self.y))

    @property
    def rect(self):
        """
        Zwraca prostokąt reprezentujący przeciwnika, używany do wykrywania kolizji z pociskami.

        Returns:
            pygame.Rect: Prostokąt odpowiadający położeniu i wymiarom przeciwnika.
        """
        return pygame.Rect(self.x, self.y, ENEMY_WIDTH, ENEMY_HEIGHT)
