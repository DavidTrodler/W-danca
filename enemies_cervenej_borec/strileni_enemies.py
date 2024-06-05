def pozice(pozice_postavy_x, pozice_postavy_y, rect_x, rect_y):
    if rect_x > pozice_postavy_x:
        pozice_postavy_x += 0.5
    if rect_x < pozice_postavy_x:
        pozice_postavy_x -= 0.5
    if rect_y > pozice_postavy_y:    
        pozice_postavy_y += 0.5
    if rect_y < pozice_postavy_y:       
        pozice_postavy_y -= 0.5
    return pozice_postavy_x, pozice_postavy_y