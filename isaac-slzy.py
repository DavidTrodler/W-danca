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

# Initialize lists for player projectiles and all projectiles
player_projectiles = []
projectiles = []

# Create the game window
window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")

# Set initial position and dimensions for the character
rect_x, rect_y = 70, 500
WIDTH, HEIGHT = 1500, 1000

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Load the character image
velikost_postavy = 50
postava = pygame.image.load("pixelovy_isaac_vetsi.png")

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Add a new player projectile when spacebar is pressed
                player_projectiles.append((rect_x + velikost_postavy - 6, rect_y))

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
    new_player_projectiles = []
    for proj_x, proj_y in player_projectiles:
        proj_y -= projectile_speed
        if proj_y > 0:
            new_player_projectiles.append((proj_x, proj_y))
    player_projectiles = new_player_projectiles

    # Draw player projectiles on the window
    for proj_x, proj_y in player_projectiles:
        pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))

    # Ensure the character stays within the window boundaries
    rect_x = max(0, min(rect_x, WIDTH - 100))
    rect_y = max(0, min(rect_y, HEIGHT - 100))

    # Draw the character on the window
    isaac = window.blit(postava, (rect_x, rect_y))

    # Update the display and control the frame rate
    pygame.display.update()
    clock.tick(30)