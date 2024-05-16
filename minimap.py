import pygame, sys

# Create the game window
window = pygame.display.set_mode((1366, 755))
pygame.display.set_caption("ˇIsaacˇ")

roomka = pygame.image.load("pozadi.png")
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()




"""
Dodělat zobrazení roomek na mapě následujícím způsobem.
-----------------------------------------------------------------
Vše se bude odvíjet od roomky č. 1, která bude mít souřadnice 360, 200. (asi, oblast minimapy je znázorněna v souboru "minimapa rozměry.png")
Následující roomky budou mít vztah k roomce, například roomka nad ní bude mít souřadnice
stejné jako roomka č. 1, ale bude mít y-ovou souřadnici o 200 větší. Roomka vpravo od ní bude mít
souřadnice pro x větší např. o 300 atd...
!! čísla roomek jsou znázorněna v excelové tabulce ve složce s projektem (W-danca) !! 

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
Pokud se změní souřadnice roomky č. 1, změní se i souřadnice všech ostatních roomek.

Při zobrazování roomek bude podmínka: Pokud nejsou souřadnice roomky v oblasti minimapy, obrázek roomky se nevykreslí.
"""