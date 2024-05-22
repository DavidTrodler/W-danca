import pygame
from jedna_moucha import muska

def druha_roomka(rect_x, rect_y, srd, window, isaac):
    prvni_moucha_x, prvni_moucha_y = 80, 30
    prvni_moucha = pygame.image.load("def/moucha.png")
    musi_pozice = muska(rect_x, prvni_moucha_x, rect_y, prvni_moucha_y)
    moucha_x = musi_pozice[0]
    moucha_y = musi_pozice[1]
    if hp_mouchy > 0:
        angry_moucha = window.blit(prvni_moucha, (moucha_x, moucha_y))
        if isaac.colliderect(angry_moucha):
            srd -= 0.5
    musi_pozice = []

druha_roomka()