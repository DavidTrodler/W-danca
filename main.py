import pygame, sys
pygame.init()
#Importing functions
from map import pohyby_mapy
from rooms_stats import set_statements, rooms_dictionary_funciton, current_room
from rooms_vyber import rooms_fixed
# map.py
prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
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
    # Move the character based on the pressed keys
    if keys[pygame.K_a]:
        rect_x -= 5
    if keys[pygame.K_d]:
        rect_x += 5
    if keys[pygame.K_w]:
        rect_y -= 5
    if keys[pygame.K_s]:
        rect_y += 5


    if doors_dictionary[current_room][0]:
        if isaac.colliderect(pygame.Rect(450,40, 100, 1)):
            rect_y -= 80
            move_up_counter += dvere_up_value
            prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
            dvere_up = True
    if doors_dictionary[current_room][1]:
        if isaac.colliderect(pygame.Rect(960,250, 1, 100)):
            rect_x += 80
            move_side_counter += dvere_right_value
            prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
            dvere_right = True
    if doors_dictionary[current_room][2]:
        if isaac.colliderect(pygame.Rect(450,560, 100, 1)):
            rect_y += 80
            move_up_counter += dvere_down_value
            prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
            dvere_down = True
    if doors_dictionary[current_room][3]:
        if isaac.colliderect(pygame.Rect(40, 250, 1, 100)):
            rect_x -= 80
            move_side_counter += dvere_left_value
            prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata = pohyby_mapy()
            dvere_left = True

    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)
