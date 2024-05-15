import pygame
import sys
import random
import time

enemies = []
move = []
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.clock = pygame.time.Clock()
while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                enemies.append([random.randint(0, 800), random.randint(0, 600)])
    screen.fill((0, 0, 0))
    for enemy in enemies:
        if "left" in move:
            enemy[0] -= 5
        if "right" in move:
            enemy[0] += 5
        if "up" in move:
            enemy[1] -= 5
        if "down" in move:
            enemy[1] += 5
        if move == []:
            if enemy[0] > 400:
                move.append("down")
            if enemy[0] < 800:
                move.append("up")
            if enemy[1] > 300:
                move.append("right")
            if enemy[1] < 300:
                move.append("left")    
            print(move)
        if enemy[1] > 600:
            enemies.remove(enemy)   
        pygame.draw.circle(screen, (255, 0, 0), (enemy[0], enemy[1]), 10)
    pygame.display.flip()
    pygame.clock.tick(30)
