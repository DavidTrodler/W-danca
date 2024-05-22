import pygame, sys
pygame.init()

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)


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
velikost_postavy = 57
postava = pygame.image.load("pixelovy_isaac_vetsi.png")
importovani_slzy = pygame.image.load("tear.png")
slza = pygame.transform.scale(importovani_slzy, (25, 25))
heart_full = pygame.image.load("srdicka/full_heart.png")
heart_half = pygame.image.load("srdicka/half_a_heart.png")

#Functions for enemies.py
def level():
    pass

def player_position():
    pass

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

    


    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)