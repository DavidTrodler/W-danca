import pygame
import random
import sys

# Inicializace Pygame
pygame.init()

# Velikost okna
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Room Generator")

# Hlavní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Definice funkcí room_typeees a room_types (vloženo sem)
    def room_typeees():
        prekazky = []
        prekazky_1 = {0: [0, 0, 50, 50], 1: [0, 0, 50, 50], 2: [0, 0, 50, 50]}
        prekazky_2 = {0: [0, 0, 50, 50], 1: [0, 0, 50, 50], 2: [0, 0, 50, 50]}
        prekazky_3 = {0: [0, 0, 50, 50], 1: [0, 0, 50, 50], 2: [0, 0, 50, 50]}
        prekazky_4 = {0: [0, 0, 50, 50], 1: [0, 0, 50, 50], 2: [0, 0, 50, 50]}
        prekazky_5 = {0: [0, 0, 50, 50], 1: [0, 0, 50, 50], 2: [0, 0, 50, 50]}
        prekazky_6 = {0: [40, 170, 50, 50], 1: [90, 170, 50, 50], 2: [40, 382, 50, 50], 3: [90, 382, 50, 50], 4: [374, 40, 50, 50], 5: [374, 90, 50, 50], 6: [374, 511, 50, 50], 7: [374, 461, 50, 50], 8: [860, 170, 50, 50], 9: [910, 170, 50, 50], 10: [860, 382, 50, 50], 11: [910, 382, 50, 50], 12: [579, 40, 50, 50], 13: [579, 90, 50, 50], 14: [579, 511, 50, 50], 15: [579, 461, 50, 50], 16: [475, 275, 50, 50], 17: [525, 275, 50, 50], 18: [475, 225, 50, 50], 19: [425, 275, 50, 50], 20: [475, 325, 50, 50]}
        prekazky_7 = {0: [40, 40, 50, 50], 1: [90, 40, 50, 50], 2: [910, 511, 50, 50], 3: [910, 461, 50, 50], 4: [860, 511, 50, 50], 5: [40, 511, 50, 50], 6: [40,461,50,50], 7: [90, 511, 50, 50], 8: [910, 40, 50, 50], 9: [910, 90, 50, 50], 10: [860, 40, 50, 50], 11: [40, 90, 50, 50]}
        basic = pygame.image.load("nakres_dveri.png")
        themes = [basic]
        theme = random.choice(themes)
        if random.random() < 1:
            for i in prekazky_1:
                prekazky.append(prekazky_1[i])
        elif random.random() < 1:
            for i in range(len(prekazky_2)):
                prekazky_2 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_2[i])
        elif random.random() < 1:
            for i in range(len(prekazky_3)):
                prekazky_3 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_3[i])
        elif random.random() < 1:
            for i in range(len(prekazky_4)):
                prekazky_4 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_4[i])
        elif random.random() < 1:
            for i in range(len(prekazky_5)):
                prekazky_5 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_5[i])
        elif random.random() < 1:
            for i in range(len(prekazky_6)):
                prekazky_6 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_6[i])
        elif random.random() < 1:
            for i in range(len(prekazky_7)):
                prekazky_7 = {}
                if random.random() < 1:
                    prekazky.append(prekazky_7[i])

        return theme, prekazky

    def room_types():
        prekazky = {}
        basic = pygame.image.load("nakres_dveri.png")
        advanted = pygame.image.load("pozadi.png")
        themes = [basic, advanted]
        room_image = random.choice(themes)

        return room_image

    # Generování místnosti a překážek
    theme, obstacles = room_typeees()

    # Kreslení motivu místnosti
    screen.blit(theme, (0, 0))

    # Kreslení překážek
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(obstacle))

    pygame.display.flip()

    # Nastavení FPS (např. 1 FPS, aby bylo vidět generování místností)
    pygame.time.Clock().tick(1)
