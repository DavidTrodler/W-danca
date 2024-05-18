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

    return numbers_of_new_rooms

print(cislicka(2))