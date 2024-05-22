def pohyby_mapy(image_width, image_height, move_side_counter, move_up_counter, move_side, move_up):
    # Room numbers
    #První
    prvni = [775 , 100] #POKUD CHCEŠ ZMĚNIT UMÍSTĚNÍ MAPY, ZMĚŇ UMÍSTĚNÍ PRVNÍ ROOMKY   
                #---Pokračuje na konci funkce---

    #Druhá
    druha = [0,0]
    druha[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    #<-----Posune se ošířku obrázku (image_width) do boku, násobí se podle závislosti na roomce č. jedna. (viz excell)
    druha[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Třetí
    treti = [0,0]
    treti[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    treti[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Čtvrtá
    ctvrta = [0,0]
    ctvrta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    ctvrta[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Pátá
    pata = [0,0]
    pata[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    pata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Šestá
    sesta = [0,0]
    sesta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    sesta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Sedmá
    sedma = [0,0]
    sedma[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    sedma[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Osmá
    osma = [0,0]
    osma[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    osma[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Devátá
    devata = [0,0]
    devata[0] = prvni[0] + (image_width * 1) + (move_side[0] * move_side_counter)
    devata[1] = prvni[1] + (image_height * (-1)) + (move_up[1] * move_up_counter)
    print(devata)
    #Desátá   x     y
    desata = [0,0]
    desata[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    desata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Jedenáctá
    jedenacta = [0,0]
    jedenacta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    jedenacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvanáctá
    dvanacta = [0,0]
    dvanacta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvanacta[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Třináctá
    trinacta = [0,0]
    trinacta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    trinacta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Čtrnáctá   x    y 
    ctrnacta = [0,0]
    ctrnacta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    ctrnacta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Patnáctá
    patnacta = [0,0]
    patnacta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    patnacta[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Šestnáctá
    sestnacta = [0,0]
    sestnacta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    sestnacta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Sedmnáctá
    sedmnacta = [0,0]
    sedmnacta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    sedmnacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Osmnáctá
    osmnacta = [0,0]
    osmnacta[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    osmnacta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Devatenáctá
    devatenacta = [0,0]
    devatenacta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    devatenacta[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Dvacátá
    dvacata = [0,0]
    dvacata[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacata[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Dvacátá první
    dvacataprvni = [0,0]
    dvacataprvni[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    dvacataprvni[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá druhá
    dvacatadruha = [0,0]
    dvacatadruha[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    dvacatadruha[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá třetí
    dvacatatreti = [0,0]
    dvacatatreti[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    dvacatatreti[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvacátá čtvrtá
    dvacatactvrta = [0,0]
    dvacatactvrta[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacatactvrta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Dvacátá pátá
    dvacatapata = [0,0]
    dvacatapata[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    dvacatapata[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Dvacátá šestá
    dvacatasesta = [0,0]
    dvacatasesta[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    dvacatasesta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Dvacátá sedmá
    dvacatasedma = [0,0]
    dvacatasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    dvacatasedma[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Dvacátá osmá
    dvacataosma = [0,0]
    dvacataosma[0] = prvni[0] + image_width * 0 + (move_side[0] * move_side_counter)
    dvacataosma[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Dvacátá devátá
    dvacatadevata = [0,0]
    dvacatadevata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    dvacatadevata[1] = prvni[1] + image_height * 0 + (move_up[1] * move_up_counter)

    #Třicátá
    tricata = [0,0]
    tricata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    tricata[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Třicátá první
    tricataprvni = [0,0]
    tricataprvni[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    tricataprvni[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Třicátá druhá
    tricatadruha = [0,0]
    tricatadruha[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    tricatadruha[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá třetí
    tricatatreti = [0,0]
    tricatatreti[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    tricatatreti[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá čtvrtá
    tricatactvrta = [0,0]
    tricatactvrta[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    tricatactvrta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá pátá
    tricatapata = [0,0]
    tricatapata[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    tricatapata[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Třicátá šestá
    tricatasesta = [0,0]
    tricatasesta[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatasesta[1] = prvni[1] + image_height * (-2) + (move_up[1] * move_up_counter)

    #Třicátá sedmá
    tricatasedma = [0,0]
    tricatasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatasedma[1] = prvni[1] + image_height * (-1) + (move_up[1] * move_up_counter)

    #Třicátá osmá
    tricataosma = [0,0]
    tricataosma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricataosma[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Třicátá devátá
    tricatadevata = [0,0]
    tricatadevata[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    tricatadevata[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Čtyřicátá
    ctyracta = [0,0]
    ctyracta[0] = prvni[0] + image_width * 2 + (move_side[0] * move_side_counter)
    ctyracta[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá první
    ctyractaprvni = [0,0]
    ctyractaprvni[0] = prvni[0] + image_width * 1 + (move_side[0] * move_side_counter)
    ctyractaprvni[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá druhá
    ctyractadruha = [0,0]
    ctyractadruha[0] = prvni[0] + image_width * (-1) + (move_side[0] * move_side_counter)
    ctyractadruha[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá třetí
    ctyratatreti = [0,0]
    ctyratatreti[0] = prvni[0] + image_width * (-2) + (move_side[0] * move_side_counter)
    ctyratatreti[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá čtvrtá
    ctyratactvrta = [0,0]
    ctyratactvrta[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratactvrta[1] = prvni[1] + image_height * 2 + (move_up[1] * move_up_counter)

    #Čtyřicátá pátá
    ctyratapata = [0,0]
    ctyratapata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratapata[1] = prvni[1] + image_height * 1 + (move_up[1] * move_up_counter)

    #Čtyřicátá šestá
    ctyratasesta = [0,0]
    ctyratasesta[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratasesta[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Čtyřicátá sedmá
    ctyratasedma = [0,0]
    ctyratasedma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    ctyratasedma[1] = prvni[1] + image_height * (-3) + (move_up[1] * move_up_counter)

    #Čtyřicátá osmá
    ctyrataosma = [0,0]
    ctyrataosma[0] = prvni[0] + image_width * 3 + (move_side[0] * move_side_counter)
    ctyrataosma[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)

    #Čtyřicátá devátá
    ctyratadevata = [0,0]
    ctyratadevata[0] = prvni[0] + image_width * (-3) + (move_side[0] * move_side_counter)
    ctyratadevata[1] = prvni[1] + image_height * 3 + (move_up[1] * move_up_counter)
    

    # Zase první
    prvni[0] = prvni[0] + (move_side[0] * move_side_counter)
    prvni[1] = prvni[1] + (move_up[1] * move_up_counter)
    return prvni, druha, treti, ctvrta, pata, sesta, sedma, osma, devata, desata, jedenacta, dvanacta, trinacta, ctrnacta, patnacta, sestnacta, sedmnacta, osmnacta, devatenacta, dvacata, dvacataprvni, dvacatadruha, dvacatatreti, dvacatactvrta, dvacatapata, dvacatasesta, dvacatasedma, dvacataosma, dvacatadevata, tricata, tricataprvni, tricatadruha, tricatatreti, tricatactvrta, tricatapata, tricatasesta, tricatasedma, tricataosma, tricatadevata, ctyracta, ctyractaprvni, ctyractadruha, ctyratatreti, ctyratactvrta, ctyratapata, ctyratasesta, ctyratasedma, ctyrataosma, ctyratadevata
