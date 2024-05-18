import pygame, sys
from random import randint, sample
def cislicka(room):
    first_rooms = [2, 3, 4, 5]
    second = [1, 7, 6]
    third = [1, 7, 8,]
    fourth = [1, 8, 9]
    fifth = [1, 6, 9]
    sixth = [2, 5]
    seventh = [2, 3]
    eighth = [3, 4]
    ninth = [4, 5]

    if room == 1:
        moznosti = first_rooms
    elif room == 2:
        moznosti = second
    elif room == 3:
        moznosti = third
    elif room == 4:
        moznosti = fourth
    elif room == 5:
        moznosti = fifth
    elif room == 6:
        moznosti = sixth
    elif room == 7:
        moznosti = seventh
    elif room == 8:
        moznosti = eighth
    elif room == 9:
        moznosti = ninth
    
    number_of_rooms = randint(1, len(moznosti))
    numbers_of_new_rooms = sample(moznosti, number_of_rooms)
    if 1 not in numbers_of_new_rooms:
        numbers_of_new_rooms.append(1)
    return numbers_of_new_rooms

def sides(numbers_of_new_rooms, room):
    sideing = []
    left = False
    right = False
    up = False
    down = False
    if room == 1:
        if 3 in numbers_of_new_rooms:
            left = True
        if 5 in numbers_of_new_rooms:
            right = True
        if 4 in numbers_of_new_rooms:
            up = True
        if 2 in numbers_of_new_rooms:
            down = True
    elif room == 2:
        if 7 in numbers_of_new_rooms:
            left = True
        if 6 in numbers_of_new_rooms:
            right = True
        if 1 in numbers_of_new_rooms:
            up = True
        if 11 in numbers_of_new_rooms:
            down = True
    elif room == 3:
        if 12 in numbers_of_new_rooms:
            left = True
        if 1 in numbers_of_new_rooms:
            right = True
        if 8 in numbers_of_new_rooms:
            up = True
        if 7 in numbers_of_new_rooms:
            down = True
    elif room == 4:
        if 13 in numbers_of_new_rooms:
            left = True
        if 8 in numbers_of_new_rooms:
            right = True
        if 9 in numbers_of_new_rooms:
            up = True
        if 1 in numbers_of_new_rooms:
            down = True
    elif room == 5:
        if 1 in numbers_of_new_rooms:
            left = True
        if 10 in numbers_of_new_rooms:
            right = True
        if 9 in numbers_of_new_rooms:
            up = True
        if 6 in numbers_of_new_rooms:
            down = True
    elif room == 6:
        if 2 in numbers_of_new_rooms:
            left = True
        if 16 in numbers_of_new_rooms:
            right = True
        if 5 in numbers_of_new_rooms:
            up = True
        if 17 in numbers_of_new_rooms:
            down = True
    elif room == 7:
        if 19 in numbers_of_new_rooms:
            left = True
        if 2 in numbers_of_new_rooms:
            right = True
        if 3 in numbers_of_new_rooms:
            up = True
        if 18 in numbers_of_new_rooms:
            down = True
    elif room == 8:
        if 20 in numbers_of_new_rooms:
            left = True
        if 4 in numbers_of_new_rooms:
            right = True
        if 21 in numbers_of_new_rooms:
            up = True
        if 3 in numbers_of_new_rooms:
            down = True
    elif room == 9:
        if 4 in numbers_of_new_rooms:
            left = True
        if 15 in numbers_of_new_rooms:
            right = True
        if 14 in numbers_of_new_rooms:
            up = True
        if 5 in numbers_of_new_rooms:
            down = True

    sideing.append(left)
    sideing.append(right)
    sideing.append(up)
    sideing.append(down)
    return sideing

print(sides(cislicka(1), 1))