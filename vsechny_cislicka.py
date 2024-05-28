#color constants
def telova_barva():
    telova = (255, 186, 141)
    return telova
def hneda_barva():
    hneda = (85, 33, 0)
    return hneda
def modra_mouchy_barva():
    modra_mouchy = (165, 199, 206)
    return modra_mouchy
def cerna_barva():
    cerna = (0, 0, 0)
    return cerna

#minimap width, height
def sirka_obrazku():
    sirka = 60
    return sirka
def vyska_obrazku():
    vyska = 30
    return vyska

#map width, height
def width_mapy():
    width = 1000
    return width
def height_mapy():
    height = 600
    return height

#level
def level():
    level = 30
    return level

# Player variables
def rect_x():
    rect_x = 70
    return rect_x
def rect_y():
    rect_y = 70
    return rect_y
def velikost_postavy():
    velikost = 57
    return velikost
def projectile_size():
    projectile_size = 10
    return projectile_size
def projectile_speed():
    projectile_speed = 10
    return projectile_speed
def projectile_speed_diagonal():
    projectile_speed_diagonal = 4
    return projectile_speed_diagonal

#shooting cooldown
def cooldown():
    cooldown = 0
    return cooldown
def cooldown_time():
    cooldown_time = 10
    return cooldown_time

#map
def move_up_counter():
    move_up_counter = 0
    return move_up_counter
def move_side_counter():
    move_side_counter = 0
    return move_side_counter
def current_room():
    current_room = 1
    return current_room

#Dveře, ukazuje, kam se mají osy posunout
def dvere_up_value():
    dvere_up_value = 1
    return dvere_up_value
def dvere_down_value():
    dvere_down_value = -1
    return dvere_down_value
def dvere_left_value():
    dvere_left_value = 1
    return dvere_left_value
def dvere_right_value():
    dvere_right_value = -1
    return dvere_right_value
def dvere_up():
    dvere_up = False
    return dvere_up
def dvere_down():
    dvere_down = False
    return dvere_down
def dvere_left():
    dvere_left = False
    return dvere_left
def dvere_right():
    dvere_right = False
    return dvere_right

#

#Lists
#UP
def player_projectiles_up():
    player_projectiles_up = []
    return player_projectiles_up
def player_projectiles_up_left():
    player_projectiles_up_left = []
    return player_projectiles_up_left
def player_projectiles_up_right():
    player_projectiles_up_right = []
    return player_projectiles_up_right
#DOWN
def player_projectiles_down():
    player_projectiles_down = []
    return player_projectiles_down
def player_projectiles_down_left():
    player_projectiles_down_left = []
    return player_projectiles_down_left
def player_projectiles_down_right():
    player_projectiles_down_right = []
    return player_projectiles_down_right
#LEFT
def player_projectiles_left():
    player_projectiles_left = []
    return player_projectiles_left
def player_projectiles_left_down():
    player_projectiles_left_down = []
    return player_projectiles_left_down
def player_projectiles_left_up():
    player_projectiles_left_up = []
    return player_projectiles_left_up
#RIGHT
def player_projectiles_right():
    player_projectiles_right = []
    return player_projectiles_right
def player_projectiles_right_down():
    player_projectiles_right_down = []
    return player_projectiles_right_down
def player_projectiles_right_up():
    player_projectiles_right_up = []
    return player_projectiles_right_up
#ALL
def projectiles():
    projectiles = []
    return projectiles
#Map
def move_up():
    move_up = [0, 30]
    return move_up
def move_side():
    move_side = [60, 0]
    return move_side
def image_filter_position():
    image_filter_position = [775, 100]
    return image_filter_position

#Rooms list
def rooms():
    rooms = [1]
    return rooms
def rooms_dict():
    rooms_dict = {}
    return rooms_dict

def door_cooldown():
    door_cooldown = 0
    return door_cooldown
def door_cooldown_time():
    door_cooldown_time = 20
    return door_cooldown_time
