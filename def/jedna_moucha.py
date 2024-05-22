import pygame

def muska(rect_x, moucha_x, rect_y, moucha_y):
    if rect_x > moucha_x:
        moucha_x += 0.5
    if rect_x < moucha_x:
        moucha_x -= 0.5
    if rect_y > moucha_y:    
        moucha_y += 0.5
    if rect_y < moucha_y:       
        moucha_y -= 0.5
    return [moucha_x, moucha_y]


"""
    musi_pozice = osm_much(rect_x, moucha_x, rect_y, moucha_y)
    if hp_mouchy > 0:
        angry_moucha = window.blit(moucha, (musi_pozice[0], musi_pozice[1]))
        if isaac.colliderect(angry_moucha):
            srd -= 0.5
"""