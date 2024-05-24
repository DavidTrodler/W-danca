import random
rooms = [1,6,2,3,13,4,5,6,20]
level = 1
print(random.randint(1, 10))

def items():
    items_crap = {}
    items_common = {'sword': [-2, +3, 0, 0, 0, 1, 0], 'shield': [-1, 0, 0, 3, 0, 0, 0], 'potion': [1, 1, 1, 0, 0, 0, 0], 'hearth': [0, 0, 1, 0, 0, 0, 0]} #Name: speed, damage, health, total health, projectile speed, reload time, lives
    items_epic = {} #Name: speed, damage, health, total health, projectile speed, reload time, lives
    items_legendary = {} #Name: speed, damage, health, total health, projectile speed, reload time, lives
    items_mythical = {} #Name: speed, damage, health, total health, projectile speed, reload time, lives
    return items_crap, items_common, items_epic, items_legendary, items_mythical


def item_room_randomizer(rooms, level):
    item_in_room = {}
    total_items = 0

    for room in rooms:
        item_in_room[room] = False

    for room in rooms:
        if not item_in_room[room] and random.randint(1, len(rooms)) == 1:
            item_in_room[room] = True
            total_items += 1
            if total_items == level:
                break
    print(item_in_room, level)
    return rooms


#Určuje, jaké předměty dostanete po zabití všech monster v roomce
def room_reward(level):
    items_to_append = {}
    items_crap, items_common, items_epic, items_legendary, items_mythical = items()
    number_of_items = random.randint(0, 5)
    while len(items_to_append) < number_of_items:
        if random.randint(1, 5) == 1:
            random_number = random.randint(1, len(items_crap)-1)
            items_to_append[random_number] = items_crap[random_number]
        elif random.randint(1, 10) == 1:
            random_number = random.randint(1, len(items_common)-1)
            items_to_append[random_number] = items_common[random_number]
        elif random.randint(1, 20) == 1 and level > 1:
            random_number = random.randint(1, len(items_epic)-1)
            items_to_append[random_number] = items_epic[random_number]
        elif random.randint(1, 30) == 1 and level > 2:
            random_number = random.randint(1, len(items_legendary)-1)
            items_to_append[random_number] = items_legendary[random_number]
        elif random.randint(1, 100) == 1 and level > 3:
            random_number = random.randint(1, len(items_mythical)-1)
            items_to_append[random_number] = items_mythical[random_number]

    return items_to_append
    


item_room_randomizer(rooms)