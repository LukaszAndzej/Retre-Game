# Space Invaders - Python Game

## Opis Projektu

Space Invaders to klasyczna gra w stylu retro stworzona w Pythonie przy użyciu biblioteki Pygame. Gracz steruje statkiem kosmicznym, strzela do przeciwników i unika ich pocisków. Gra kończy się, gdy gracz straci wszystkie życia.

---

## Wymagania

Aby uruchomić grę, musisz zainstalować:

1. **Python**: wersja 3.7 lub nowsza.
2. **Pygame**: biblioteka do tworzenia gier 2D.

### Instalacja Pygame

#### Instalacja globalna:
```bash
pip install pygame
```

#### Instalacja w wirtualnym środowisku (zalecane):
1. Utwórz środowisko wirtualne:
   ```bash
   python -m venv venv
   ```
2. Aktywuj środowisko:
   - Windows (cmd):
     ```bash
     venv\Scripts\activate
     ```
   - Windows (PowerShell):
     ```bash
     .\venv\Scripts\Activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```
3. Zainstaluj Pygame:
   ```bash
   pip install pygame
   ```

### Sprawdzenie instalacji Pygame
Upewnij się, że Pygame jest zainstalowane:
```bash
pip show pygame
```

---

## Instrukcja Uruchamiania

1. Upewnij się, że wszystkie wymagania są zainstalowane.
2. Pobierz projekt lub sklonuj repozytorium:
   ```bash
   git clone <url-repozytorium>
   cd space_invaders
   ```
3. Uruchom grę:
   ```bash
   python main.py
   ```

---

## Sterowanie

- **Strzał w lewo**: Strzałki w lewo (`←`)
- **Strzał w prawo**: Strzałki w prawo (`→`)
- **Strzał**: Spacja (`Space`)
- **Wyjście z gry**: Kliknij `X` w oknie gry

---

## Zasady Gry

1. **Cel gry**:
   - Zestrzel jak najwięcej przeciwników, unikając ich pocisków.
2. **Życia gracza**:
   - Gracz zaczyna z 3 życiami, reprezentowanymi przez serduszka w prawym górnym rogu.
   - Gdy przeciwnik trafi gracza, traci jedno życie.
   - Gra kończy się po utracie wszystkich żyć.
3. **Przeciwnicy**:
   - Przeciwnicy poruszają się w różnych kierunkach i strzelają czerwonymi pociskami.
4. **Poziomy**:
   - Po zestrzeleniu wszystkich przeciwników na planszy przechodzisz na kolejny poziom, gdzie liczba przeciwników rośnie.
