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

#Dveře
dvere_up_value = -1
dvere_down_value = 1
dvere_left_value = 1
dvere_right_value = -1

dvere_up = False
dvere_down = False
dvere_left = False
dvere_right = False

# Room numbers
prvni = [100,100]
prvni[1] = prvni[1] + (move_up[1] * move_up_counter)
prvni[0] = prvni[0] + (move_side[0] * move_side_counter)
druha = [100, 130]

treti = [40, 100]

ctvrta = [100, 70]

pata = [160, 100]

sesta = [160, 130]

sedma = [40, 130]

osma = [40, 70]

devata = [160,70]

print(prvni)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    for img_x, img_y in prvni:
        if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0:
            window.blit(room_image, ((prvni)))
    #Druhá

    window.blit(room_image, (druha))
    window.blit(room_image, (treti))
    window.blit(room_image, (ctvrta))
    window.blit(room_image, (pata))
    window.blit(room_image, (sesta))
    window.blit(room_image, (sedma))
    window.blit(room_image, (osma))
    window.blit(room_image, (devata))



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