import pygame
from game.constants import SCREEN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.y = 500
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.x += self.speed

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
