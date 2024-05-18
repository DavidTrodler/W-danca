import pygame, sys
from rooms_vyber import rooms_fixed


pygame.display.set_mode


# Create the game window
window = pygame.display.set_mode((1366, 755))
WIDTH = 755
HEIGHT = 1366
image_width = 60 #x
image_height = 30 #y
pygame.display.set_caption("ˇIsaacˇ")
room_image = pygame.image.load("pozadi.png")
zkouzka_image = pygame.image.load("nakres_dveri.png")
clock = pygame.time.Clock()
zkouzka_image = pygame.transform.scale(zkouzka_image,(image_width,image_height))
room_image = pygame.transform.scale(room_image,(image_width,image_height))
# Rooms list
rooms = [1]
rooms = rooms_fixed(3)
print(rooms)


#Pohyby mapy
move_up = [0, 30] # y + 30
move_side = [60, 0] # x + 60
move_up_counter = 0
move_side_counter = 0

#Dveře, ukazuje, kam se mají osy posunout
dvere_up_value = -1
dvere_down_value = 1
dvere_left_value = 1
dvere_right_value = -1

dvere_up = False #<--- Změní se, pokud hráč projde dveřmi (kvůli if statment ve while loop)
dvere_down = False
dvere_left = False
dvere_right = False

# Room numbers
#První
prvni = [500 , 500] #POKUD CHCEŠ ZMĚNIT UMÍSTĚNÍ MAPY, ZMĚŇ UMÍSTĚNÍ PRVNÍ ROOMKY   
prvni[1] = prvni[1] + (move_up[1] * move_up_counter)
prvni[0] = prvni[0] + (move_side[0] * move_side_counter)

#Druhá
druha = [0,0]
druha[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
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




prvni_statement = True
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


print(prvni)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Nyní nefunguje, ale bude, až budeme mít dveře
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



    #První
    if prvni_statement:
        for img_x, img_y in [prvni]:
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
                window.blit(zkouzka_image, (prvni))
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



#PŘIDAT oblast na obrazovce, ve které se roomky nebudou zobrazovat (podobně jako to tam je, jen si vyber oblast jakou budeš chtít)


    pygame.display.update()


"""
Search for: Half transparent image in pygame
            How to adjust pygame window blit size
"""


"""
Dodělat zobrazení roomek na mapě následujícím způsobem.
-----------------------------------------------------------------
Vše se bude odvíjet od roomky č. 1, která bude mít souřadnice 360, 200. (asi, oblast minimapy je znázorněna v souboru "minimapa rozměry.png")
Následující roomky budou mít vztah k roomce, například roomka nad ní bude mít souřadnice
stejné jako roomka č. 1, ale bude mít y-ovou souřadnici o 200 větší. Roomka vpravo od ní bude mít
souřadnice pro x větší např. o 300 atd...
!! čísla roomek jsou znázorněna v excelové tabulce ve složce s projektem (W-danca) !! 

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
Pokud se změní souřadnice roomky č. 1, změní se i souřadnice všech ostatních roomek.

Při zobrazování roomek bude podmínka: Pokud nejsou souřadnice roomky v oblasti minimapy, obrázek roomky se nevykreslí.
"""