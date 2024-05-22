
#Určuje, zda jsou roomky v seznamu rooms
def set_statements(rooms):
    statements = {}
    for i in range(1, 50):
        key = f"{i}_statement"
        statements[key] = True if i in rooms else False
    return statements

#Rozhoduje, zda budou v místnostech dveře (UP, RIGHT, DOWN, LEFT)
def rooms_dictionary_funciton(rooms):
    doors_dictionary = {0: [False, False, False, False]} 
    for i in range(1, 50):
        doors_dictionary[i] = [False, False, False, False]



    if 1 in rooms:
        #Čtyři
        doors_dictionary[4][2] = True
        #Pět
        doors_dictionary[5][3] = True
        #Dva
        doors_dictionary[2][0] = True
        #Tři
        doors_dictionary[3][1] = True
    if 2 in rooms:
        #Jedna
        doors_dictionary[1][2] = True
        #Šest
        doors_dictionary[6][3] = True
        #Jedenáct
        doors_dictionary[11][0] = True
        #Sedm
        doors_dictionary[7][1] = True
    if 3 in rooms:
        #Osm
        doors_dictionary[8][2] = True
        #Jedna
        doors_dictionary[1][3] = True
        #Sedm
        doors_dictionary[7][0] = True
        #Dvanáct
        doors_dictionary[12][1] = True
    if 4 in rooms:
        #Třináct
        doors_dictionary[13][2] = True
        #Devět
        doors_dictionary[9][3] = True
        #Jedna
        doors_dictionary[1][0] = True
        #Osm
        doors_dictionary[8][1] = True
    if 5 in rooms:
        #Devět
        doors_dictionary[9][2] = True
        #Deset
        doors_dictionary[10][3] = True
        #Šest
        doors_dictionary[6][0] = True
        #Jedna
        doors_dictionary[1][1] = True
    if 6 in rooms:
        #Pět
        doors_dictionary[5][2] = True
        #Šestnáct
        doors_dictionary[16][3] = True
        #Sedmnáct
        doors_dictionary[17][0] = True
        #Dva
        doors_dictionary[2][1] = True
    if 7 in rooms:
        #Tři
        doors_dictionary[3][2] = True
        #Dva
        doors_dictionary[2][3] = True
        #Osmnáct
        doors_dictionary[18][1] = True
        #Devatenáct
        doors_dictionary[19][0] = True
    if 8 in rooms:
        #Dvacetjedna
        doors_dictionary[21][2] = True
        #Čtyři
        doors_dictionary[4][3] = True
        #Tři
        doors_dictionary[3][0] = True
        #Dvacet
        doors_dictionary[20][1] = True
    if 9 in rooms:
        #Čtrnáct
        doors_dictionary[14][2] = True
        #Patnáct
        doors_dictionary[15][3] = True
        #Pět
        doors_dictionary[5][0] = True
        #Čtyři
        doors_dictionary[4][1] = True
    if 10 in rooms:
        #Patnáct
        doors_dictionary[15][2] = True
        #Dvacetsedm
        doors_dictionary[27][3] = True
        #Šestnáct
        doors_dictionary[16][0] = True
        #Pět
        doors_dictionary[5][1] = True
    if 11 in rooms:
        #Dva
        doors_dictionary[2][2] = True
        #Sedmnáct
        doors_dictionary[17][3] = True
        #Dvacetosm
        doors_dictionary[28][0] = True
        #Osmnáct
        doors_dictionary[18][1] = True
    if 12 in rooms:
        #Dvacet
        doors_dictionary[20][2] = True
        #Tři
        doors_dictionary[3][3] = True
        #Devatenáct
        doors_dictionary[19][0] = True
        #Dvacetdevět
        doors_dictionary[29][1] = True
    if 13 in rooms:
        #Dvacetšest
        doors_dictionary[26][2] = True
        #Čtrnáct
        doors_dictionary[14][3] = True
        #Čtyři
        doors_dictionary[4][0] = True
        #Dvacetjedna
        doors_dictionary[21][1] = True
    if 14 in rooms:
        #Třicetčtyři
        doors_dictionary[34][2] = True
        #Dvacetdva
        doors_dictionary[22][3] = True
        #Devět
        doors_dictionary[9][0] = True
        #Třináct
        doors_dictionary[13][1] = True
    if 15 in rooms:
        #Dvacetdva
        doors_dictionary[22][2] = True
        #Třicetsedm
        doors_dictionary[37][3] = True
        #Deset
        doors_dictionary[10][0] = True
        #Devět
        doors_dictionary[9][1] = True
    if 16 in rooms:
        #Deset
        doors_dictionary[10][2] = True
        #Třicetosm
        doors_dictionary[38][3] = True
        #Dvacettři
        doors_dictionary[23][0] = True
        #Šest
        doors_dictionary[6][1] = True
    if 17 in rooms:
        #Šest
        doors_dictionary[6][2] = True
        #Dvacettři
        doors_dictionary[23][3] = True
        #Čtyřicetjedna
        doors_dictionary[41][0] = True
        #Jedenáct
        doors_dictionary[11][1] = True
    if 18 in rooms:
        #Sedm
        doors_dictionary[7][2] = True
        #Jedenáct
        doors_dictionary[11][3] = True
        #Čtyřicetdva
        doors_dictionary[42][0] = True
        #Dvacetčtyři
        doors_dictionary[24][1] = True
    if 19 in rooms:
        #Dvanáct
        doors_dictionary[12][2] = True
        #Sedm
        doors_dictionary[7][3] = True
        #Dvacetčtyři
        doors_dictionary[24][0] = True
        #Čtyřicetpět
        doors_dictionary[45][1] = True
    if 20 in rooms:
        #Dvacetpět
        doors_dictionary[25][2] = True
        #Osm
        doors_dictionary[8][3] = True
        #Dvanáct
        doors_dictionary[12][0] = True
        #Třicet
        doors_dictionary[30][1] = True
    if 21 in rooms:
        #Třicettři
        doors_dictionary[33][2] = True
        #Třináct
        doors_dictionary[13][3] = True
        #Osm
        doors_dictionary[8][0] = True
        #Dvacetpět
        doors_dictionary[25][1] = True
    if 22 in rooms:
        #Třicetpět
        doors_dictionary[35][2] = True
        #Třicetšest
        doors_dictionary[36][3] = True
        #Patnáct
        doors_dictionary[15][0] = True
        #Čtrnáct
        doors_dictionary[14][1] = True
    if 23 in rooms:
        #Šestnáct
        doors_dictionary[16][2] = True
        #Třicetdevět
        doors_dictionary[39][3] = True
        #Čtyřicet
        doors_dictionary[40][0] = True
        #Sedmnáct
        doors_dictionary[17][1] = True
    if 24 in rooms:
        #Devatenáct
        doors_dictionary[19][2] = True
        #Osmnáct
        doors_dictionary[18][3] = True
        #Čtyřicettři
        doors_dictionary[34][0] = True
        #Čtyřicetčtyři
        doors_dictionary[34][1] = True
    if 25 in rooms:
        #Třicetpět
        doors_dictionary[35][2] = True
        #Dvacetjedna
        doors_dictionary[21][3] = True
        #Dvacet
        doors_dictionary[20][0] = True
        #Třicetjedna
        doors_dictionary[31][1] = True
    if 26 in rooms:
        #Třicetčtyři
        doors_dictionary[34][3] = True
        #Třináct
        doors_dictionary[13][0] = True
        #Třicettři
        doors_dictionary[33][1] = True
    if 27 in rooms:
        #Třicetsedm
        doors_dictionary[37][2] = True
        #Třicetosm
        doors_dictionary[38][0] = True
        #Deset
        doors_dictionary[10][1] = True
    if 28 in rooms:
        #Jedenáct
        doors_dictionary[11][2] = True
        #Čtyřicetjedna
        doors_dictionary[41][3] = True
        #Čtyřicetdva
        doors_dictionary[11][1] = True
    if 29 in rooms:
        #Třicet
        doors_dictionary[30][2] = True
        #Dvanáct
        doors_dictionary[12][3] = True
        #Čtyřicetpět
        doors_dictionary[45][0] = True
    if 30 in rooms:
        #Třicetjedna
        doors_dictionary[31][2] = True
        #Dvacet
        doors_dictionary[20][3] = True
        #Dvacetdevět
        doors_dictionary[29][0] = True
    if 31 in rooms:
        #Čtyřicetšest
        doors_dictionary[46][2] = True
        #Dvacetpět
        doors_dictionary[25][3] = True
        #Třicet
        doors_dictionary[30][0] = True
    if 32 in rooms:
        #Třicettři
        doors_dictionary[33][3] = True
        #Dvacetpět
        doors_dictionary[25][0] = True
        #Čtyřicetšest
        doors_dictionary[46][1] = True
    if 33 in rooms:
        #Dvacetšest
        doors_dictionary[26][3] = True
        #Třicetjedna
        doors_dictionary[31][0] = True
        #Třicetdva
        doors_dictionary[32][1] = True
    if 34 in rooms:
        #Třicetpět
        doors_dictionary[35][3] = True
        #Čtrnáct
        doors_dictionary[14][0] = True
        #Dvacetšest
        doors_dictionary[26][1] = True
    if 35 in rooms:
        #Čtyřicetsedm
        doors_dictionary[47][3] = True
        #Dvacetdva
        doors_dictionary[22][0] = True
        #Třicetčtyři
        doors_dictionary[34][1] = True
    if 36 in rooms:
        #Čtyřicetsedm
        doors_dictionary[47][2] = True
        #Třicetsedm
        doors_dictionary[37][0] = True
        #Dvacetdva
        doors_dictionary[22][1] = True
    if 37 in rooms:
        #Třicetšest
        doors_dictionary[36][2] = True
        #Dvacetsedm
        doors_dictionary[27][0] = True
        #Patnáct
        doors_dictionary[15][1] = True
    if 38 in rooms:
        #Dvacetsedm
        doors_dictionary[27][2] = True
        #Třicetdevět
        doors_dictionary[39][0] = True
        #Šestnáct
        doors_dictionary[16][1] = True
    if 39 in rooms:
        #Třicetosm
        doors_dictionary[38][2] = True
        #Čtyřicetosm
        doors_dictionary[48][0] = True
        #Dvacettři
        doors_dictionary[23][1] = True
    if 40 in rooms:
        #Dvacettři
        doors_dictionary[23][2] = True
        #Čtyřicetosm
        doors_dictionary[48][3] = True
        #Čtyřicetjedna
        doors_dictionary[41][1] = True
    if 41 in rooms:
        #Sedmnáct
        doors_dictionary[17][2] = True
        #Čtyřicet
        doors_dictionary[40][3] = True
        #Dvacetosm
        doors_dictionary[28][1] = True
    if 42 in rooms:
        #Osmnáct
        doors_dictionary[18][2] = True
        #Dvacetosm
        doors_dictionary[28][3] = True
        #Čtyřicettři
        doors_dictionary[43][1] = True
    if 43 in rooms:
        #Dvacetčtyři
        doors_dictionary[24][2] = True
        #Čtyřicetdva
        doors_dictionary[42][3] = True
        #Čtyřicetdevět
        doors_dictionary[49][0] = True
    if 44 in rooms:
        #Čtyřicetpět
        doors_dictionary[45][2] = True
        #Dvacetčtyři
        doors_dictionary[24][3] = True
        #Čtyřicetdevět
        doors_dictionary[49][0] = True
    if 45 in rooms:
        #Dvacetdevět
        doors_dictionary[29][2] = True
        #Devatenáct
        doors_dictionary[19][3] = True
        #Čtyřicetčtyři
        doors_dictionary[44][0] = True
    if 46 in rooms:
        #Třicetdva
        doors_dictionary[32][3] = True
        #Třicetjedna
        doors_dictionary[31][0] = True
    if 47 in rooms:
        #Třicetpět
        doors_dictionary[35][1] = True
        #Třicetšest
        doors_dictionary[36][0] = True
    if 48 in rooms:
        #Třicetdevět
        doors_dictionary[39][2] = True
        #Čtyřicet
        doors_dictionary[40][1] = True
    if 49 in rooms:
        #Čtyřicetčtyři
        doors_dictionary[44][2] = True
        #Čtyřicettři
        doors_dictionary[43][3] = True
    return doors_dictionary



#Mění současnou roomku (current_room), podle toho, do jakých dveří hráč vstoupil
def current_room(doors, current_room):
    if current_room == 1:
        if doors == "UP":
            return 4
        if doors == "RIGHT":
            return 5
        if doors == "DOWN":
            return 2
        if doors == "LEFT":
            return 3
    if current_room == 2:
        if doors == "UP":
            return 1
        if doors == "RIGHT":
            return 6
        if doors == "DOWN":
            return 11
        if doors == "LEFT":
            return 7
    if current_room == 3:
        if doors == "UP":
            return 8
        if doors == "RIGHT":
            return 1
        if doors == "DOWN":
            return 7
        if doors == "LEFT":
            return 12
    if current_room == 4:
        if doors == "UP":
            return 13
        if doors == "RIGHT":
            return 9
        if doors == "DOWN":
            return 1
        if doors == "LEFT":
            return 8
    if current_room == 5:
        if doors == "UP":
            return 9
        if doors == "RIGHT":
            return 10
        if doors == "DOWN":
            return 6
        if doors == "LEFT":
            return 1
    if current_room == 6:
        if doors == "UP":
            return 5
        if doors == "RIGHT":
            return 16
        if doors == "DOWN":
            return 17
        if doors == "LEFT":
            return 2
    if current_room == 7:
        if doors == "UP":
            return 3
        if doors == "RIGHT":
            return 2
        if doors == "DOWN":
            return 18
        if doors == "LEFT":
            return 19
    if current_room == 8:
        if doors == "UP":
            return 21
        if doors == "RIGHT":
            return 4
        if doors == "DOWN":
            return 3
        if doors == "LEFT":
            return 20
    if current_room == 9:
        if doors == "UP":
            return 14
        if doors == "RIGHT":
            return 15
        if doors == "DOWN":
            return 5
        if doors == "LEFT":
            return 4
    if current_room == 10:
        if doors == "UP":
            return 15
        if doors == "RIGHT":
            return 27
        if doors == "DOWN":
            return 16
        if doors == "LEFT":
            return 5
    if current_room == 11:
        if doors == "UP":
            return 2
        if doors == "RIGHT":
            return 17
        if doors == "DOWN":
            return 28
        if doors == "LEFT":
            return 18
    if current_room == 12:
        if doors == "UP":
            return 20
        if doors == "RIGHT":
            return 3
        if doors == "DOWN":
            return 19
        if doors == "LEFT":
            return 29
    if current_room == 13:
        if doors == "UP":
            return 26
        if doors == "RIGHT":
            return 14
        if doors == "DOWN":
            return 4
        if doors == "LEFT":
            return 21
    if current_room == 14:
        if doors == "UP":
            return 34
        if doors == "RIGHT":
            return 22
        if doors == "DOWN":
            return 9
        if doors == "LEFT":
            return 13
    if current_room == 15:
        if doors == "UP":
            return 22
        if doors == "RIGHT":
            return 37
        if doors == "DOWN":
            return 10
        if doors == "LEFT":
            return 9
    if current_room == 16:
        if doors == "UP":
            return 10
        if doors == "RIGHT":
            return 38
        if doors == "DOWN":
            return 23
        if doors == "LEFT":
            return 6
    if current_room == 17:
        if doors == "UP":
            return 6
        if doors == "RIGHT":
            return 23
        if doors == "DOWN":
            return 41
        if doors == "LEFT":
            return 11
    if current_room == 18:
        if doors == "UP":
            return 7
        if doors == "RIGHT":
            return 11
        if doors == "DOWN":
            return 42
        if doors == "LEFT":
            return 24
    if current_room == 19:
        if doors == "UP":
            return 12
        if doors == "RIGHT":
            return 7
        if doors == "DOWN":
            return 24
        if doors == "LEFT":
            return 45
    if current_room == 20:
        if doors == "UP":
            return 25
        if doors == "RIGHT":
            return 8
        if doors == "DOWN":
            return 12
        if doors == "LEFT":
            return 30
    if current_room == 21:
        if doors == "UP":
            return 33
        if doors == "RIGHT":
            return 13
        if doors == "DOWN":
            return 8
        if doors == "LEFT":
            return 25
    if current_room == 22:
        if doors == "UP":
            return 35
        if doors == "RIGHT":
            return 36
        if doors == "DOWN":
            return 15
        if doors == "LEFT":
            return 14
    if current_room == 23: 
        if doors == "UP":
            return 16
        if doors == "RIGHT":
            return 39
        if doors == "DOWN":
            return 40
        if doors == "LEFT":
            return 17
    if current_room == 24:
        if doors == "UP":
            return 19
        if doors == "RIGHT":
            return 18
        if doors == "DOWN":
            return 43
        if doors == "LEFT":
            return 44
    if current_room == 25:
        if doors == "UP":
            return 32
        if doors == "RIGHT":
            return 21
        if doors == "DOWN":
            return 20
        if doors == "LEFT":
            return 31
    if current_room == 26:
        if doors == "RIGHT":
            return 34
        if doors == "DOWN":
            return 13
        if doors == "LEFT":
            return 33
    if current_room == 27:
        if doors == "UP":
            return 37
        if doors == "DOWN":
            return 38
        if doors == "LEFT":
            return 10
    if current_room == 28:
        if doors == "UP":
            return 11
        if doors == "RIGHT":
            return 41
        if doors == "LEFT":
            return 42
    if current_room == 29:
        if doors == "UP":
            return 30
        if doors == "RIGHT":
            return 12
        if doors == "DOWN":
            return 45
    if current_room == 30:
        if doors == "UP":
            return 31
        if doors == "RIGHT":
            return 20
        if doors == "DOWN":
            return 29
    if current_room == 31:
        if doors == "UP":
            return 46
        if doors == "RIGHT":
            return 25
        if doors == "DOWN":
            return 30
    if current_room == 32:
        if doors == "RIGHT":
            return 33
        if doors == "DOWN":
            return 25
        if doors == "LEFT":
            return 46
    if current_room == 33:
        if doors == "RIGHT":
            return 26
        if doors == "DOWN":
            return 21
        if doors == "LEFT":
            return 32
    if current_room == 34:
        if doors == "RIGHT":
            return 35
        if doors == "DOWN":
            return 14
        if doors == "LEFT":
            return 26
    if current_room == 35:
        if doors == "RIGHT":
            return 47
        if doors == "DOWN":
            return 22
        if doors == "LEFT":
            return 34
    if current_room == 36:
        if doors == "UP":
            return 47
        if doors == "DOWN":
            return 37
        if doors == "LEFT":
            return 22
    if current_room == 37:
        if doors == "UP":
            return 36
        if doors == "DOWN":
            return 27
        if doors == "LEFT":
            return 15
    if current_room == 38:
        if doors == "UP":
            return 27
        if doors == "DOWN":
            return 39
        if doors == "LEFT":
            return 16
    if current_room == 39:
        if doors == "UP":
            return 38
        if doors == "DOWN":
            return 48
        if doors == "LEFT":
            return 23
    if current_room == 40:
        if doors == "UP":
            return 23
        if doors == "RIGHT":
            return 48
        if doors == "LEFT":
            return 41
    if current_room == 41:
        if doors == "UP":
            return 17
        if doors == "RIGHT":
            return 40
        if doors == "LEFT":
            return 28
    if current_room == 42:
        if doors == "UP":
            return 18
        if doors == "RIGHT":
            return 28
        if doors == "LEFT":
            return 43
    if current_room == 43:
        if doors == "UP":
            return 24
        if doors == "RIGHT":
            return 42
        if doors == "LEFT":
            return 49
    if current_room == 44:
        if doors == "UP":
            return 45
        if doors == "RIGHT":
            return 24
        if doors == "DOWN":
            return 49
    if current_room == 45:
        if doors == "UP":
            return 29
        if doors == "RIGHT":
            return 19
        if doors == "DOWN":
            return 44
    if current_room == 46:
        if doors == "RIGHT":
            return 32
        if doors == "DOWN":
            return 31
    if current_room == 47:
        if doors == "DOWN":
            return 36
        if doors == "LEFT":
            return 35
    if current_room == 48:
        if doors == "UP":
            return 39
        if doors == "LEFT":
            return 40
    if current_room == 49:
        if doors == "UP":
            return 44
        if doors == "RIGHT":
            return 43