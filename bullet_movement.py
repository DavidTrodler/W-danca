    
def bullet_movement(projectile_speed, projectile_speed_diagonal, WIDTH, HEIGHT, player_projectiles_up, player_projectiles_up_left, player_projectiles_up_right, player_projectiles_down, player_projectiles_down_left, player_projectiles_down_right, player_projectiles_left, player_projectiles_left_down, player_projectiles_left_up, player_projectiles_right, player_projectiles_right_down, player_projectiles_right_up, new_player_projectiles_UP, new_player_projectiles_UP_LEFT, new_player_projectiles_UP_RIGHT, new_player_projectiles_DOWN, new_player_projectiles_DOWN_LEFT, new_player_projectiles_DOWN_RIGHT, new_player_projectiles_LEFT, new_player_projectiles_LEFT_DOWN, new_player_projectiles_LEFT_UP, new_player_projectiles_RIGHT, new_player_projectiles_RIGHT_DOWN, new_player_projectiles_RIGHT_UP):
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y in player_projectiles_up:
            proj_y -= projectile_speed
            if proj_y > 0:
                new_player_projectiles_UP.append((proj_x, proj_y))
        player_projectiles_up = new_player_projectiles_UP
    #UP_LEFT
    if len(player_projectiles_up_left) > 0:
        for proj_x, proj_y in player_projectiles_up_left:
            proj_y -= projectile_speed
            proj_x -= projectile_speed_diagonal
            if proj_y > 0 or proj_x > 0:
                new_player_projectiles_UP_LEFT.append((proj_x, proj_y))
        player_projectiles_up_left = new_player_projectiles_UP_LEFT
    #UP_RIGHT
    if len(player_projectiles_up_right) > 0:
        for proj_x, proj_y in player_projectiles_up_right:
            proj_y -= projectile_speed
            proj_x += projectile_speed_diagonal
            if proj_y > 0 or proj_x < WIDTH:
                new_player_projectiles_UP_RIGHT.append((proj_x, proj_y))
        player_projectiles_up_right = new_player_projectiles_UP_RIGHT

    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y in player_projectiles_down:
            proj_y += projectile_speed
            if proj_y < HEIGHT:
                new_player_projectiles_DOWN.append((proj_x, proj_y))
        player_projectiles_down = new_player_projectiles_DOWN
    #DOWN_LEFT
    if len(player_projectiles_down_left) > 0:
        for proj_x, proj_y in player_projectiles_down_left:
            proj_y += projectile_speed
            proj_x -= projectile_speed_diagonal
            if proj_y < HEIGHT or proj_x < 0:
                new_player_projectiles_DOWN_LEFT.append((proj_x, proj_y))
        player_projectiles_down_left = new_player_projectiles_DOWN_LEFT
    #DOWN_RIGHT
    if len(player_projectiles_down_right) > 0:
        for proj_x, proj_y in player_projectiles_down_right:
            proj_y += projectile_speed
            proj_x += projectile_speed_diagonal
            if proj_y < HEIGHT or proj_x < WIDTH:
                new_player_projectiles_DOWN_RIGHT.append((proj_x, proj_y))
        player_projectiles_down_right = new_player_projectiles_DOWN_RIGHT
    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y in player_projectiles_left:
            proj_x -= projectile_speed
            if proj_x > 0:
                new_player_projectiles_LEFT.append((proj_x, proj_y))
        player_projectiles_left = new_player_projectiles_LEFT
    #LEFT_DOWN
    if len(player_projectiles_left_down) > 0:
        for proj_x, proj_y in player_projectiles_left_down:
            proj_x -= projectile_speed
            proj_y += projectile_speed_diagonal
            if proj_x > 0 or proj_y < HEIGHT:
                new_player_projectiles_LEFT_DOWN.append((proj_x, proj_y))
        player_projectiles_left_down = new_player_projectiles_LEFT_DOWN
    #LEFT_UP
    if len(player_projectiles_left_up) > 0:
        for proj_x, proj_y in player_projectiles_left_up:
            proj_x -= projectile_speed
            proj_y -= projectile_speed_diagonal
            if proj_x > 0 or proj_y > 0:
                new_player_projectiles_LEFT_UP.append((proj_x, proj_y))
        player_projectiles_left_up = new_player_projectiles_LEFT_UP
    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y in player_projectiles_right:
            proj_x += projectile_speed
            if proj_x < WIDTH:
                new_player_projectiles_RIGHT.append((proj_x, proj_y))
        player_projectiles_right = new_player_projectiles_RIGHT
    #RIGHT_DOWN
    if len(player_projectiles_right_down) > 0:
        for proj_x, proj_y in player_projectiles_right_down:
            proj_x += projectile_speed
            proj_y += projectile_speed_diagonal
            if proj_x < WIDTH or proj_y < HEIGHT:
                new_player_projectiles_RIGHT_DOWN.append((proj_x, proj_y))
        player_projectiles_right_down = new_player_projectiles_RIGHT_DOWN
    #RIGHT_UP
    if len(player_projectiles_right_up) > 0:
        for proj_x, proj_y in player_projectiles_right_up:
            proj_x += projectile_speed
            proj_y -= projectile_speed_diagonal
            if proj_x < WIDTH or proj_y > 0:
                new_player_projectiles_RIGHT_UP.append((proj_x, proj_y))
        player_projectiles_right_up = new_player_projectiles_RIGHT_UP
    return player_projectiles_up, player_projectiles_up_left, player_projectiles_up_right, player_projectiles_down, player_projectiles_down_left, player_projectiles_down_right, player_projectiles_left, player_projectiles_left_down, player_projectiles_left_up, player_projectiles_right, player_projectiles_right_down, player_projectiles_right_up