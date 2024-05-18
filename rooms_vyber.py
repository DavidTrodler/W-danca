import random
import time

#fialova = zakladni room

def vyber_insert_level(x):
    #Vybrané roomky
    rooms=[1]

    #Pravděpodobnosti
    level = float(x)
    level_pravdepodobnost = float(0.25 / (level/2))
    pravdepodobnost_cervena = float(1)
    pravdepodobnost_ruzova = float(0.5)
    pravdepodobnost_zelena = float(0.1)


    #Pokud je level 1
    if level == float(1):
        pravdepodobnost_ruzova = float(1)
        pravdepodobnost_cervena = float(2)

    fialova = True
    cervena = False
    ruzova = False
    zelena = False
    #Smyčka výběrů roomek
    if random.random() < pravdepodobnost_cervena:
        pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
        rooms.append(random.choice([2, 3, 4, 5]))
    
    while True:

        if not cervena:
            for i in range(2,9):
                if i in rooms:
                    cervena = True
        if not ruzova:
            for i in range(10,25):
                if i in rooms:
                    ruzova = True



        if fialova and cervena:
            #pokud je v místnostech 2
            
            if 2 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(random.choice([6,7]))
                    cervena = True
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(11)
                    ruzova = True

            #pokud je v místnostech 3
            
            if 3 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(random.choice([8,7]))
                    cervena = True

                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(12)
                    ruzova = True
            #pokud je v místnostech 4
            
            if 4 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(random.choice([8,9]))
                    cervena = True
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(13)
                    ruzova = True
            #pokud je v místnostech 5
            
            if 5 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(random.choice([9,6]))
                    cervena = True
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(10)
                    ruzova = True
            #pokud je v místnostech 6
            
            if 6 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([16,17]))
                    ruzova = True
            #pokud je v místnostech 7
            
            if 7 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([18,19]))
                    ruzova = True
            #pokud je v místnostech 8
            
            if 8 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([20,21]))
                    ruzova = True
            #pokud je v místnostech 9
            
            if 9 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([14,15]))
                    ruzova = True
        if fialova and cervena and ruzova:
            #pokud je v místnostech 10
            if 10 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(5)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([15,16]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(27)
                    zelena = True
            #pokud je v místnostech 11
            if 11 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(2)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([17,18]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(28)
                    zelena = True
            #pokud je v místnostech 12
            if 12 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(3)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([19,20]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(29)
                    zelena = True
            #pokud je v místnostech 13
            if 13 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(4)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([21,14]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(26)
                    zelena = True
            #pokud je v místnostech 14
            if 14 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(9)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([22,13]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(34)
                    zelena = True
            #pokud je v místnostech 15
            if 15 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(9)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([22,10]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(37)
                    zelena = True
            #pokud je v místnostech 16
            if 16 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(6)
                #Růžová
                    rooms.append(6)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([10,23]))
                    ruzova = True
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(38)
                    zelena = True
            #pokud je v místnostech 17
            if 17 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(6)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([11,23]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(41)
                    zelena = True
            #pokud je v místnostech 18
            if 18 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(7)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([11,24]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(42)
                    zelena = True
            #pokud je v místnostech 19
            if 19 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(7)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([12,24]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(45)
                    zelena = True
            #pokud je v místnostech 20
            if 20 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(8)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([12,25]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(30)
                    zelena = True
            #pokud je v místnostech 21
            if 21 in rooms:
                #Červená
                if random.random() < pravdepodobnost_cervena:
                    pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                    rooms.append(8)
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([13,25]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(33)
                    zelena = True
            #pokud je v místnostech 22
            if 22 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([14,15]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([35,36]))
                    zelena = True
            #pokud je v místnostech 23
            if 23 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([16,17]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([39,40]))
                    zelena = True
            #pokud je v místnostech 24
            if 24 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([18,19]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([43,44]))
                    zelena = True
            #pokud je v místnostech 25
            if 25 in rooms:
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(random.choice([20,21]))
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([31,32]))
                    zelena = True
        if fialova and cervena and ruzova and zelena:
            #pokud je v místnostech 26
            if 26 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([33,34]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(13)
            #pokud je v místnostech 27
            if 27 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([37,38]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(10)
            #pokud je v místnostech 28
            if 28 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([41,42]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(11)
            #pokud je v místnostech 29
            if 29 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([45,30]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(12)
            #pokud je v místnostech 30
            if 30 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([31,29]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(20)
            #pokud je v místnostech 31
            if 31 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([30,46]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(25)
            #pokud je v místnostech 32
            if 32 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([33,46]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(25)
            #pokud je v místnostech 33
            if 33 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([26,32]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(21)
            #pokud je v místnostech 34
            if 34 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([26,35]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(14)
            #pokud je v místnostech 35
            if 35 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([34,47]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(22)
            #pokud je v místnostech 36
            if 36 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([37,47]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(22)
            #pokud je v místnostech 37
            if 37 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([27,36]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(15)
            #pokud je v místnostech 38
            if 38 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([27,39]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(16)
            #pokud je v místnostech 39
            if 39 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([38,48]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(23)
            #pokud je v místnostech 40
            if 40 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([41,48]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(23)
            #pokud je v místnostech 41
            if 41 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([28,40]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(17)
            #pokud je v místnostech 42
            if 42 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([28,43]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(18)
            #pokud je v místnostech 43
            if 43 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([42,49]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(24)
            #pokud je v místnostech 44
            if 44 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([45,49]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(24)
            #pokud je v místnostech 45
            if 45 in rooms:
                #Zelená
                if random.random() < pravdepodobnost_zelena:
                    pravdepodobnost_zelena -= level_pravdepodobnost
                    rooms.append(random.choice([29,44]))
                #Růžová
                if random.random() < pravdepodobnost_ruzova:
                    pravdepodobnost_ruzova -= level_pravdepodobnost
                    rooms.append(19)
            #pokud je v místnostech 46
            if 46 in rooms:
                if 31 in rooms:
                    rooms.append(32)
                else:
                    rooms.append(31)
            #pokud je v místnostech 47
            if 47 in rooms:
                if 35 in rooms:
                    rooms.append(36)
                else:
                    rooms.append(35)
            #pokud je v místnostech 48
            if 48 in rooms:
                if 39 in rooms:
                    rooms.append(40)
                else:
                    rooms.append(39)
            #pokud je v místnostech 49
            if 49 in rooms:
                if 43 in rooms:
                    rooms.append(44)
                else:
                    rooms.append(43)


        if pravdepodobnost_cervena <= 0000.1:
            cervena = False
        if pravdepodobnost_ruzova <= 0000.1:
            ruzova = False
        if pravdepodobnost_zelena <= 0000.1:
            zelena = False
        if pravdepodobnost_cervena <= 0000.1 and pravdepodobnost_ruzova <= 0000.1 and pravdepodobnost_zelena <= 0000.1 and len(rooms) > 3:
            return rooms

            
    
        



def rooms_fixed(y):
    #Čištění seznamu
    rooms = vyber_insert_level(y)
    rooms_fixed_list = []
    for i in rooms:
        if i not in rooms_fixed_list:
            rooms_fixed_list.append(i)

    return rooms_fixed_list



