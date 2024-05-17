import pygame, sys
from rooms_vyber import vyber_insert_level

pygame.display.set_mode


# Create the game window
window = pygame.display.set_mode((1366, 755))
WIDTH = 755
HEIGHT = 1366


pygame.display.set_caption("ˇIsaacˇ")
room_image = pygame.image.load("pozadi.png")
clock = pygame.time.Clock()
room_image = pygame.transform.scale(room_image,(60,30))
# Rooms list
rooms = [2]
rooms = vyber_insert_level(3)
print(rooms)


#Pohyby mapy
move_up = [0, 30]
move_side = [60, 0]
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
prvni = [100,100]
prvni[1] = prvni[1] + (move_up[1] * move_up_counter) # <-- Pokud se změní move up counter, nebude nulový a osa x se posune
prvni[0] = prvni[0] + (move_side[0] * move_side_counter)

#Druhá
druha = [100, 130]
druha[1] = druha[1] + (move_up[1] * move_up_counter)
druha[0] = druha[0] + (move_side[0] * move_side_counter)

#Třetí
treti = [40, 100]
treti[1] = treti[1] + (move_up[1] * move_up_counter)
treti[0] = treti[0] + (move_side[0] * move_side_counter)

#Čtvrtá
ctvrta = [100, 70]
ctvrta[1] = ctvrta[1] + (move_up[1] * move_up_counter)
ctvrta[0] = ctvrta[0] + (move_side[0] * move_side_counter)

#Pátá
pata = [160, 100]
pata[1] = pata[1] + (move_up[1] * move_up_counter)
pata[0] = pata[0] + (move_side[0] * move_side_counter)

#Šestá
sesta = [160, 130]
sesta[1] = sesta[1] + (move_up[1] * move_up_counter)
sesta[0] = sesta[0] + (move_side[0] * move_side_counter)

#Sedmá
sedma = [40, 130]
sedma[1] = sedma[1] + (move_up[1] * move_up_counter)
sedma[0] = sedma[0] + (move_side[0] * move_side_counter)

#Osmá
osma = [40, 70]
osma[1] = osma[1] + (move_up[1] * move_up_counter)
osma[0] = osma[0] + (move_side[0] * move_side_counter)

#Devátá
devata = [160,70]
devata[1] = devata[1] + (move_up[1] * move_up_counter)
devata[0] = devata[0] + (move_side[0] * move_side_counter)

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
    for img_x, img_y in [prvni]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, (prvni))
    #Druhá
    for img_x, img_y in [druha]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((druha)))
    #Třetí
    for img_x, img_y in [treti]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((treti)))
    #Čtvrtá
    for img_x, img_y in [ctvrta]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((ctvrta)))
    #Pátá
    for img_x, img_y in [pata]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((pata)))
    #Šestá
    for img_x, img_y in [sesta]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((sesta))) 
    #Sedmá
    for img_x, img_y in [sedma]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((sedma)))
    #Osmá
    for img_x, img_y in [osma]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((osma)))
    #Devátá
    for img_x, img_y in [devata]:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, (devata))


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