import pygame, sys
pygame.init()

telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)

projectile_size = 10
projectile_speed = 10
player_projectiles = []
projectiles = []

window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")
rect_x, rect_y = 70, 500
WIDTH, HEIGHT = 1500, 1000
clock = pygame.time.Clock()
velikost_postavy = 30
postava = pygame.image.load("pixelovy_isaac_vetsi.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_projectiles.append((rect_x + velikost_postavy // 2, rect_y))

    window.fill(hneda)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        rect_x -= 5
    if keys[pygame.K_d]:
        rect_x += 5
    if keys[pygame.K_w]:
        rect_y -= 5
    if keys[pygame.K_s]:
        rect_y += 5

    new_player_projectiles = []
    for proj_x, proj_y in player_projectiles:
        proj_y -= projectile_speed
        if proj_y > 0:
            new_player_projectiles.append((proj_x, proj_y))
    player_projectiles = new_player_projectiles

    for proj_x, proj_y in player_projectiles:
        pygame.draw.rect(window, modra_mouchy, (proj_x, proj_y, projectile_size, projectile_size))



    rect_x = max(0, min(rect_x, WIDTH - 100))
    rect_y = max(0, min(rect_y, HEIGHT - 100))

    isaac = window.blit(postava, (rect_x, rect_y))


    
    pygame.display.update()
    clock.tick(30)