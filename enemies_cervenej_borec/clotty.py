def clotty_moves(rect_x, rect_y, moucha_x, moucha_y):
    if rect_x > moucha_x:
        moucha_x += 0.5
    if rect_x < moucha_x:
        moucha_x -= 0.5
    if rect_y > moucha_y:    
        moucha_y += 0.5
    if rect_y < moucha_y:       
        moucha_y -= 0.5
    
    return moucha_x, moucha_y


    """
    if hp_mouchy > 0:
        angry_moucha = window.blit(moucha, (moucha_x, moucha_y))
        if isaac.colliderect(angry_moucha):
            frst_srd -= 0.5

    up_cervenej = window.blit(slza, (cervenej_projectiles_up_x, cervenej_projectiles_up_y))
    cervenej_projectiles_up_y -= 5
    if up_cervenej.colliderect(isaac):
        frst_srd -= 0.5

    down_cervenej = window.blit(slza, (cervenej_projectiles_down_x, cervenej_projectiles_down_y))
    cervenej_projectiles_down_y += 5
    if down_cervenej.colliderect(isaac):
        frst_srd -= 0.5

    left_cervenej = window.blit(slza, (cervenej_projectiles_left_x, cervenej_projectiles_left_y))
    cervenej_projectiles_left_x -= 5
    if left_cervenej.colliderect(isaac):
        frst_srd -= 0.5

    right_cervenej = window.blit(slza, (cervenej_projectiles_right_x, cervenej_projectiles_right_y))
    cervenej_projectiles_right_x += 5
    if right_cervenej.colliderect(isaac):
        frst_srd -= 0.5

    cas -= 1
    """

    
def clotty_cooldown(cas, moucha_x, moucha_y, cervenej_projectiles_up_y, cervenej_projectiles_up_x, cervenej_projectiles_down_y, cervenej_projectiles_down_x, cervenej_projectiles_left_x, cervenej_projectiles_left_y, cervenej_projectiles_right_x, cervenej_projectiles_right_y):
    if cas == 0:
        cervenej_projectiles_up_y = moucha_y
        cervenej_projectiles_up_x = moucha_x
        cervenej_projectiles_down_y = moucha_y
        cervenej_projectiles_down_x = moucha_x
        cervenej_projectiles_left_x = moucha_x
        cervenej_projectiles_left_y = moucha_y
        cervenej_projectiles_right_x = moucha_x
        cervenej_projectiles_right_y = moucha_y
        cas = 120
    return cas, cervenej_projectiles_up_y, cervenej_projectiles_up_x, cervenej_projectiles_down_y, cervenej_projectiles_down_x, cervenej_projectiles_left_x, cervenej_projectiles_left_y, cervenej_projectiles_right_x, cervenej_projectiles_right_y