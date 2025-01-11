import pygame
from game.constants import SCREEN_WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT

class Player:
    def __init__(self, screen):
        """
        Inicjalizuje gracza z grafiką, pozycją początkową i prędkością ruchu.

        Args:
            screen: Powierzchnia, na której gracz jest rysowany.
        """
        self.screen = screen
        self.image = pygame.image.load("assets/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.x = SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2
        self.y = 500
        self.speed = 5

    def update(self):
        """
        Aktualizuje pozycję gracza na podstawie wciśniętych klawiszy, ograniczając ruch do granic ekranu.

        Returns:
            None
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.x += self.speed

    def draw(self):
        """
        Rysuje statek gracza na ekranie w bieżącej pozycji.

        Returns:
            None
        """
        self.screen.blit(self.image, (self.x, self.y))

    @property
    def rect(self):
        """
        Zwraca prostokąt reprezentujący gracza, używany do wykrywania kolizji z pociskami.

        Returns:
            pygame.Rect: Prostokąt odpowiadający położeniu i wymiarom gracza.
        """
        return pygame.Rect(self.x, self.y, PLAYER_WIDTH, PLAYER_HEIGHT)
