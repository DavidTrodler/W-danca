import pygame
import sys
import time
import random
import math

pygame.init()

# Nastavení okna hry
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Hra s obrazci")

# Barvy
white = (255, 255, 255)
red = (255, 0, 0)

# Velikosti hráče, nepřátel a projektilů
player_size = 30
player_speed = 5

enemy_size = 20
enemy_speed = 2

projectile_size = 10
projectile_speed = 10

# Inicializace proměnných pro úroveň a nepřátele
level = 1
last_level_time = time.time()
enemies_on_screen = 1

player_projectiles = []
enemies = []
projectiles = []

# Font pro text na obrazovce
font = pygame.font.Font(None, 36)

# Počáteční pozice hráče
player_x, player_y = screen.get_width() // 2, screen.get_height() - player_size

# Funkce pro vytvoření nových nepřátel
def create_new_enemies():
    global enemies_on_screen
    for _ in range(enemies_on_screen):
        enemy_x = random.randint(0, screen.get_width() - enemy_size)
        enemy_y = random.randint(0, screen.get_height() // 2)
        enemies.append((enemy_x, enemy_y, False))  # Přidání informace o stavu zásahu

# Funkce pro vytvoření nové úrovně (přidává více nepřátel)
def create_new_level():
    global level, enemies_on_screen
    level += 1
    enemies_on_screen = level
    create_new_enemies()

# Počáteční vytvoření nepřátel
create_new_enemies()

# Hlavní smyčka hry
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_projectiles.append((player_x + player_size // 2, player_y))

    # Pohyb hráče
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Detekce kolizí mezi projektily hráče a nepřáteli
    for proj_x, proj_y in player_projectiles:
        for i, (enemy_x, enemy_y, hit) in enumerate(enemies):
            if not hit and pygame.Rect(proj_x, proj_y, projectile_size, projectile_size).colliderect(
                    pygame.Rect(enemy_x, enemy_y, enemy_size, enemy_size)):
                enemies[i] = (enemy_x, enemy_y, True)  # Označení nepřítele jako zasaženého
                player_projectiles.remove((proj_x, proj_y))

    # Pohyb a aktualizace projektilů hráče
    new_player_projectiles = []
    for proj_x, proj_y in player_projectiles:
        proj_y -= projectile_speed
        if proj_y > 0:
            new_player_projectiles.append((proj_x, proj_y))
    player_projectiles = new_player_projectiles

    # Pohyb a aktualizace nepřátelských projektilů
    new_projectiles = []
    for proj_x, proj_y, angle in projectiles:
        proj_x += projectile_speed * math.cos(angle)
        proj_y += projectile_speed * math.sin(angle)
        if proj_y < screen.get_height():
            new_projectiles.append((proj_x, proj_y, angle))
    projectiles = new_projectiles

    # Detekce kolize hráče s nepřátelskými projektily
    for proj_x, proj_y, _ in projectiles:
        if pygame.Rect(player_x, player_y, player_size, player_size).colliderect(
                pygame.Rect(proj_x, proj_y, projectile_size, projectile_size)):
            print("Prohrál jsi!")
            pygame.quit()
            sys.exit()

    # Střelba nepřátel
    for i, (enemy_x, enemy_y, hit) in enumerate(enemies):
        if not hit:  # Nepřátelské projektily nestřílejí z zasažených nepřátel
            if enemy_x >= 0:
                if random.random() < 0.01:
                    dx = player_x - enemy_x
                    dy = player_y - enemy_y
                    angle = math.atan2(dy, dx)
                    projectiles.append((enemy_x + enemy_size // 2, enemy_y + enemy_size // 2, angle))

    # Omezení pohybu nepřátel na obrazovce
    for i, (enemy_x, enemy_y, hit) in enumerate(enemies):
        if enemy_x <= 0 or enemy_x >= screen.get_width() - enemy_size:
            enemy_x = min(max(enemy_x, 0), screen.get_width() - enemy_size)
            enemies[i] = (enemy_x, enemy_y, hit)

    # Vytvoření nové úrovně po určitém čase
    current_time = time.time()
    if current_time - last_level_time >= 15:
        create_new_level()
        last_level_time = current_time

    # Vykreslení všeho na obrazovku
    screen.fill(white)
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    for enemy_x, enemy_y, hit in enemies:
        if not hit:
            pygame.draw.rect(screen, red, (enemy_x, enemy_y, enemy_size, enemy_size))
    for proj_x, proj_y in player_projectiles:
        pygame.draw.rect(screen, red, (proj_x, proj_y, projectile_size, projectile_size))
    for proj_x, proj_y, _ in projectiles:
        pygame.draw.rect(screen, red, (proj_x, proj_y, projectile_size, projectile_size))

    # Vykreslení úrovně na obrazovku
    level_text = font.render(f"Level: {level}", True, red)
    screen.blit(level_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(60)