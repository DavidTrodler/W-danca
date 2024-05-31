    
def bullet_movement(projectile_speed, WIDTH, HEIGHT, player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, new_player_projectiles_UP, new_player_projectiles_DOWN, new_player_projectiles_LEFT, new_player_projectiles_RIGHT):
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_up:
            proj_y -= projectile_speed - y
            proj_x += x

            if time > 0:
                if proj_y > 0:
                    time -= 1
                    new_player_projectiles_UP.append((proj_x, proj_y, x, y, time))

        player_projectiles_up = new_player_projectiles_UP

    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_down:
            proj_y += projectile_speed + y
            proj_x += x
            if time > 0:
                if proj_y < HEIGHT:
                    time -= 1
                    new_player_projectiles_DOWN.append((proj_x, proj_y, x, y, time))

        player_projectiles_down = new_player_projectiles_DOWN

    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_left:
            proj_x -= projectile_speed - x
            proj_y += y
            if time > 0:
                if proj_x > 0:
                    time -= 1
                    new_player_projectiles_LEFT.append((proj_x, proj_y, x, y, time))

        player_projectiles_left = new_player_projectiles_LEFT

    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_right:
            proj_x += projectile_speed + x
            proj_y += y
            if time > 0:
                if proj_x < WIDTH:
                    time -= 1
                    new_player_projectiles_RIGHT.append((proj_x, proj_y, x, y, time))
        player_projectiles_right = new_player_projectiles_RIGHT

    return player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right
