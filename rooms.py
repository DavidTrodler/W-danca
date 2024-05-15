rooms=[]
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
    for i in range (26,49):
        if i in rooms:
            zelena = True        