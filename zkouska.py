import pygame
import sys,time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Projectile Shooter")
clock = pygame.time.Clock()
# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player = pygame.Rect(400, 550, 50, 50)

# Set up the projectile
projectile = pygame.Rect(0, 0, 10, 10)
projectile_color = WHITE
projectile_speed = 5
projectile_state = "ready"

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Shoot projectile when spacebar is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if projectile_state == "ready":
                    projectile.x = player.x + player.width // 2 - projectile.width // 2
                    projectile.y = player.y
                    projectile_state = "fire"

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.x < 750:
        player.x += 5

    # Move the projectile
    if projectile_state == "fire":
        projectile.y -= projectile_speed
        if projectile.y < 0:
            projectile_state = "ready"

    # Draw the player, projectile, and background
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, projectile_color, projectile)

    # Update the display
    pygame.display.update()
    clock.tick(30)