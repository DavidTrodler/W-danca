import pygame
import random
import sys

# Inicializace Pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Room Generator")

# Definice všech sad překážek
all_obstacles = [
    {0: [40, 40, 50, 50], 1: [90, 40, 50, 50], 2: [40, 40, 50, 50], 3: [810, 485, 50, 50], 5: [115, 485, 50, 50], 6: [810, 40, 50, 50]},
    {0: [400, 400, 50, 50], 1: [500, 500, 50, 50], 2: [600, 100, 50, 50]},
    {0: [700, 200, 50, 50], 1: [100, 300, 50, 50], 2: [200, 400, 50, 50]},
    {0: [300, 500, 50, 50], 1: [400, 100, 50, 50], 2: [500, 200, 50, 50]},
    {0: [600, 300, 50, 50], 1: [700, 400, 50, 50], 2: [100, 500, 50, 50]},
    {0: [200, 600, 50, 50], 1: [300, 100, 50, 50], 2: [400, 200, 50, 50]},
    {0: [500, 300, 50, 50], 1: [600, 400, 50, 50], 2: [700, 500, 50, 50]}
]

# Vybrání jedné ze sad překážek
chosen_obstacles = random.choice(all_obstacles)

# Hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kreslení motivu místnosti
    screen.fill((255, 255, 255))  # Vyplní obrazovku bílou barvou (pokoj)

    # Kreslení překážek
    for obstacle in chosen_obstacles.values():
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(obstacle))

    pygame.display.flip()

    # Nastavení FPS (např. 1 FPS, aby bylo vidět generování místností)
    pygame.time.Clock().tick(1)
