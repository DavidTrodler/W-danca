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
# Shooting cooldown
cooldown = 0
cooldown_time = 5


# Initialize lists for player projectiles and all projectiles
player_projectiles_up = []
player_projectiles_down = []
player_projectiles_left = []
player_projectiles_right = []
projectiles = []

# Create the game window
window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")

# Set initial position and dimensions for the character
rect_x, rect_y = 500, 500
WIDTH, HEIGHT = 1500, 1000

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load the character image
velikost_postavy = 57
postava = pygame.image.load("pixelovy_isaac_vetsi.png")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            #UP
            if event.key == pygame.K_UP and shoots == False:
                player_projectiles_up.append((rect_x + velikost_postavy // 2, rect_y))
                cooldown = cooldown_time
                break
            #DOWN
            elif event.key == pygame.K_DOWN and shoots == False:
                player_projectiles_down.append((rect_x + velikost_postavy // 2, rect_y + 46))
                cooldown = cooldown_time  
                break
            #LEFT
            elif event.key == pygame.K_LEFT and shoots == False:
                player_projectiles_left.append((rect_x - 2, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break
            #RIGHT
            elif event.key == pygame.K_RIGHT and shoots == False:
                player_projectiles_right.append((rect_x + 52, rect_y + velikost_postavy // 2))
                cooldown = cooldown_time
                break

    if cooldown > 0:
        cooldown -= 1
        shoots = True
    if cooldown == 0:
        shoots = False
            

        


    window.fill(hneda)

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
    new_player_projectiles_UP = []
    new_player_projectiles_DOWN = []
    new_player_projectiles_LEFT = []
    new_player_projectiles_RIGHT = []



    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            proj_y -= projectile_speed
            if proj_y > 0:
                new_player_projectiles_UP.append((proj_x, proj_y))
        player_projectiles_up = new_player_projectiles_UP

    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            proj_y += projectile_speed
            if proj_y < HEIGHT:
                new_player_projectiles_DOWN.append((proj_x, proj_y))
        player_projectiles_down = new_player_projectiles_DOWN

    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            proj_x -= projectile_speed
            if proj_x > 0:
                new_player_projectiles_LEFT.append((proj_x, proj_y))
        player_projectiles_left = new_player_projectiles_LEFT

    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            proj_x += projectile_speed
            if proj_x < WIDTH:
                new_player_projectiles_RIGHT.append((proj_x, proj_y))
        player_projectiles_right = new_player_projectiles_RIGHT

    # Draw player projectiles on the window
    
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))
    
    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))
    
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))
    
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))
    
    # Ensure the character stays within the window boundaries
    rect_x = max(0, min(rect_x, WIDTH - 100))
    rect_y = max(0, min(rect_y, HEIGHT - 100))

    # Draw the character on the window
    isaac = window.blit(postava, (rect_x, rect_y))

    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)

"""
To do:

Vyřešit pohyb projektilů v závislosti na pohybu ISAACA. ---> (rozdíl jednotlivých framů pozic ISAACA)
Vyřešit pohyb projektilů ve všech směrech.


vytvořit NEPŘÁTELÉ a místnosti

"""