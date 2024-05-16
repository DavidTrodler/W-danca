import random
import time
#Vybrané roomky
rooms=[]

#Pravděpodobnosti
level = float(5)
level_odcitani = 0
level_pravdepodobnost = float(0.25 / (level/2))
pravdepodobnost_cervena = float(1)
pravdepodobnost_ruzova = float(0.5)
pravdepodobnost_zelena = float(0.1)

#Smyčka výběrů roomek
while True:
    fialova = True
    cervena = False
    ruzova = False
    zelena = False

    for i in range(2,9):
        if i in rooms:
            cervena = True
    for i in range (10,25):
        if i in rooms:
            ruzova = True


    if random.random() < pravdepodobnost_cervena:
        pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
        rooms.append(random.choice([2, 3, 4, 5]))

    if fialova and cervena:
        #pokud je v místnostech 2
        print("2")
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
        print("3")
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
        print("4")
        if 4 in rooms:
            #Červená
            if random.random() < pravdepodobnost_cervena:
                pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                rooms.append(random.choice([8,9]))
                cervena = True
            #Růžová
            if random.random() < pravdepodobnost_ruzova:
                pravdepodobnost_ruzova -= level_pravdepodobnost
                rooms.append([13])
                ruzova = True
        #pokud je v místnostech 5
        print("5")
        if 5 in rooms:
            #Červená
            if random.random() < pravdepodobnost_cervena:
                pravdepodobnost_cervena -= (level_pravdepodobnost * 2)
                rooms.append(random.choice([9,6]))
                cervena = True
            #Růžová
            if random.random() < pravdepodobnost_ruzova:
                pravdepodobnost_ruzova -= level_pravdepodobnost
                rooms.append([10])
                ruzova = True
        #pokud je v místnostech 6
        print("6")
        if 6 in rooms:
            #Růžová
            if random.random() < pravdepodobnost_ruzova:
                pravdepodobnost_ruzova -= level_pravdepodobnost
                rooms.append(random.choice([16,17]))
                ruzova = True
        #pokud je v místnostech 7
        print("7")
        if 7 in rooms:
            #Růžová
            if random.random() < pravdepodobnost_ruzova:
                pravdepodobnost_ruzova -= level_pravdepodobnost
                rooms.append(random.choice([18,19]))
                ruzova = True
        #pokud je v místnostech 8
        print("8")
        if 8 in rooms:
            #Růžová
            if random.random() < pravdepodobnost_ruzova:
                pravdepodobnost_ruzova -= level_pravdepodobnost
                rooms.append(random.choice([20,21]))
                ruzova = True
        #pokud je v místnostech 9
        print("9")
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
                rooms.append(random.choice([24,25]))
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
                rooms.append([35,36])
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
                rooms.append([43,44])
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
                rooms.append([31,32])
                zelena = True
    if fialova and cervena and ruzova and zelena:
        break
    time.sleep(0.1)


print(rooms)
print(len(rooms))
print(pravdepodobnost_cervena)
print(pravdepodobnost_ruzova)
print(pravdepodobnost_zelena)


"""
Možná přidat do posledního ifu více větvení, pokud je pravděpodobnost u zelené stále větší než 0
"""
