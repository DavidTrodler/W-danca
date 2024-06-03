import pygame
import random

def room_typeees(): #NEOPRAVOVAT NAZEV JINAK SE TO POJEBE, dik :D
    prekazky = []
    prekazky_1 = {0: [730, 155, 680, 205, 780, 205, 730, 255], 1: [250, 300, 200, 350, 250, 400, 300, 350]}
    prekazky_2 = {0: [40, 200, 90, 200, 140, 200, 190, 200, 240, 200, 910, 200, 860, 200, 810, 200, 760, 200, 710, 200, 40, 350, 90, 350, 140, 350, 190, 350, 240, 350, 910, 350, 860, 350, 810, 350, 760, 350, 710, 350], 1: [400, 40, 400, 90, 400, 140, 550, 510, 550, 460, 550, 410, 400, 510, 400, 460, 400, 410, 550, 40, 550, 90, 550, 140]}
    prekazky_3 = {0: [475, 225, 525, 275, 425, 275, 475, 325], 1: [475, 175, 425, 225, 375, 275, 425, 325, 475, 375, 575, 275, 525, 225, 525, 325]}
    prekazky_4 = {0: [221, 410], 1: [151, 126], 2: [782, 128], 3: [477, 132], 4: [369, 285], 5: [720, 435], 6: [730, 267], 7: [527, 410]}
    prekazky_5 = {0: [140, 90, 140, 140, 140, 190, 140, 240, 140, 290, 140, 340, 140, 390, 140, 440, 190, 275, 240, 275, 290, 275, 340, 275], 1: [810, 275, 760, 275, 710, 275, 660, 275, 610, 275, 810, 225, 810, 175, 810, 125, 810, 275, 810, 325, 810, 375, 810, 425, 810, 90, 810, 440]}
    prekazky_6 = {0: [40, 150, 90, 150, 910, 150, 860, 150, 40, 400, 90, 400, 860, 400, 910, 400], 1: [350, 40, 350, 90, 350, 511, 350, 461, 579, 40, 579, 90, 579, 511, 579, 461], 2: [475, 275, 525, 275, 475, 225, 425, 275, 475, 325]}
    prekazky_7 = {0: [40, 40, 90, 40, 40, 90], 1: [910, 511, 910, 461, 860, 511], 2: [40, 511, 40, 461, 90, 511], 3: [910, 40, 910, 90, 860, 40]}
    prekazky_8 = {0: [730, 155, 50, 50], 1: [680, 205, 50, 50], 2: [780, 205, 50, 50], 3: [730, 255, 50, 50], 4: [250, 300, 50, 50], 5: [200, 350, 50, 50], 6: [250, 400, 50, 50], 7: [300, 350, 50, 50]}
    WIDTH, HEIGHT = 1000, 600
    basic = pygame.image.load("nakres_dveri.png")
    advanted = pygame.image.load("pozadi.png")
    basic = pygame.transform.scale(basic,(WIDTH, HEIGHT))
    advanted = pygame.transform.scale(advanted,(WIDTH, HEIGHT))
    images = [basic, advanted]
    theme = random.choice(images)

    random_int = random.randint(1, 8)

    if random_int == 1:
        keys = list(prekazky_1.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_1[key]), 2):  # Iterate over pairs
                    pair = prekazky_1[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky
    elif random_int == 2:
        keys = list(prekazky_2.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_2[key]), 2):  # Iterate over pairs
                    pair = prekazky_2[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky
    elif random_int == 3:
        keys = list(prekazky_3.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_3[key]), 2):  # Iterate over pairs
                    pair = prekazky_3[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky
    elif random_int == 4:
        keys = list(prekazky_4.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_4[key]), 2):  # Iterate over pairs
                    pair = prekazky_4[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky
    elif random_int == 5:
        keys = list(prekazky_5.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_5[key]), 2):  # Iterate over pairs
                    pair = prekazky_5[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky
    elif random_int == 6:
        keys = list(prekazky_6.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_6[key]), 2):  # Iterate over pairs
                    pair = prekazky_6[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky

    elif random_int == 7:
        keys = list(prekazky_7.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_7[key]), 2):  # Iterate over pairs
                    pair = prekazky_7[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky

    elif random_int == 8:
        keys = list(prekazky_8.keys()) 
        for i in range(len(keys)):
            if random.randint(1,3) == 1:
                key = keys[i]
                for i in range(0, len(prekazky_8[key]), 2):  # Iterate over pairs
                    pair = prekazky_8[key][i:i+2]  # Get the pair
                    pair.append(random.randint(1, 5))  # Add a random number to the pair
                    prekazky.extend(pair)  # Add the pair to prekazky    
    
    else:
        return theme

    print(prekazky)
    return theme, prekazky  



rooms = {0:[],1:[],2:[],3:[]}

def room_typesss(x):
    


    slovnik = {}
    for i in range(len(x)):
        slovnik[x[i]] = x[i]

    for key in x:
        result = room_typeees()
        theme, prekazky = result
        slovnik[key] = {"theme": theme, "prekazky": prekazky}

    return slovnik




def room_types():
    basic = pygame.image.load("nakres_dveri.png")
    advanted = pygame.image.load("pozadi.png")
    themes = [basic, advanted]
    room_image = random.choice(themes)
    

    return room_image


room_typeees()