import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("My Game")

# Set up the player
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 3  

# Set up the FOLLOWERS
followers = []
follower_width = 50
follower_height = 50
follower_speed = 1  # Adjust follower speed as needed
# Set up the SHOOTERS
shooters = []
shooter_projectile = []
shooter_width = 50
shooter_height = 50
shooter_projectile_speed = 1  # Adjust shooter speed as needed


# Set up the FOLLOWER timer
follower_spawn_timer = pygame.time.get_ticks()  # Get the current time in milliseconds
follower_spawn_interval = 10000  # Spawn a new follower every 10000 milliseconds (10 second)
# Set up the SHOOTER timer
shooter_spawn_timer = pygame.time.get_ticks()  # Get the current time in milliseconds
shooter_spawn_interval = 5000  # Spawn a new shooter every 5000 milliseconds (5 seconds)

# Game loop
running = True
clock = pygame.time.Clock()  # Create a clock object


shooter_x = random.randint(0, window_width - shooter_width)
shooter_y = random.randint(0, window_height - shooter_height)
shooters.append((shooter_x, shooter_y))



for i in shooters:
    projectile_x, projectile_y  = shooters[i]
    shooter_projectile.append((projectile_x, projectile_y, angle))
    projectiles = shooter_projectile
    shooter_projectile[i] = (projectile_x, projectile_y, angle)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < window_height - player_height:
        player_y += player_speed

    # Check if it's time to spawn a new FOLLOWER
    current_time = pygame.time.get_ticks()
    if current_time - follower_spawn_timer >= follower_spawn_interval:
        follower_x = random.randint(0, window_width - follower_width)
        follower_y = random.randint(0, window_height - follower_height)
        followers.append((follower_x, follower_y))
        follower_spawn_timer = current_time
    # Check if it's time to spawn a new SHOOTER
    if current_time - shooter_spawn_timer >= shooter_spawn_interval:
        shooter_x = random.randint(0, window_width - shooter_width)
        shooter_y = random.randint(0, window_height - shooter_height)
        shooters.append((shooter_x, shooter_y))
        shooter_spawn_timer = current_time


    # Update the position of each FOLLOWER to follow the player
    for i in range(len(followers)):
        follower_x, follower_y = followers[i]
        if follower_x < player_x:
            follower_x += follower_speed
        elif follower_x > player_x:
            follower_x -= follower_speed
        if follower_y < player_y:
            follower_y += follower_speed
        elif follower_y > player_y:
            follower_y -= follower_speed
        followers[i] = (follower_x, follower_y)

    # Make shooter shoot at the player direction
    for i in range(len(shooter_projectile)):
        projectile_x, projectile_y, angle = shooter_projectile[i]
        if projectile_x < projectile_y:
            move = projectile_y / projectile_x
            projectile_y = float(projectile_y) + (float(shooter_projectile_speed) - move)
            projectile_x = float(projectile_x) + (float(shooter_projectile_speed) // float(move))
            shooter_projectile.append((shooter_x, shooter_y))
        if projectile_y < window.get_height():
            projectile.append((projectile_x, projectile_y, angle))
        projectiles = shooter_projectile
        shooter_projectile[i] = (projectile_x, projectile_y, angle)




       
    
    # Check for collision with any FOLLOWER
    for follower in followers:
        follower_x, follower_y = follower
        if player_x < follower_x + follower_width and player_x + player_width > follower_x and player_y < follower_y + follower_height and player_y + player_height > follower_y:
            running = False
    # Check for collision with any SHOOTER
    for shooter in shooters:
        shooter_x, shooter_y = shooter
        if player_x < shooter_x + shooter_width and player_x + player_width > shooter_x and player_y < shooter_y + shooter_height and player_y + player_height > shooter_y:
            running = False
    # Check for collision with any SHOOTER projectile
    for projectile in shooter_projectile:
        projectile_x, projectile_y, angle = projectile
        if player_x < projectile_x + shooter_width and player_x + player_width > projectile_x and player_y < projectile_y + shooter_height and player_y + player_height > projectile_y:
            running = False
    # Check for collision with SHOOTER projectiles

    # Clear the window
    window.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(window, (255, 0, 0), (player_x, player_y, player_width, player_height))

    # Draw the FOLLOWERS
    for follower in followers:
        follower_x, follower_y = follower
        pygame.draw.rect(window, (0, 0, 255), (follower_x, follower_y, follower_width, follower_height))
    # Draw the SHOOTERS
    for shooter in shooters:
        shooter_x, shooter_y = shooter
        pygame.draw.rect(window, (0, 255, 0), (shooter_x, shooter_y, shooter_width, shooter_height))
    # Draw the SHOOTER projectiles
    for projectile in shooter_projectile:
        projectile_x, projectile_y, angle = projectile
        pygame.draw.rect(window, (255, 255, 0), (projectile_x, projectile_y, shooter_width, shooter_height))

    # Update the display
    pygame.display.update()

    clock.tick(300)

# Quit the game
pygame.quit()
