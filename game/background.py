import pygame
import random
from game.constants import STAR_COUNT, SCREEN_WIDTH, SCREEN_HEIGHT

class Background:
    def __init__(self, screen):
        """
        Inicjalizuje tło gry z losowo rozmieszczonymi gwiazdami.

        Args:
            screen: Powierzchnia, na której rysowane jest tło.
        """
        self.screen = screen
        self.stars = [
            [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            for _ in range(STAR_COUNT)
        ]

    def update(self):
        """
        Aktualizuje położenie gwiazd, przesuwając je w dół ekranu. Gwiazdy, które opuszczają ekran,
        pojawiają się ponownie na górze w losowej pozycji.

        Returns:
            None
        """
        for star in self.stars:
            star[1] += 1
            if star[1] > SCREEN_HEIGHT:
                star[1] = 0
                star[0] = random.randint(0, SCREEN_WIDTH)

    def draw(self):
        """
        Rysuje wszystkie gwiazdy na ekranie jako białe kółka.

        Returns:
            None
        """
        for star in self.stars:
            pygame.draw.circle(self.screen, (255, 255, 255), star, 2)
