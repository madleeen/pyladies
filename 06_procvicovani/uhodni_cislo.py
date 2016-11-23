from random import randrange

cislo = randrange(1,21)
print ("Tipuj si cislo od 1 do 20 -", cislo)
pokus = 0
while cislo != pokus:
    pokus = int(input("Hadej cislo: "))
    if pokus > 20 or pokus < 0:
        print ("Cislo musi byt mezi 1 a 20!!")
    elif pokus > cislo:
        print ("Je to min nez tvuj pokus: ",pokus)
    elif pokus < cislo:
        print ("Je to vic nez tvuj pokus: ",pokus)

print ("Super, vyhral jsi! Cislo je: ", cislo)
exit ()
