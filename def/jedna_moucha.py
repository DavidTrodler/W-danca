import pygame

def osm_much(rect_x, moucha_x, rect_y, moucha_y):
    if rect_x > moucha_x:
        moucha_x += 0.5
    if rect_x < moucha_x:
        moucha_x -= 0.5
    if rect_y > moucha_y:    
        moucha_y += 0.5
    if rect_y < moucha_y:       
        moucha_y -= 0.5

    return [moucha_x, moucha_y]