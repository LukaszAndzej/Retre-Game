import pygame
from game.constants import BULLET_WIDTH, BULLET_HEIGHT

class Bullet:
    def __init__(self, screen, x, y, direction=-1):
        """
        Inicjalizuje pocisk z podanymi współrzędnymi (x, y), ekranem docelowym i kierunkiem ruchu.

        Args:
            screen: Powierzchnia, na której pocisk jest rysowany.
            x: Pozycja początkowa w osi X.
            y: Pozycja początkowa w osi Y.
            direction: Kierunek ruchu pocisku (-1 dla góry, 1 dla dołu).
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 7
        self.direction = direction  # Kierunek pocisku: -1 (w górę), 1 (w dół)

    def update(self):
        """
        Aktualizuje pozycję pocisku w pionie, przesuwając go zgodnie z jego kierunkiem i prędkością.

        Returns:
            None
        """
        self.y += self.speed * self.direction

    def draw(self):
        """
        Rysuje pocisk na ekranie w odpowiednim kolorze:
            - Żółty (gracz).
            - Czerwony (przeciwnik).

        Returns:
            None
        """
        pygame.draw.rect(self.screen, (255, 255, 0) if self.direction == -1 else (255, 0, 0),
                         (self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT))

    def is_on_screen(self):
        """
        Sprawdza, czy pocisk znajduje się w granicach ekranu.

        Returns:
            bool: True, jeśli pocisk znajduje się na ekranie. False, jeśli wypadł poza ekran.
        """
        return 0 <= self.y <= 600

    @property
    def rect(self):
        """
        Zwraca prostokąt reprezentujący pocisk, używany do wykrywania kolizji z innymi obiektami.

        Returns:
            pygame.Rect: Prostokąt odpowiadający położeniu i wymiarom pocisku.
        """
        return pygame.Rect(self.x, self.y, BULLET_WIDTH, BULLET_HEIGHT)
