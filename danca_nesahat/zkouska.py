"""
v tomto souboru na nás útočí moucha, která nám ubírá životy (zatim ne)§
moucha se pohybuje na základě toho, kde se nachází hráč <-- AI generated
pokud hráč narazí do mouchy, ztratí polovinu srdíčka <-- AI generated
je fakt pekna btw
"""



import pygame, sys
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
pozadi = pygame.image.load("nakres_dveri.png")
window.blit(pozadi, (0, 0))
aktualni_room = 1
importovani_slzy   = pygame.image.load("tear.png")
slza = pygame.transform.scale(importovani_slzy, (25, 25))

# Set initial position and dimensions for the character
rect_x, rect_y = 70, 500
WIDTH, HEIGHT = 1000, 600



""" ENEMIES """
#moucha bracho
moucha_x, moucha_y = 500, 300
hp_mouchy = 20

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load the character and tear image
velikost_postavy = 57
postava = pygame.image.load("pixelovy_isaac_vetsi.png")
importovani_slzy = pygame.image.load("tear.png")
heart_full = pygame.image.load("srdicka/full_heart.png")
heart_half = pygame.image.load("srdicka/half_a_heart.png")
moucha = pygame.image.load("enemies/moucha.png")

frst_srd = 3

pygame.display.update()

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
    window.blit(pozadi, (0, 0))

    # Ensure the character stays within the window boundaries
    rect_x = max(40, min(rect_x, WIDTH - 101))
    rect_y = max(40, min(rect_y, HEIGHT - 96))

    # Draw the character
    isaac = window.blit(postava, (rect_x, rect_y))

    # Draw the player health bar
    if frst_srd == 3:
        window.blit(heart_full, (25, 25))
        window.blit(heart_full, (95, 25))
        window.blit(heart_full, (165, 25))
    elif frst_srd == 2.5:
        window.blit(heart_full, (25, 25))
        window.blit(heart_full, (95, 25))
        window.blit(heart_half, (165, 25))
    elif frst_srd == 2:
        window.blit(heart_full, (25, 25))
        window.blit(heart_full, (95, 25))
    elif frst_srd == 1.5:
        window.blit(heart_full, (25, 25))
        window.blit(heart_half, (95, 25))
    elif frst_srd == 1:
        window.blit(heart_full, (25, 25))
    elif frst_srd == 0.5:
        window.blit(heart_half, (25, 25))
    elif frst_srd == 0:
        print("Game over, bracho")
        sys.exit()

    if isaac.colliderect(pygame.Rect(40, 250, 1, 100)):
        rect_x += 855
        print("zapadni")
    elif isaac.colliderect(pygame.Rect(960,250, 1, 100)):
        rect_x -= 855
        print("vychodni")
    elif isaac.colliderect(pygame.Rect(450,40, 100, 1)):
        rect_y += 460
        print("severni")
    elif isaac.colliderect(pygame.Rect(450,560, 100, 1)):
        rect_y -= 460
        print("jizni")





    if rect_x > moucha_x:
        moucha_x += 0.5
    if rect_x < moucha_x:
        moucha_x -= 0.5
    if rect_y > moucha_y:    
        moucha_y += 0.5
    if rect_y < moucha_y:       
        moucha_y -= 0.5

    if hp_mouchy > 0:
        angry_moucha = window.blit(moucha, (moucha_x, moucha_y))

    if isaac.colliderect(angry_moucha):
        frst_srd -= 0.5

    # Draw player projectiles on the window
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #UP_LEFT
    if len(player_projectiles_up_left) > 0:
        for proj_x, proj_y in player_projectiles_up_left:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #UP_RIGHT
    if len(player_projectiles_up_right) > 0:
        for proj_x, proj_y in player_projectiles_up_right:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN_LEFT
    if len(player_projectiles_down_left) > 0:
        for proj_x, proj_y in player_projectiles_down_left:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #DOWN_RIGHT
    if len(player_projectiles_down_right) > 0:
        for proj_x, proj_y in player_projectiles_down_right:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass
    #LEFT_DOWN
    if len(player_projectiles_left_down) > 0:
        for proj_x, proj_y in player_projectiles_left_down:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass
    #LEFT_UP
    if len(player_projectiles_left_up) > 0:
        for proj_x, proj_y in player_projectiles_left_up:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass
    #RIGHT_DOWN
    if len(player_projectiles_right_down) > 0:
        for proj_x, proj_y in player_projectiles_right_down:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass
    #RIGHT_UP
    if len(player_projectiles_right_up) > 0:
        for proj_x, proj_y in player_projectiles_right_up:
            isaac_strela = window.blit(slza, (proj_x, proj_y, projectile_size, projectile_size))
            if isaac_strela.colliderect(angry_moucha):
                hp_mouchy -= 0.5
                pass


    # Update the display and control the frame rate
    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
