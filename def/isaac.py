import pygame, sys
pygame.init()
from jedna_moucha import osm_much

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)

""" LIST S TYPY ROOMEK, ZATIM NEPOUZIVANE """
list_typu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

""" ENEMIES """
#moucha bracho
moucha_x, moucha_y = 500, 300
hp_mouchy = 20
srd = 3
moucha = pygame.image.load("def/moucha.png")
musi_pozice = []

# Create the game window + Load images
WIDTH, HEIGHT = 1000, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ˇIsaacˇ")
pozadi = pygame.image.load("nakres_dveri.png")
window.blit(pozadi, (0, 0))

# Set initial position for the character
rect_x, rect_y = 70, 500

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load the character and tear image
postava = pygame.image.load("pixelovy_isaac_vetsi.png")

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

    musi_pozice = osm_much(rect_x, moucha_x, rect_y, moucha_y)
    if hp_mouchy > 0:
        angry_moucha = window.blit(moucha, (musi_pozice[0], musi_pozice[1]))
        if isaac.colliderect(angry_moucha):
            srd -= 0.5

    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)