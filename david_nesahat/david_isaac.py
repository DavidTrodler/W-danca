import pygame, sys
from rooms_vyber import rooms_fixed
pygame.init()

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)

# Define projectile size and speed
projectile_size = 10
projectile_speed = 10
projectile_speed_diagonal = 4

# Shooting cooldown
cooldown = 0
cooldown_time = 10

# Initialize lists for player projectiles and all projectiles
#UP
player_projectiles_up = []
player_projectiles_up_left = []
player_projectiles_up_right = []
#DOWN
player_projectiles_down = []
player_projectiles_down_left = []
player_projectiles_down_right = []
#LEFT
player_projectiles_left = []
player_projectiles_left_down = []
player_projectiles_left_up = []
#RIGHT
player_projectiles_right = []
player_projectiles_right_down = []
player_projectiles_right_up = []
#ALL
projectiles = []

# Create the game window + Load images
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("ˇIsaacˇ")
pozadi = pygame.image.load("pozadi.png")
pozadi = pygame.transform.scale(pozadi, (1000, 600))

window.blit(pozadi, (0, 0))

# Set initial position and dimensions for the character
rect_x, rect_y = 70, 500
WIDTH, HEIGHT = 1000, 600

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load the character and tear image
velikost_postavy = 57
postava = pygame.image.load("pixelovy_isaac_vetsi.png")
importovani_slzy = pygame.image.load("tear.png")
slza = pygame.transform.scale(importovani_slzy, (25, 25))
heart_full = pygame.image.load("srdicka/full_heart.png")
heart_half = pygame.image.load("srdicka/half_a_heart.png")

#Functions for enemies.py
"""
Start -------------- minimap_file.py
"""
image_width = 60 #x  #<---- Šířka obrázku, dá se volně měnit
image_height = 30 #y
pygame.display.set_caption("ˇIsaacˇ")
room_image = pygame.image.load("pozadi.png")
zkouzka_image = pygame.image.load("nakres_dveri.png") #<---- Zkušební obrázek pro roomku č. 1

zkouzka_image = pygame.transform.scale(zkouzka_image,(image_width,image_height))
room_image = pygame.transform.scale(room_image,(image_width,image_height))
image_filter = pygame.transform.scale(room_image,(image_width,image_height))
room_image.set_alpha(128) #průhledné 0 - 255 neprůhledné


image_filter_position = [775, 100] #<---- Pozice filtru
# Rooms list
rooms = [1]
rooms = rooms_fixed(3) #<---- Číslo = level
current_room = [1]


doors_dictionary = {0: [False, False, False, False]} #Posloupnost dveří: UP, RIGHT, BOTTOM, LEFT
for i in range(1, 50):
    doors_dictionary[i] = [False, False, False, False]

print(doors_dictionary)
print(rooms)


#Pohyby mapy
move_up = [0, 30] # y + 30
move_side = [60, 0] # x + 60
move_up_counter = 0 #<---- O kolik roomek se posunul hráč nahoru nebo dolů
move_side_counter = 0

#Dveře, ukazuje, kam se mají osy posunout
dvere_up_value = 1
dvere_down_value = -1
dvere_left_value = 1
dvere_right_value = -1

dvere_up = False #<--- Změní se, pokud hráč projde dveřmi (kvůli if statment ve while loop)
dvere_down = False 
dvere_left = False
dvere_right = False

#Funkce která určí zda budou dveře v dané roomce funkční
def rooms_dictionary_funciton():
    if 1 in rooms:
        #Čtyři
        doors_dictionary[4][2] = True
        #Pět
        doors_dictionary[5][3] = True
        #Dva
        doors_dictionary[2][0] = True
        #Tři
        doors_dictionary[3][1] = True
    if 2 in rooms:
        #Jedna
        doors_dictionary[1][2] = True
        #Šest
        doors_dictionary[6][3] = True
        #Jedenáct
        doors_dictionary[11][0] = True
        #Sedm
        doors_dictionary[7][1] = True
    if 3 in rooms:
        #Osm
        doors_dictionary[8][2] = True
        #Jedna
        doors_dictionary[1][3] = True
        #Sedm
        doors_dictionary[7][0] = True
        #Dvanáct
        doors_dictionary[12][1] = True
    if 4 in rooms:
        #Třináct
        doors_dictionary[13][2] = True
        #Devět
        doors_dictionary[9][3] = True
        #Jedna
        doors_dictionary[1][0] = True
        #Osm
        doors_dictionary[8][1] = True
    if 5 in rooms:
        #Devět
        doors_dictionary[9][2] = True
        #Deset
        doors_dictionary[10][3] = True
        #Šest
        doors_dictionary[6][0] = True
        #Jedna
        doors_dictionary[1][1] = True
    if 6 in rooms:
        #Pět
        doors_dictionary[5][2] = True
        #Šestnáct
        doors_dictionary[16][3] = True
        #Sedmnáct
        doors_dictionary[17][0] = True
        #Dva
        doors_dictionary[2][1] = True
    if 7 in rooms:
        #Tři
        doors_dictionary[3][2] = True
        #Dva
        doors_dictionary[2][3] = True
        #Osmnáct
        doors_dictionary[18][1] = True
        #Devatenáct
        doors_dictionary[19][0] = True
    if 8 in rooms:
        #Dvacetjedna
        doors_dictionary[21][2] = True
        #Čtyři
        doors_dictionary[4][3] = True
        #Tři
        doors_dictionary[3][0] = True
        #Dvacet
        doors_dictionary[20][1] = True
    if 9 in rooms:
        #Čtrnáct
        doors_dictionary[14][2] = True
        #Patnáct
        doors_dictionary[15][3] = True
        #Pět
        doors_dictionary[5][0] = True
        #Čtyři
        doors_dictionary[4][1] = True
    if 10 in rooms:
        #Patnáct
        doors_dictionary[15][2] = True
        #Dvacetsedm
        doors_dictionary[27][3] = True
        #Šestnáct
        doors_dictionary[16][0] = True
        #Pět
        doors_dictionary[5][1] = True
    if 11 in rooms:
        #Dva
        doors_dictionary[2][2] = True
        #Sedmnáct
        doors_dictionary[17][3] = True
        #Dvacetosm
        doors_dictionary[28][0] = True
        #Osmnáct
        doors_dictionary[18][1] = True
    if 12 in rooms:
        #Dvacet
        doors_dictionary[20][2] = True
        #Tři
        doors_dictionary[3][3] = True
        #Devatenáct
        doors_dictionary[19][0] = True
        #Dvacetdevět
        doors_dictionary[29][1] = True
    if 13 in rooms:
        #Dvacetšest
        doors_dictionary[26][2] = True
        #Čtrnáct
        doors_dictionary[14][3] = True
        #Čtyři
        doors_dictionary[4][0] = True
        #Dvacetjedna
        doors_dictionary[21][1] = True
    if 14 in rooms:
        #Třicetčtyři
        doors_dictionary[34][2] = True
        #Dvacetdva
        doors_dictionary[22][3] = True
        #Devět
        doors_dictionary[9][0] = True
        #Třináct
        doors_dictionary[13][1] = True
    if 15 in rooms:
        #Dvacetdva
        doors_dictionary[22][2] = True
        #Třicetsedm
        doors_dictionary[37][3] = True
        #Deset
        doors_dictionary[10][0] = True
        #Devět
        doors_dictionary[9][1] = True
    if 16 in rooms:
        #Deset
        doors_dictionary[10][2] = True
        #Třicetosm
        doors_dictionary[38][3] = True
        #Dvacettři
        doors_dictionary[23][0] = True
        #Šest
        doors_dictionary[6][1] = True
    if 17 in rooms:
        #Šest
        doors_dictionary[6][2] = True
        #Dvacettři
        doors_dictionary[23][3] = True
        #Čtyřicetjedna
        doors_dictionary[41][0] = True
        #Jedenáct
        doors_dictionary[11][1] = True
    if 18 in rooms:
        #Sedm
        doors_dictionary[7][2] = True
        #Jedenáct
        doors_dictionary[11][3] = True
        #Čtyřicetdva
        doors_dictionary[42][0] = True
        #Dvacetčtyři
        doors_dictionary[24][1] = True
    if 19 in rooms:
        #Dvanáct
        doors_dictionary[12][2] = True
        #Sedm
        doors_dictionary[7][3] = True
        #Dvacetčtyři
        doors_dictionary[24][0] = True
        #Čtyřicetpět
        doors_dictionary[45][1] = True
    if 20 in rooms:
        #Dvacetpět
        doors_dictionary[25][2] = True
        #Osm
        doors_dictionary[8][3] = True
        #Dvanáct
        doors_dictionary[12][0] = True
        #Třicet
        doors_dictionary[30][1] = True
    if 21 in rooms:
        #Třicettři
        doors_dictionary[33][2] = True
        #Třináct
        






def pohyby_mapy():
    # Room numbers
    #První
    prvni = [775 , 100] #POKUD CHCEŠ ZMĚNIT UMÍSTĚNÍ MAPY, ZMĚŇ UMÍSTĚNÍ PRVNÍ ROOMKY   
                #---Pokračuje na konci funkce---

    #Druhá
    druha = [0,0]
    druha[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    #<-----Posune se ošířku obrázku (image_width) do boku, násobí se podle závislosti na roomce č. jedna. (viz excell)
    druha[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Třetí
    treti = [0,0]
    treti[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    treti[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Čtvrtá
    ctvrta = [0,0]
    ctvrta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    ctvrta[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Pátá
    pata = [0,0]
    pata[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    pata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Šestá
    sesta = [0,0]
    sesta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    sesta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Sedmá
    sedma = [0,0]
    sedma[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    sedma[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Osmá
    osma = [0,0]
    osma[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    osma[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Devátá
    devata = [0,0]
    devata[0] = prvni[0] + (image_width * 1) + (move_side[0] * move_side_counter)
    devata[1] = prvni[1] + (image_height * (-1)) + (move_up[1] * move_up_counter)
    print(devata)
    #Desátá   x     y
    desata = [0,0]
    desata[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    desata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Jedenáctá
    jedenacta = [0,0]
    jedenacta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    jedenacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvanáctá
    dvanacta = [0,0]
    dvanacta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvanacta[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Třináctá
    trinacta = [0,0]
    trinacta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    trinacta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Čtrnáctá   x    y 
    ctrnacta = [0,0]
    ctrnacta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    ctrnacta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Patnáctá
    patnacta = [0,0]
    patnacta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    patnacta[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Šestnáctá
    sestnacta = [0,0]
    sestnacta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    sestnacta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Sedmnáctá
    sedmnacta = [0,0]
    sedmnacta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    sedmnacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Osmnáctá
    osmnacta = [0,0]
    osmnacta[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    osmnacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Devatenáctá
    devatenacta = [0,0]
    devatenacta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    devatenacta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Dvacátá
    dvacata = [0,0]
    dvacata[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacata[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Dvacátá první
    dvacataprvni = [0,0]
    dvacataprvni[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    dvacataprvni[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá druhá
    dvacatadruha = [0,0]
    dvacatadruha[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    dvacatadruha[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá třetí
    dvacatatreti = [0,0]
    dvacatatreti[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    dvacatatreti[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvacátá čtvrtá
    dvacatactvrta = [0,0]
    dvacatactvrta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacatactvrta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvacátá pátá
    dvacatapata = [0,0]
    dvacatapata[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacatapata[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá šestá
    dvacatasesta = [0,0]
    dvacatasesta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    dvacatasesta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Dvacátá sedmá
    dvacatasedma = [0,0]
    dvacatasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    dvacatasedma[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Dvacátá osmá
    dvacataosma = [0,0]
    dvacataosma[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    dvacataosma[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Dvacátá devátá
    dvacatadevata = [0,0]
    dvacatadevata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    dvacatadevata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Třicátá
    tricata = [0,0]
    tricata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    tricata[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Třicátá první
    tricataprvni = [0,0]
    tricataprvni[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    tricataprvni[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Třicátá druhá
    tricatadruha = [0,0]
    tricatadruha[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    tricatadruha[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá třetí
    tricatatreti = [0,0]
    tricatatreti[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    tricatatreti[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá čtvrtá
    tricatactvrta = [0,0]
    tricatactvrta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    tricatactvrta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá pátá
    tricatapata = [0,0]
    tricatapata[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    tricatapata[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá šestá
    tricatasesta = [0,0]
    tricatasesta[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatasesta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Třicátá sedmá
    tricatasedma = [0,0]
    tricatasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatasedma[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Třicátá osmá
    tricataosma = [0,0]
    tricataosma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricataosma[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Třicátá devátá
    tricatadevata = [0,0]
    tricatadevata[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatadevata[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Čtyřicátá
    ctyracta = [0,0]
    ctyracta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    ctyracta[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá první
    ctyractaprvni = [0,0]
    ctyractaprvni[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    ctyractaprvni[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá druhá
    ctyractadruha = [0,0]
    ctyractadruha[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    ctyractadruha[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá třetí
    ctyratatreti = [0,0]
    ctyratatreti[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    ctyratatreti[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá čtvrtá
    ctyratactvrta = [0,0]
    ctyratactvrta[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratactvrta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Čtyřicátá pátá
    ctyratapata = [0,0]
    ctyratapata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratapata[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Čtyřicátá šestá
    ctyratasesta = [0,0]
    ctyratasesta[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratasesta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Čtyřicátá sedmá
    ctyratasedma = [0,0]
    ctyratasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    ctyratasedma[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Čtyřicátá osmá
    ctyrataosma = [0,0]
    ctyrataosma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    ctyrataosma[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá devátá
    ctyratadevata = [0,0]
    ctyratadevata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratadevata[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)
    

    # Zase první
    prvni[0] = prvni[0] + (move_side[0] * move_side_counter)
    prvni[1] = prvni[1] + (move_up[1] * move_up_counter)
    return prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata



prvni_statement = True #<----- indikuje, jesli je dané číslo v seznamu rooms
druha_statement = False
treti_statement = False
ctvrta_statement = False
pata_statement = False
sesta_statement = False
sedma_statement = False
osma_statement = False
devata_statement = False
desata_statement = False
jedenacta_statement = False
dvanacta_statement = False
trinacta_statement = False
ctrnacta_statement = False
patnacta_statement = False
sestnacta_statement = False
sedmnacta_statement = False
osmnacta_statement = False
devatenacta_statement = False
dvacata_statement = False
dvacataprvni_statement = False
dvacatadruha_statement = False
dvacatatreti_statement = False
dvacatactvrta_statement = False
dvacatapata_statement = False
dvacatasesta_statement = False
dvacatasedma_statement = False
dvacataosma_statement = False
dvacatadevata_statement = False
tricata_statement = False
tricataprvni_statement = False
tricatadruha_statement = False
tricatatreti_statement = False
tricatactvrta_statement = False
tricatapata_statement = False
tricatasesta_statement = False
tricatasedma_statement = False
tricataosma_statement = False
tricatadevata_statement = False
ctyracta_statement = False
ctyractaprvni_statement = False
ctyractadruha_statement = False
ctyratatreti_statement = False
ctyratactvrta_statement = False
ctyratapata_statement = False
ctyratasesta_statement = False
ctyratasedma_statement = False
ctyrataosma_statement = False
ctyratadevata_statement = False

prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()


if 2 in rooms:
    druha_statement = True 
if 3 in rooms:
    treti_statement = True
if 4 in rooms:
    ctvrta_statement = True
if 5 in rooms:
    pata_statement = True
if 6 in rooms:
    sesta_statement = True
if 7 in rooms:
    sedma_statement = True
if 8 in rooms:
    osma_statement = True
if 9 in rooms:
    devata_statement = True
if 10 in rooms:
    desata_statement = True
if 11 in rooms:
    jedenacta_statement = True
if 12 in rooms:
    dvanacta_statement = True
if 13 in rooms:
    trinacta_statement = True
if 14 in rooms:
    ctrnacta_statement = True
if 15 in rooms:
    patnacta_statement = True
if 16 in rooms:
    sestnacta_statement = True
if 17 in rooms:
    sedmnacta_statement = True
if 18 in rooms:
    osmnacta_statement = True
if 19 in rooms:
    devatenacta_statement = True
if 20 in rooms:
    dvacata_statement = True
if 21 in rooms:
    dvacataprvni_statement = True
if 22 in rooms:
    dvacatadruha_statement = True
if 23 in rooms:
    dvacatatreti_statement = True
if 24 in rooms:
    dvacatactvrta_statement = True
if 25 in rooms:
    dvacatapata_statement = True
if 26 in rooms:
    dvacatasesta_statement = True
if 27 in rooms:
    dvacatasedma_statement = True
if 28 in rooms:
    dvacataosma_statement = True
if 29 in rooms:
    dvacatadevata_statement = True
if 30 in rooms:
    tricata_statement = True
if 31 in rooms:
    tricataprvni_statement = True
if 32 in rooms:
    tricatadruha_statement = True
if 33 in rooms:
    tricatatreti_statement = True
if 34 in rooms:
    tricatactvrta_statement = True
if 35 in rooms:
    tricatapata_statement = True
if 36 in rooms:
    tricatasesta_statement = True
if 37 in rooms:
    tricatasedma_statement = True
if 38 in rooms:
    tricataosma_statement = True
if 39 in rooms:
    tricatadevata_statement = True
if 40 in rooms:
    ctyracta_statement = True
if 41 in rooms:
    ctyractaprvni_statement = True
if 42 in rooms:
    ctyractadruha_statement = True
if 43 in rooms:
    ctyratatreti_statement = True
if 44 in rooms:
    ctyratactvrta_statement = True
if 45 in rooms:
    ctyratapata_statement = True
if 46 in rooms:
    ctyratasesta_statement = True
if 47 in rooms:
    ctyratasedma_statement = True
if 48 in rooms:
    ctyrataosma_statement = True
if 49 in rooms:
    ctyratadevata_statement = True

pohyby_mapy()
"""
End -------------- minimap_file.py
"""

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #UP
            if event.key == pygame.K_UP and not keys[pygame.K_a] and not keys[pygame.K_d] and shoots == False:
                player_projectiles_up.append((rect_x + velikost_postavy // 2, rect_y))
                cooldown = cooldown_time
                break
            #UP_LEFT
            elif event.key == pygame.K_UP and keys[pygame.K_a] and not keys[pygame.K_d] and shoots == False:
                player_projectiles_up_left.append((rect_x + velikost_postavy // 2, rect_y))
                cooldown = cooldown_time
                break
            #UP_RIGHT
            elif event.key == pygame.K_UP and keys[pygame.K_d] and not keys[pygame.K_a] and shoots == False:
                player_projectiles_up_right.append((rect_x + velikost_postavy // 2, rect_y))
                cooldown = cooldown_time
                break

            #DOWN
            elif event.key == pygame.K_DOWN and not keys[pygame.K_a] and not keys[pygame.K_d] and shoots == False:
                player_projectiles_down.append((rect_x + velikost_postavy // 2, rect_y + 46))
                cooldown = cooldown_time  
                break
            #DOWN_LEFT
            elif event.key == pygame.K_DOWN and keys[pygame.K_a] and not keys[pygame.K_d] and shoots == False:
                player_projectiles_down_left.append((rect_x + velikost_postavy // 2, rect_y + 46))
                cooldown = cooldown_time
                break
            #DOWN_RIGHT
            elif event.key == pygame.K_DOWN and keys[pygame.K_d] and not keys[pygame.K_a] and shoots == False:
                player_projectiles_down_right.append((rect_x + velikost_postavy // 2, rect_y + 46))
                cooldown = cooldown_time
                break

            #LEFT
            elif event.key == pygame.K_LEFT and not keys[pygame.K_w] and not keys[pygame.K_s] and shoots == False:
                player_projectiles_left.append((rect_x - 2, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #LEFT_DOWN
            elif event.key == pygame.K_LEFT and keys[pygame.K_s] and not keys[pygame.K_w] and shoots == False:
                player_projectiles_left_down.append((rect_x - 2, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #LEFT_UP
            elif event.key == pygame.K_LEFT and keys[pygame.K_w] and not keys[pygame.K_s] and shoots == False:
                player_projectiles_left_up.append((rect_x - 2, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #RIGHT
            elif event.key == pygame.K_RIGHT and not keys[pygame.K_w] and not keys[pygame.K_s] and shoots == False:
                player_projectiles_right.append((rect_x + 52, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #RIGHT_DOWN
            elif event.key == pygame.K_RIGHT and keys[pygame.K_s] and not keys[pygame.K_w] and shoots == False:
                player_projectiles_right_down.append((rect_x + 52, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #RIGHT_UP
            elif event.key == pygame.K_RIGHT and keys[pygame.K_w] and not keys[pygame.K_s] and shoots == False:
                player_projectiles_right_up.append((rect_x + 52, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break

    if cooldown > 0:
        cooldown -= 1
        shoots = True
    if cooldown == 0:
        shoots = False


    # DOČASNĚ ZAKOMENTOVÁNO
    """
    Start -------------- minimap_file.py
    
    # Jestliže jsou aktivovány dveře
    if dvere_up:
        move_up_counter += dvere_up_value
        dvere_up = False
    elif dvere_down:
        move_up_counter += dvere_down_value
        dvere_down = False
    elif dvere_left:
        move_side_counter += dvere_left_value
        dvere_left = False
    elif dvere_right:
        move_side_counter += dvere_right_value
        dvere_right = False
    
    End -------------- minimap_file.py
    """
    keys = pygame.key.get_pressed()

    # Move the character based on the pressed keys
    if keys[pygame.K_a]:
        rect_x -= 5
    if keys[pygame.K_d]:
        rect_x += 5
    if keys[pygame.K_w]:
        rect_y -= 5
    if keys[pygame.K_s]:
        rect_y += 5

    # Update the position of player projectiles
    #UP
    new_player_projectiles_UP = []
    new_player_projectiles_UP_LEFT = []
    new_player_projectiles_UP_RIGHT = []
    #DOWN
    new_player_projectiles_DOWN = []
    new_player_projectiles_DOWN_LEFT = []
    new_player_projectiles_DOWN_RIGHT = []
    #LEFT
    new_player_projectiles_LEFT = []
    new_player_projectiles_LEFT_DOWN = []
    new_player_projectiles_LEFT_UP = []
    #RIGHT
    new_player_projectiles_RIGHT = []
    new_player_projectiles_RIGHT_DOWN = []
    new_player_projectiles_RIGHT_UP = []

    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            proj_y -= projectile_speed
            if proj_y > 0:
                new_player_projectiles_UP.append((proj_x, proj_y))
        player_projectiles_up = new_player_projectiles_UP
    #UP_LEFT
    if len(player_projectiles_up_left) > 0:
        for proj_x, proj_y in player_projectiles_up_left:
            proj_y -= projectile_speed
            proj_x -= projectile_speed_diagonal
            if proj_y > 0 or proj_x > 0:
                new_player_projectiles_UP_LEFT.append((proj_x, proj_y))
        player_projectiles_up_left = new_player_projectiles_UP_LEFT
    #UP_RIGHT
    if len(player_projectiles_up_right) > 0:
        for proj_x, proj_y in player_projectiles_up_right:
            proj_y -= projectile_speed
            proj_x += projectile_speed_diagonal
            if proj_y > 0 or proj_x < WIDTH:
                new_player_projectiles_UP_RIGHT.append((proj_x, proj_y))
        player_projectiles_up_right = new_player_projectiles_UP_RIGHT

    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            proj_y += projectile_speed
            if proj_y < HEIGHT:
                new_player_projectiles_DOWN.append((proj_x, proj_y))
        player_projectiles_down = new_player_projectiles_DOWN
    #DOWN_LEFT
    if len(player_projectiles_down_left) > 0:
        for proj_x, proj_y in player_projectiles_down_left:
            proj_y += projectile_speed
            proj_x -= projectile_speed_diagonal
            if proj_y < HEIGHT or proj_x < 0:
                new_player_projectiles_DOWN_LEFT.append((proj_x, proj_y))
        player_projectiles_down_left = new_player_projectiles_DOWN_LEFT
    #DOWN_RIGHT
    if len(player_projectiles_down_right) > 0:
        for proj_x, proj_y in player_projectiles_down_right:
            proj_y += projectile_speed
            proj_x += projectile_speed_diagonal
            if proj_y < HEIGHT or proj_x < WIDTH:
                new_player_projectiles_DOWN_RIGHT.append((proj_x, proj_y))
        player_projectiles_down_right = new_player_projectiles_DOWN_RIGHT
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            proj_x -= projectile_speed
            if proj_x > 0:
                new_player_projectiles_LEFT.append((proj_x, proj_y))
        player_projectiles_left = new_player_projectiles_LEFT
    #LEFT_DOWN
    if len(player_projectiles_left_down) > 0:
        for proj_x, proj_y in player_projectiles_left_down:
            proj_x -= projectile_speed
            proj_y += projectile_speed_diagonal
            if proj_x > 0 or proj_y < HEIGHT:
                new_player_projectiles_LEFT_DOWN.append((proj_x, proj_y))
        player_projectiles_left_down = new_player_projectiles_LEFT_DOWN
    #LEFT_UP
    if len(player_projectiles_left_up) > 0:
        for proj_x, proj_y in player_projectiles_left_up:
            proj_x -= projectile_speed
            proj_y -= projectile_speed_diagonal
            if proj_x > 0 or proj_y > 0:
                new_player_projectiles_LEFT_UP.append((proj_x, proj_y))
        player_projectiles_left_up = new_player_projectiles_LEFT_UP
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            proj_x += projectile_speed
            if proj_x < WIDTH:
                new_player_projectiles_RIGHT.append((proj_x, proj_y))
        player_projectiles_right = new_player_projectiles_RIGHT
    #RIGHT_DOWN
    if len(player_projectiles_right_down) > 0:
        for proj_x, proj_y in player_projectiles_right_down:
            proj_x += projectile_speed
            proj_y += projectile_speed_diagonal
            if proj_x < WIDTH or proj_y < HEIGHT:
                new_player_projectiles_RIGHT_DOWN.append((proj_x, proj_y))
        player_projectiles_right_down = new_player_projectiles_RIGHT_DOWN
    #RIGHT_UP
    if len(player_projectiles_right_up) > 0:
        for proj_x, proj_y in player_projectiles_right_up:
            proj_x += projectile_speed
            proj_y -= projectile_speed_diagonal
            if proj_x < WIDTH or proj_y > 0:
                new_player_projectiles_RIGHT_UP.append((proj_x, proj_y))
        player_projectiles_right_up = new_player_projectiles_RIGHT_UP


    # Vykreslení pozadí
    window.blit(pozadi, (0,0))
    window.blit(image_filter, (image_filter_position))
    
    # Draw player projectiles on the window
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #UP_LEFT
    if len(player_projectiles_up_left) > 0:
        for proj_x, proj_y in player_projectiles_up_left:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #UP_RIGHT
    if len(player_projectiles_up_right) > 0:
        for proj_x, proj_y in player_projectiles_up_right:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN_LEFT
    if len(player_projectiles_down_left) > 0:
        for proj_x, proj_y in player_projectiles_down_left:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN_RIGHT
    if len(player_projectiles_down_right) > 0:
        for proj_x, proj_y in player_projectiles_down_right:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #LEFT_DOWN
    if len(player_projectiles_left_down) > 0:
        for proj_x, proj_y in player_projectiles_left_down:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #LEFT_UP
    if len(player_projectiles_left_up) > 0:
        for proj_x, proj_y in player_projectiles_left_up:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #RIGHT_DOWN
    if len(player_projectiles_right_down) > 0:
        for proj_x, proj_y in player_projectiles_right_down:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #RIGHT_UP
    if len(player_projectiles_right_up) > 0:
        for proj_x, proj_y in player_projectiles_right_up:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))



    # DOČASNĚ ZAKOMENTOVÁNO
    """
    # Ensure the character stays within the window boundaries
    rect_x = max(45, min(rect_x, WIDTH - 100))
    rect_y = max(45, min(rect_y, HEIGHT - 100))
    """

    # Draw the character and hearts on the window
    isaac = window.blit(postava, (rect_x, rect_y))
    
    """
    Start -------------- minimap_file.py
    """
    # Vykreslení mapy
    #První
    if prvni_statement: #<---- pokud je 1. roomka v seznamu rooms, bude True
        for img_x, img_y in [prvni]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0: #<----- pouze, aby se nezobrazovaly mimo obrazovku
                window.blit(room_image, (prvni))
    #Druhá
    if druha_statement:
        for img_x, img_y in [druha]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((druha)))
    #Třetí
    if treti_statement:
        for img_x, img_y in [treti]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((treti)))
    #Čtvrtá
    if ctvrta_statement:
        for img_x, img_y in [ctvrta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((ctvrta)))
    #Pátá
    if pata_statement:
        for img_x, img_y in [pata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((pata)))
    #Šestá
    if sesta_statement:
        for img_x, img_y in [sesta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((sesta))) 
    #Sedmá
    if sedma_statement:
        for img_x, img_y in [sedma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((sedma)))
    #Osmá
    if osma_statement:
        for img_x, img_y in [osma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, ((osma)))
    #Devátá
    if devata_statement:
        for img_x, img_y in [devata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (devata))
    #Desátá
    if desata_statement:
        for img_x, img_y in [desata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (desata))
    #Jedenáctá
    if jedenacta_statement:
        for img_x, img_y in [jedenacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (jedenacta))
    #Dvanáctá
    if dvanacta_statement:
        for img_x, img_y in [dvanacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvanacta))
    #Třináctá
    if trinacta_statement:
        for img_x, img_y in [trinacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (trinacta))
    #Čtrnáctá
    if ctrnacta_statement:
        for img_x, img_y in [ctrnacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctrnacta))
    #Patnáctá
    if patnacta_statement:
        for img_x, img_y in [patnacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (patnacta))
    #Šestnáctá
    if sestnacta_statement:
        for img_x, img_y in [sestnacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (sestnacta))
    #Sedmnáctá
    if sedmnacta_statement:
        for img_x, img_y in [sedmnacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (sedmnacta))
    #Osmnáctá
    if osmnacta_statement:
        for img_x, img_y in [osmnacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (osmnacta))
    #Devatenáctá
    if devatenacta_statement:
        for img_x, img_y in [devatenacta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (devatenacta))
    #Dvacátá
    if dvacata_statement:
        for img_x, img_y in [dvacata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacata))
    #Dvacátá první
    if dvacataprvni_statement:
        for img_x, img_y in [dvacataprvni]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacataprvni))
    #Dvacátá druhá
    if dvacatadruha_statement:
        for img_x, img_y in [dvacatadruha]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatadruha))
    #Dvacátá třetí
    if dvacatatreti_statement:
        for img_x, img_y in [dvacatatreti]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatatreti))
    #Dvacátá čtvrtá
    if dvacatactvrta_statement:
        for img_x, img_y in [dvacatactvrta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatactvrta))
    #Dvacátá pátá
    if dvacatapata_statement:
        for img_x, img_y in [dvacatapata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatapata))
    #Dvacátá šestá
    if dvacatasesta_statement:
        for img_x, img_y in [dvacatasesta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatasesta))
    #Dvacátá sedmá
    if dvacatasedma_statement:
        for img_x, img_y in [dvacatasedma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatasedma))
    #Dvacátá osmá
    if dvacataosma_statement:
        for img_x, img_y in [dvacataosma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacataosma))
    #Dvacátá devátá
    if dvacatadevata_statement:
        for img_x, img_y in [dvacatadevata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (dvacatadevata))
    #Třicátá
    if tricata_statement:
        for img_x, img_y in [tricata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricata))
    #Třicátá první
    if tricataprvni_statement:
        for img_x, img_y in [tricataprvni]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricataprvni))
    #Třicátá druhá
    if tricatadruha_statement:
        for img_x, img_y in [tricatadruha]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatadruha))
    #Třicátá třetí
    if tricatatreti_statement:
        for img_x, img_y in [tricatatreti]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatatreti))
    #Třicátá čtvrtá
    if tricatactvrta_statement:
        for img_x, img_y in [tricatactvrta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatactvrta))
    #Třicátá pátá
    if tricatapata_statement:
        for img_x, img_y in [tricatapata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatapata))
    #Třicátá šestá
    if tricatasesta_statement:
        for img_x, img_y in [tricatasesta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatasesta))
    #Třicátá sedmá
    if tricatasedma_statement:
        for img_x, img_y in [tricatasedma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatasedma))
    #Třicátá osmá
    if tricataosma_statement:
        for img_x, img_y in [tricataosma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricataosma))
    #Třicátá devátá
    if tricatadevata_statement:
        for img_x, img_y in [tricatadevata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (tricatadevata))
    #Čtyřicátá
    if ctyracta_statement:
        for img_x, img_y in [ctyracta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyracta))
    #Čtyřicátá první
    if ctyractaprvni_statement:
        for img_x, img_y in [ctyractaprvni]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyractaprvni))
    #Čtyřicátá druhá
    if ctyractadruha_statement:
        for img_x, img_y in [ctyractadruha]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyractadruha))
    #Čtyřicátá třetí
    if ctyratatreti_statement:
        for img_x, img_y in [ctyratatreti]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratatreti))
    #Čtyřicátá čtvrtá
    if ctyratactvrta_statement:
        for img_x, img_y in [ctyratactvrta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratactvrta))
    #Čtyřicátá pátá
    if ctyratapata_statement:
        for img_x, img_y in [ctyratapata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratapata))
    #Čtyřicátá šestá
    if ctyratasesta_statement:
        for img_x, img_y in [ctyratasesta]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratasesta))
    #Čtyřicátá sedmá
    if ctyratasedma_statement:
        for img_x, img_y in [ctyratasedma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratasedma))
    #Čtyřicátá osmá
    if ctyrataosma_statement:
        for img_x, img_y in [ctyrataosma]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyrataosma))
    #Čtyřicátá devátá
    if ctyratadevata_statement:
        for img_x, img_y in [ctyratadevata]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(room_image, (ctyratadevata))

    """
    End -------------- minimap_file.py
    """
    """
    Start -------------- plane.py
    """
    if isaac.colliderect(pygame.Rect(40, 250, 1, 100)):
        rect_x += 855
        move_side_counter += dvere_left_value
        prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
        dvere_left = True
    elif isaac.colliderect(pygame.Rect(960,250, 1, 100)):
        rect_x -= 855
        move_side_counter += dvere_right_value
        prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
        dvere_right = True
    elif isaac.colliderect(pygame.Rect(450,40, 100, 1)):
        rect_y += 460
        move_up_counter += dvere_up_value
        prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
        dvere_up = True
    elif isaac.colliderect(pygame.Rect(450,560, 100, 1)):
        rect_y -= 460
        move_up_counter += dvere_down_value
        prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
        dvere_down = True





    """
    End -------------- plane.py
    """
    # Draw the player health bar
    window.blit(heart_full, (25, 25))
    window.blit(heart_full, (95, 25))
    window.blit(heart_half, (165, 25))
    
    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)

"""
tears
Věnovala bych se more important things, bullets zatim +- funguji, potom bych se podivala na tears hybajici se podle tela a vycentrovani

dvere
ve slozce "danca_nesahat" v souboru "idk.py" presne polohy dveri, pozadi<"nakres_dveri.png"> jen pro mereni polohy dveri
"""