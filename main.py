import pygame, sys
pygame.init()
#Importing functions
from map import pohyby_mapy
from rooms_stats import set_statements, rooms_dictionary_funciton, current_room_function
from rooms_vyber import rooms_fixed
from bullet_movement import bullet_movement
from rooms_types import room_types, room_typesss, room_typeees
import rooms_types
import time
from vsechny_cislicka import telova_barva, hneda_barva, modra_mouchy_barva, cerna_barva, sirka_obrazku, vyska_obrazku, width_mapy, height_mapy, level, rect_x, rect_y, velikost_postavy, projectile_size, projectile_speed, projectile_speed_diagonal, cooldown, cooldown_time, move_up_counter, move_side_counter, current_room, dvere_up_value, dvere_down_value, dvere_left_value, dvere_right_value, dvere_up, dvere_down, dvere_left, dvere_right, player_projectiles_up, player_projectiles_up_left, player_projectiles_up_right, player_projectiles_down, player_projectiles_down_left, player_projectiles_down_right, player_projectiles_left, player_projectiles_left_down, player_projectiles_left_up, player_projectiles_right, player_projectiles_right_down, player_projectiles_right_up, rooms, rooms_dict, move_up, move_side, image_filter_position, projectiles, door_cooldown, door_cooldown_time
# map.py
#----------------------------------------------------------------------



clock = pygame.time.Clock()

# Define color constants
telova = telova_barva()
hneda = hneda_barva()
modra_mouchy = modra_mouchy_barva()
cerna = cerna_barva()
image_width = sirka_obrazku() #x  #<---- Šířka obrázku, dá se volně měnit
image_height = vyska_obrazku() #y


#----------------------------------------------------------------------

# Create the game window
WIDTH, HEIGHT = width_mapy(), height_mapy()
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Loading background images
pozadi = pygame.image.load("nakres_dveri.png")
room_image = pygame.image.load("david_nesahat/pozadi.png")
pozaadi = room_types()
#----------------------------------------------------------------------
doors_image = pygame.image.load("doors.png")
doors_image = pygame.transform.scale(doors_image, (100, 60))
pozaadi = pygame.transform.scale(pozaadi,(WIDTH, HEIGHT))
postava = pygame.image.load("pixelovy_isaac_vetsi.png")
importovani_slzy = pygame.image.load("david_nesahat/tear.png")
slza = pygame.transform.scale(importovani_slzy, (25, 25))
room_image = pygame.transform.scale(room_image,(image_width, image_height))
image_filter = pygame.transform.scale(room_image,(image_width, image_height))
room_image.set_alpha(128) #průhledné 0 - 255 neprůhledné
pygame.display.set_caption("ˇIsaacˇ")
#----------------------------------------------------------------------
#Level
level = level()

# Player variables
rect_x, rect_y = rect_x(), rect_y()
velikost_postavy = velikost_postavy()
projectile_size = projectile_size()
projectile_speed = projectile_speed()
projectile_speed_diagonal = projectile_speed_diagonal()

# Room variables
velikost_mistnosti = WIDTH, HEIGHT

# Shooting cooldown
cooldown = cooldown()
cooldown_time = cooldown_time()


#Map
move_up_counter = move_up_counter() #<---- O kolik roomek se posunul hráč nahoru nebo dolů
move_side_counter = move_side_counter()
current_room = current_room()
#Dveře, ukazuje, kam se mají osy posunout
dvere_up_value = dvere_up_value()
dvere_down_value = dvere_down_value()
dvere_left_value = dvere_left_value()
dvere_right_value = dvere_right_value()
dvere_up = dvere_up() #<--- Změní se, pokud hráč projde dveřmi (kvůli if statment ve while loop)
dvere_down = dvere_down()
dvere_left = dvere_left()
dvere_right = dvere_right()

#----------------------------------------------------------------------

# Lists
#UP
player_projectiles_up = player_projectiles_up()
player_projectiles_up_left = player_projectiles_up_left()
player_projectiles_up_right = player_projectiles_up_right()
#DOWN
player_projectiles_down = player_projectiles_down()
player_projectiles_down_left = player_projectiles_down_left()
player_projectiles_down_right = player_projectiles_down_right()
#LEFT
player_projectiles_left = player_projectiles_left()
player_projectiles_left_down = player_projectiles_left_down()
player_projectiles_left_up = player_projectiles_left_up()
#RIGHT
player_projectiles_right = player_projectiles_right()
player_projectiles_right_down = player_projectiles_right_down()
player_projectiles_right_up = player_projectiles_right_up()
#ALL
projectiles = projectiles()
#Map
move_up = move_up() # y + 30
move_side = move_side() # x + 60
image_filter_position = image_filter_position() #<---- Pozice filtru
# Rooms list
rooms = rooms()
rooms = rooms_fixed(level)

rooms_dict = rooms_dict()
rooms_dict = room_typesss(rooms)

print(rooms_dict)


door_cooldown = door_cooldown()
door_cooldown_time = door_cooldown_time()

#Vyvolání funkcí
doors_dictionary = rooms_dictionary_funciton(rooms)
print(doors_dictionary)
mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)
print(mapa)

"""
#POUZE DOČASNÉ, NÁSTROJ NA DĚLÁNÍ PŘEKÁŽEK
# Vytvoření seznamu pro ukládání pozic kliknutí
click_positions = []
"""



# Game loop
while True:
    # cooldown
    if cooldown > 0:
        cooldown -= 1
        shoots = True
    if cooldown == 0:
        shoots = False
    if door_cooldown > 0:
        door_cooldown -= 1
    keys = pygame.key.get_pressed()
    # Shooting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Shooting
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
        
    """
        #POUZE DOČASNÉ, NÁSTROJ NA DĚLÁNÍ PŘEKÁŽEK
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Získání pozice kurzoru myši při kliknutí
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)  # Vypíše pozici kurzoru myši při kliknutí
            click_positions.append(pygame.mouse.get_pos())
    """
    # Bullet positions update
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
    player_projectiles_up, player_projectiles_up_left, player_projectiles_up_right, player_projectiles_down, player_projectiles_down_left, player_projectiles_down_right, player_projectiles_left, player_projectiles_left_down, player_projectiles_left_up, player_projectiles_right, player_projectiles_right_down, player_projectiles_right_up = bullet_movement(projectile_speed, projectile_speed_diagonal, WIDTH, HEIGHT, player_projectiles_up, player_projectiles_up_left, player_projectiles_up_right, player_projectiles_down, player_projectiles_down_left, player_projectiles_down_right, player_projectiles_left, player_projectiles_left_down, player_projectiles_left_up, player_projectiles_right, player_projectiles_right_down, player_projectiles_right_up, new_player_projectiles_UP, new_player_projectiles_UP_LEFT, new_player_projectiles_UP_RIGHT, new_player_projectiles_DOWN, new_player_projectiles_DOWN_LEFT, new_player_projectiles_DOWN_RIGHT, new_player_projectiles_LEFT, new_player_projectiles_LEFT_DOWN, new_player_projectiles_LEFT_UP, new_player_projectiles_RIGHT, new_player_projectiles_RIGHT_DOWN, new_player_projectiles_RIGHT_UP)
    # Move the character based on the pressed keys
    if keys[pygame.K_a]:
        rect_x -= 5
    if keys[pygame.K_d]:
        rect_x += 5
    if keys[pygame.K_w]:
        rect_y -= 5
    if keys[pygame.K_s]:
        rect_y += 5

    #Vykreslení pozadí
    window.blit(pozaadi, (0, 0))





    """
    #POUZE DOČASNÉ, NÁSTROJ NA DĚLÁNÍ PŘEKÁŽEK
    # Získání pozice kurzoru myši
    mouse_pos = pygame.mouse.get_pos()
    # Vykreslení čtverce na pozici myši
    pygame.draw.rect(window, (255, 0, 0), (mouse_pos[0], mouse_pos[1], 50, 50))
    
    for pos in click_positions:
        pygame.draw.rect(window, (255, 0, 0), (pos[0], pos[1], 50, 50))
    """






    #Vykrelsení projektilů
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

    
    
    #Vykreslení postavy + filtru
    isaac = window.blit(postava, (rect_x, rect_y))
    #Vykreslení minimapy
    for ii in rooms:
        for i in range(0, len(mapa[ii-1]), 2):
            img_x, img_y = mapa[ii-1][i], mapa[ii-1][i+1]
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0: #<----- pouze, aby se nezobrazovaly mimo obrazovku
                window.blit(room_image, (img_x, img_y))

        window.blit(image_filter, (image_filter_position))

    #Doors
    #UP
    if doors_dictionary[current_room][0]:
        window.blit(doors_image, (450, -10))
        if isaac.colliderect(pygame.Rect(450,40, 100, 1)) and door_cooldown == 0:
            doors = "UP"
            door_cooldown = door_cooldown_time
            rect_y += 460
            move_up_counter += dvere_up_value
            dvere_up = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
            
            time.sleep(0.1)
    #RIGHT
    if doors_dictionary[current_room][1]:
        rotated_doors_image_right = pygame.transform.rotate(doors_image, -90)
        window.blit(rotated_doors_image_right, (960, 250))
        if isaac.colliderect(pygame.Rect(960,250, 1, 100)) and door_cooldown == 0:
            doors = "RIGHT"
            door_cooldown = door_cooldown_time
            rect_x -= 855
            move_side_counter += dvere_right_value
            dvere_right = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
            time.sleep(0.1)   
    #DOWN
    if doors_dictionary[current_room][2]:
        rotated_doors_image_right = pygame.transform.rotate(doors_image, 180)
        window.blit(rotated_doors_image_right, (450, 550))
        if isaac.colliderect(pygame.Rect(450,560, 100, 1)) and door_cooldown == 0:
            doors = "DOWN"
            door_cooldown = door_cooldown_time
            rect_y -= 460
            move_up_counter += dvere_down_value
            dvere_down = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
            time.sleep(0.1)
    #LEFT
    if doors_dictionary[current_room][3]:
        rotated_doors_image_left = pygame.transform.rotate(doors_image, 90)
        window.blit(rotated_doors_image_left, (-20, 250))
        if isaac.colliderect(pygame.Rect(40, 250, 1, 100)) and door_cooldown == 0:
            doors = "LEFT"
            door_cooldown = door_cooldown_time
            rect_x += 855
            move_side_counter += dvere_left_value
            dvere_left = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
            time.sleep(0.1)

    rect_x = max(40, min(rect_x, WIDTH - 101))
    rect_y = max(40, min(rect_y, HEIGHT - 96))
    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
