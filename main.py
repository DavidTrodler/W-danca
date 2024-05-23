import pygame, sys
pygame.init()
#Importing functions
from map import pohyby_mapy
from rooms_stats import set_statements, rooms_dictionary_funciton, current_room_function
from rooms_vyber import rooms_fixed
from bullet_movement import bullet_movement
# map.py
#----------------------------------------------------------------------


clock = pygame.time.Clock()

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)
image_width = 60 #x  #<---- Šířka obrázku, dá se volně měnit
image_height = 30 #y


#----------------------------------------------------------------------

# Create the game window + Load images
WIDTH, HEIGHT = 1000, 600

window = pygame.display.set_mode((WIDTH, HEIGHT))
pozadi = pygame.image.load("nakres_dveri.png")
window.blit(pozadi, (0, 0))
postava = pygame.image.load("pixelovy_isaac_vetsi.png")
importovani_slzy = pygame.image.load("david_nesahat/tear.png")
slza = pygame.transform.scale(importovani_slzy, (25, 25))
room_image = pygame.image.load("david_nesahat/pozadi.png")
room_image = pygame.transform.scale(room_image,(image_width, image_height))
image_filter = pygame.transform.scale(room_image,(image_width, image_height))
room_image.set_alpha(128) #průhledné 0 - 255 neprůhledné
pygame.display.set_caption("ˇIsaacˇ")
#----------------------------------------------------------------------
#Level
level = 1

# Player variables
rect_x, rect_y = 70, 500
velikost_postavy = 57
projectile_size = 10
projectile_speed = 10
projectile_speed_diagonal = 4

# Room variables
velikost_mistnosti = WIDTH, HEIGHT

# Shooting cooldown
cooldown = 0
cooldown_time = 10


#Map
move_up_counter = 0 #<---- O kolik roomek se posunul hráč nahoru nebo dolů
move_side_counter = 0
current_room = 1
#Dveře, ukazuje, kam se mají osy posunout
dvere_up_value = 1
dvere_down_value = -1
dvere_left_value = 1
dvere_right_value = -1
dvere_up = False #<--- Změní se, pokud hráč projde dveřmi (kvůli if statment ve while loop)
dvere_down = False 
dvere_left = False
dvere_right = False

#----------------------------------------------------------------------

# Lists
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
#Map
move_up = [0, 30] # y + 30
move_side = [60, 0] # x + 60
image_filter_position = [775, 100] #<---- Pozice filtru
# Rooms list
rooms = [1]
rooms = rooms_fixed(level)




#Vyvolání funkcí
doors_dictionary = rooms_dictionary_funciton(rooms)
print(doors_dictionary)
mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)
print(mapa)
# Game loop
while True:
    # cooldown
    if cooldown > 0:
        cooldown -= 1
        shoots = True
    if cooldown == 0:
        shoots = False

    keys = pygame.key.get_pressed()

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
    window.blit(pozadi, (0, 0))


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

    for ii in rooms:
        for i in range(0, len(mapa[ii-1]), 2):
            img_x, img_y = mapa[ii-1][i], mapa[ii-1][i+1]
            if img_x < WIDTH and img_x > 0 and img_y < HEIGHT and img_y > 0: #<----- pouze, aby se nezobrazovaly mimo obrazovku
                window.blit(room_image, (img_x, img_y))

        window.blit(image_filter, (image_filter_position))
    #UP
    if doors_dictionary[current_room][0]:
        if isaac.colliderect(pygame.Rect(450,40, 100, 1)):
            doors = "UP"
            rect_y -= 80
            move_up_counter += dvere_up_value
            dvere_up = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
    #RIGHT
    if doors_dictionary[current_room][1]:
        if isaac.colliderect(pygame.Rect(960,250, 1, 100)):
            doors = "RIGHT"
            rect_x += 80
            move_side_counter += dvere_right_value
            dvere_right = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
    #DOWN
    if doors_dictionary[current_room][2]:
        if isaac.colliderect(pygame.Rect(450,560, 100, 1)):
            doors = "DOWN"
            rect_y += 80
            move_up_counter += dvere_down_value
            dvere_down = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
    #LEFT
    if doors_dictionary[current_room][3]:
        if isaac.colliderect(pygame.Rect(40, 250, 1, 100)):
            doors = "LEFT"
            rect_x -= 80
            move_side_counter += dvere_left_value
            dvere_left = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            

    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
