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

# Create the game window + Load images
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("ˇIsaacˇ")
pozadi = pygame.image.load("nakres_dveri.png")
window.blit(pozadi, (0, 0))
aktualni_room = 1

# Set initial position and dimensions for the character
rect_x, rect_y = 70, 500
WIDTH, HEIGHT = 1000, 600



""" ENEMIES """
#moucha bracho
moucha_x, moucha_y = 500, 300

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

    # Vykreslení pozadí
    window.blit(pozadi, (0, 0))

    # Ensure the character stays within the window boundaries
    rect_x = max(40, min(rect_x, WIDTH - 101))
    rect_y = max(40, min(rect_y, HEIGHT - 96))

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


    # Draw the character and hearts on the window
    isaac = window.blit(postava, (rect_x, rect_y))

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



    # Draw the character and hearts on the window
    isaac = window.blit(postava, (rect_x, rect_y))


    if rect_x > moucha_x:
        moucha_x += 1
    if rect_x < moucha_x:
        moucha_x -= 1
    if rect_y > moucha_y:    
        moucha_y += 1               
    if rect_y < moucha_y:       
        moucha_y -= 1
    angry_moucha = window.blit(moucha, (moucha_x, moucha_y))
    if isaac.colliderect(angry_moucha):
        frst_srd -= 0.5

    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)
