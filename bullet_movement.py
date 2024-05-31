import pygame   
def bullet_movement(projectile_speed, WIDTH, HEIGHT, player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right, new_player_projectiles_UP, new_player_projectiles_DOWN, new_player_projectiles_LEFT, new_player_projectiles_RIGHT, no_entry_area_x, no_entry_area_y, projectile_size):
    
    
    #UP
    if len(player_projectiles_up) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_up:
            proj_y -= projectile_speed - y
            proj_x += x
            is_bullet = True
            for i,ii in zip(no_entry_area_x, no_entry_area_y):
                prekazka = pygame.Rect(i, ii, 50, 50)
                projektil = pygame.Rect(proj_x, proj_y, projectile_size, projectile_size)
                if projektil.colliderect(prekazka):
                    is_bullet = False
            if time > 0 and is_bullet:
                if proj_y > 0:
                    time -= 1
                    new_player_projectiles_UP.append((proj_x, proj_y, x, y, time))

        player_projectiles_up = new_player_projectiles_UP

    #DOWN
    if len(player_projectiles_down) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_down:
            proj_y += projectile_speed + y
            proj_x += x
            is_bullet = True
            for i,ii in zip(no_entry_area_x, no_entry_area_y):
                prekazka = pygame.Rect(i, ii, 50, 50)
                projektil = pygame.Rect(proj_x, proj_y, projectile_size, projectile_size)
                if projektil.colliderect(prekazka):
                    is_bullet = False
            if time > 0 and is_bullet:
                if proj_y < HEIGHT:
                    time -= 1
                    new_player_projectiles_DOWN.append((proj_x, proj_y, x, y, time))

        player_projectiles_down = new_player_projectiles_DOWN

    #LEFT
    if len(player_projectiles_left) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_left:
            proj_x -= projectile_speed - x
            proj_y += y
            is_bullet = True
            for i,ii in zip(no_entry_area_x, no_entry_area_y):
                prekazka = pygame.Rect(i, ii, 50, 50)
                projektil = pygame.Rect(proj_x, proj_y, projectile_size, projectile_size)
                if projektil.colliderect(prekazka):
                    is_bullet = False
            if time > 0 and is_bullet:
                if proj_x > 0:
                    time -= 1
                    new_player_projectiles_LEFT.append((proj_x, proj_y, x, y, time))

        player_projectiles_left = new_player_projectiles_LEFT

    #RIGHT
    if len(player_projectiles_right) > 0:
        for proj_x, proj_y, x, y, time in player_projectiles_right:
            proj_x += projectile_speed + x
            proj_y += y
            is_bullet = True
            for i,ii in zip(no_entry_area_x, no_entry_area_y):
                prekazka = pygame.Rect(i, ii, 50, 50)
                projektil = pygame.Rect(proj_x, proj_y, projectile_size, projectile_size)
                if projektil.colliderect(prekazka):
                    is_bullet = False
            if time > 0 and is_bullet:
                if proj_x < WIDTH:
                    time -= 1
                    new_player_projectiles_RIGHT.append((proj_x, proj_y, x, y, time))
        player_projectiles_right = new_player_projectiles_RIGHT

    return player_projectiles_up, player_projectiles_down, player_projectiles_left, player_projectiles_right
