
import pygame
import random

def room_typeees(x): #NEOPRAVOVAT NAZEV JINAK SE TO POJEBE, dik :D
    prekazky = {}
    prekazky_1 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_2 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_3 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_4 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_5 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_6 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    prekazky_7 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    basic = pygame.image.load("nakres_dvery.png")
    themes = [basic]
    theme = random.choice(themes)
    if random.random() < 1:
        for i in len(prekazky_1):
            prekazky_1 = {1: [50, 50, WIDTH, HEIGHT]}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_2):
            prekazky_2 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_3):
            prekazky_3 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_4):
            prekazky_4 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_5):
            prekazky_5 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_6):
            prekazky_6 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])
    elif random.random() < 1:
        for i in len(prekazky_7):
            prekazky_7 = {}
            if  random.random() < 1:
                prekazky.append(prekazky_1[i])

    return theme, prekazky  

def room_types():
    prekazky = {}
    basic = pygame.image.load("nakres_dveri.png")
    advanted = pygame.image.load("pozadi.png")
    themes = [basic, advanted]
    room_image = random.choice(themes)
    

    return room_image