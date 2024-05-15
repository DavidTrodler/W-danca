import pygame, sys
pygame.init()

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)


# Create the game window
window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")

# Set initial position and dimensions for the character
rect_x, rect_y = 500, 500
WIDTH, HEIGHT = 1500, 1000

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

#ROOMS
rooms = [56,66,67,68,58,59,49,50,60,70,80]

#Mapa
pygame.image.load("pozadi.png")




# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    

    
    pygame.display.update()
    clock.tick(30)

