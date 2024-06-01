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

# Create the game window
WIDTH, HEIGHT = 1000, 600
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
level = 20

# Player variables
rect_x, rect_y = 70, 500
velikost_postavy = 57
projectile_size = 10
projectile_speed = 2
projectile_speed_diagonal = 0.5
bullet_range = 100 #Čas, po který bude existovat
player_speed = 2

# Room variables
velikost_mistnosti = WIDTH, HEIGHT

# Shooting cooldown
cooldown = 0
cooldown_time = 20


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

#DOWN
player_projectiles_down = []

#LEFT
player_projectiles_left = []

#RIGHT
player_projectiles_right = []

#ALL
projectiles = []
#Map
move_up = [0, 30] # y + 30
move_side = [60, 0] # x + 60
image_filter_position = [775, 100] #<---- Pozice filtru
# Rooms list
rooms = [1]
rooms = rooms_fixed(level)

rooms_dict = {}
rooms_dict = room_typesss(rooms)

print(rooms_dict)

current_prekazky = rooms_dict[current_room]["prekazky"]
print("PREKAZKY", current_prekazky)



door_cooldown = 0
door_cooldown_time = 20

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



#NO ENTRY AREA
no_entry_area_x = []
no_entry_area_y = []

def new_room_shit():
    no_entry_area_x = []
    no_entry_area_y = []
    for i in range(0, len(current_prekazky), 2):
        x, y = current_prekazky[i], current_prekazky[i+1]
        no_entry_area_x.append(x)
        no_entry_area_y.append(y)
    return no_entry_area_x, no_entry_area_y

def projectile_cleaning():
    player_projectiles_up = []
    player_projectiles_down = []
    player_projectiles_left = []
    player_projectiles_right = []
    projectiles = []
    
    return player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, projectiles

#HOUSE OD DANCI
VELOCITY         = 5
LERP_FACTOR      = 0.05
minimum_distance = 25
maximum_distance = 100


#TO DO --- OBRÁTIT ČERVENOU SRAČKU
def FollowMe(pops, fpos):
    target_vector       = pygame.math.Vector2(*pops)
    follower_vector     = pygame.math.Vector2(*fpos)
    new_follower_vector = pygame.math.Vector2(*fpos)

    distance = follower_vector.distance_to(target_vector)
    direction_vector    = (target_vector - follower_vector) / distance
    min_step            = max(0, distance - maximum_distance)
    max_step            = distance
    step_distance       = min_step + (max_step - min_step) * LERP_FACTOR
    new_follower_vector = follower_vector + direction_vector * step_distance

    return (new_follower_vector.x, new_follower_vector.y) 

follower = (100, 100)

player_dot = (rect_x + 28.5), (rect_y + 28.5)
no_entry_area_x, no_entry_area_y = new_room_shit()
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
    #HOUSE OD DANCI
    player   = (rect_x + 28.5), (rect_y + 28.5)
    follower = FollowMe(player, follower)
    f_x,f_y = follower
    p_x,p_y = player
    f_x = f_x - p_x
    f_y = f_y - p_y
    f_x = -(f_x/20)
    f_y = -(f_y/20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #Shooting
        elif event.type == pygame.KEYDOWN:
            #UP
            if event.key == pygame.K_UP and shoots == False:
                player_projectiles_up.append((rect_x + velikost_postavy // 2, rect_y, f_x, f_y, bullet_range))
                cooldown = cooldown_time
                break
            #DOWN
            elif event.key == pygame.K_DOWN and shoots == False:
                player_projectiles_down.append((rect_x + velikost_postavy // 2, rect_y + velikost_postavy, f_x, f_y, bullet_range))
                cooldown = cooldown_time  
                break

            #LEFT
            elif event.key == pygame.K_LEFT and shoots == False:
                player_projectiles_left.append((rect_x, rect_y + velikost_postavy // 2, f_x, f_y, bullet_range))
                cooldown = cooldown_time
                break
            #RIGHT
            elif event.key == pygame.K_RIGHT and shoots == False:
                player_projectiles_right.append((rect_x + velikost_postavy, rect_y + velikost_postavy // 2, f_x, f_y, bullet_range))
                cooldown = cooldown_time
                break
        

    # Move the character based on thed pressed keys



    w_statement = True
    d_statement = True
    s_statement = True
    a_statement = True
    d_statement = True
    
    for x, y in zip(no_entry_area_x, no_entry_area_y):
        isaac_rect = pygame.Rect(rect_x, rect_y, velikost_postavy, velikost_postavy)
        zone_1 = pygame.Rect(x+2, y, 46, 25)
        zone_2 = pygame.Rect(x+25, y+2, 25, 46)
        zone_3 = pygame.Rect(x+2, y+25, 46, 25)
        zone_4 = pygame.Rect(x, y+2, 25, 46)
        
        if isaac_rect.colliderect(zone_1):
            s_statement = False
        elif isaac_rect.colliderect(zone_2):
            a_statement = False
        elif isaac_rect.colliderect(zone_3):
            w_statement = False
        elif isaac_rect.colliderect(zone_4):
            d_statement = False

    if keys[pygame.K_d] and d_statement:
        player_dot_x, player_dot_y = player_dot
        player_dot_x += player_speed
        player_dot = player_dot_x, player_dot_y

    if keys[pygame.K_w] and w_statement:
        player_dot_x, player_dot_y = player_dot
        player_dot_y -= player_speed
        player_dot = player_dot_x, player_dot_y

    if keys[pygame.K_s] and s_statement:
        player_dot_x, player_dot_y = player_dot
        player_dot_y += player_speed
        player_dot = player_dot_x, player_dot_y

    if keys[pygame.K_a] and a_statement:
        player_dot_x, player_dot_y = player_dot
        player_dot_x -= player_speed
        player_dot = player_dot_x, player_dot_y


    rect_x, rect_y = FollowMe(player_dot, (rect_x, rect_y))
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

    #DOWN
    new_player_projectiles_DOWN = []

    #LEFT
    new_player_projectiles_LEFT = []

    #RIGHT
    new_player_projectiles_RIGHT = []

    print("UP", player_projectiles_up)
    player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right = bullet_movement(projectile_speed, WIDTH, HEIGHT, player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, new_player_projectiles_UP, new_player_projectiles_DOWN, new_player_projectiles_LEFT, new_player_projectiles_RIGHT, no_entry_area_x, no_entry_area_y, projectile_size)


    #Vykreslení pozadí
    window.blit(rooms_dict[current_room]["theme"], (0, 0)) #ANOOO FUNGUJE TOO DOPICII





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
        for proj_x, proj_y, x, y, t in player_projectiles_up:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y, x, y, t in player_projectiles_left:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y, x, y, t in player_projectiles_down:
            window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y, x, y, t in player_projectiles_right:
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
            current_prekazky = rooms_dict[current_room]["prekazky"]
            no_entry_area_x, no_entry_area_y = new_room_shit()
            player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, projectiles = projectile_cleaning()
            time.sleep(0.1)
    #RIGHT
    if doors_dictionary[current_room][1]:
        rotated_doors_image_right = pygame.transform.rotate(doors_image, -90)
        window.blit(rotated_doors_image_right, (960, 250))
        if isaac.colliderect(pygame.Rect(950,250, 1, 100)) and door_cooldown == 0:
            doors = "RIGHT"
            door_cooldown = door_cooldown_time
            rect_x -= 855
            move_side_counter += dvere_right_value
            dvere_right = True
            current_room = current_room_function(doors, current_room)
            mapa = [prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata] = pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up)            
            current_prekazky = rooms_dict[current_room]["prekazky"]
            no_entry_area_x, no_entry_area_y = new_room_shit()
            player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, projectiles = projectile_cleaning()
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
            current_prekazky = rooms_dict[current_room]["prekazky"]
            no_entry_area_x, no_entry_area_y = new_room_shit()
            player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, projectiles = projectile_cleaning()
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
            current_prekazky = rooms_dict[current_room]["prekazky"]
            no_entry_area_x, no_entry_area_y = new_room_shit()
            player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, projectiles = projectile_cleaning()
            time.sleep(0.1)

    for i in range(0, len(current_prekazky), 2):
        x, y = current_prekazky[i], current_prekazky[i+1]
        pygame.draw.rect(window, (255, 0, 0), (x, y, 50, 50))

    rect_x = max(40, min(rect_x, WIDTH - 101))
    rect_y = max(40, min(rect_y, HEIGHT - 96))

    #HOUSE OD DANCI
    pygame.draw.circle(window, (0, 0, 255), player, 10)
    pygame.draw.circle(window, (255, 0, 0), (round(follower[0]), round(follower[1])), 10)


    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.display.update()
    clock.tick(150)