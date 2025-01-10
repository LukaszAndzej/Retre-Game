import pygame
from game.constants import BULLET_WIDTH, BULLET_HEIGHT

class Bullet:
    def __init__(self, screen, x, y, direction=-1):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 7
        self.direction = direction  # Kierunek pocisku: -1 (w górę), 1 (w dół)

    def update(self):
        self.y += self.speed * self.direction

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 0) if self.direction == -1 else (255, 0, 0),
                         (self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT))

    def is_on_screen(self):
        return 0 <= self.y <= 600

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT)
