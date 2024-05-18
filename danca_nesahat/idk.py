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

minimap = pygame.image.load("minimap_layout.png")
minimap = pygame.transform.scale(minimap, (250, 200))



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

    # Draw the character and hearts on the window
    isaac = window.blit(postava, (rect_x, rect_y))
    # Draw the player health bar
    window.blit(heart_full, (25, 25))
    window.blit(heart_full, (95, 25))
    window.blit(heart_half, (165, 25))

    window.blit(minimap, (1089, 25))
    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)


#75,50 <-- stred minimapy
"""
mereno na velikosti okna - 1000,600

0,250 - 0,350 - zapadni dvere
1000,250 - 1000,350 - vychodni dvere
450,0 - 550,0 - severni dvere
450,600 - 550,600 - jizni dvere

ohraniceni isaaca:
rect_x = max(40, min(rect_x, WIDTH - 101))
rect_y = max(40, min(rect_y, HEIGHT - 96))
<presne na pixel, opovaz se zpochybnovat>
"""
