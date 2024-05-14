import pygame, sys
pygame.init()


telova = (255, 186, 141)
hneda = (85, 33, 0)
modra_mouchy =(165, 199, 206)
cerna = (0, 0, 0)

window = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("ˇIsaacˇ")
rect_x, rect_y = 70, 500
rext_x, rext_y = rect_x, rect_y
WIDTH, HEIGHT = 1500, 1000
clock = pygame.time.Clock()
postava = pygame.image.load("pixelovy_isaac_vetsi.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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

    rect_x = max(0, min(rect_x, WIDTH - 100))
    rect_y = max(0, min(rect_y, HEIGHT - 100))

    isaac = window.blit(postava, (rect_x, rect_y))


    
    pygame.display.update()
    clock.tick(30)