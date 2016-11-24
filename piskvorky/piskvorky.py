#Zadani
# 1 radek o 20ti znacich, vyplnene -
# v prvnim kole - hrac zada pozici (0-19) na kterou chce dat X, vystrida se s druhym
# druhy hrac s O
# kdo da 3 vedle sebe, vyhral
from random import randrange
herni_pole= "-" * 20
symbol=0
pozice=0

def piskvorky1d(herni_pole):
    # kolo=1
    konec=False
    symbol=str.upper(input("Zadej symbol hrace(o,x):"))

    while not konec:
        herni_pole = tah_hrace(herni_pole, pozice, symbol)
        konec = vyhodnot(herni_pole)
        herni_pole = tah_pocitace(herni_pole,symbol)
        konec = vyhodnot(herni_pole)

def tah(herni_pole, pozice, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    herni_pole=herni_pole[:pozice] + symbol + herni_pole[pozice + 1:]
    print(herni_pole, "| tah na pozici cislo",pozice,"s hracem", symbol)
    return herni_pole

def tah_hrace(herni_pole, pozice, symbol):
    "Vrátí herní pole s daným symbolem umístěným na danou pozici"
    pozice=int(input("Zadej cislo pozice(0-19):"))
    herni_pole = tah(herni_pole,pozice,symbol)
    return herni_pole

def tah_pocitace(herni_pole,symbol):
    "Vrátí herní pole se zaznamenaným tahem počítače"
    if symbol=="O":
        symbol_pocitace="X"
    else:
        symbol_pocitace="O"
    #pozice - nahodne vyber pozici 0-19, pokud obsahuje - obsah symbolem, jinak vyber jinou dokud neni vyhovujici
    if "-" in herni_pole:
    #overeni, ze herni_pole ma jeste neobsazena policka
        cislo = randrange(0,19)
        while "-" not in herni_pole[cislo:]:
            cislo = randrange(0,19)
    herni_pole = tah(herni_pole,cislo,symbol_pocitace)
    return herni_pole

def vyhodnot(herni_pole):
    if "XXX" in herni_pole:
        print("Vyhrál hráč X!")
        konec=True
    elif "OOO" in herni_pole:
        print("Vyhrál hráč O!")
        konec=True
    elif "-" not in herni_pole:
        print("Remíza!Nikdo nevyhrál.")
        konec=True
    else:
        #print("Hra ještě neskončila.")
        konec=False
    return konec


piskvorky1d(herni_pole)
