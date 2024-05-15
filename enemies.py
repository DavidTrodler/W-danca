import pygame, sys
from isaac_strileni_do_stran import level, player_position
pygame.init()

# Define color constants
telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)

enemies = []

# Create the game window
window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")

# Set initial position and dimensions for the character
rect_x, rect_y = 500, 500
WIDTH, HEIGHT = 1500, 1000

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

#Stats to variables
level = level() #----> Od levelu se odvíjí pravděpodobnost spavnutí nepřítele
player_position = player_position() #----> Od pozice se odvíjí, kam budou nepřátelé střílet

#enemies spawn
def enemies():
    pass

def enemies_position(): #----> Funkce, která určí pozici nepřátel
    pass

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for enemy in enemies:
        pygame.draw.rect(window, telova, enemy)
        pygame.draw.rect(window, cerna, enemy, 2)

    

    
    pygame.display.update()
    clock.tick(30)

"""
To do:

vytvořit NEPŘÁTELÉ a místnosti

"""