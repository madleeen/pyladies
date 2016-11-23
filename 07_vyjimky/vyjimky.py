# def over_cislo(cislo):
#     if cislo > 0:
#         return "ok"
#     else:
#         raise ValueError("Cislo musi byt vetsi nez 0.")
#
# over_cislo(1)
# print ("OK")
#
# try:
#     over_cislo(-1)
# except ValueError:
#     print ("Osetrena vyjimka")
#
# print ("Pokracuju!")

while True:
    try:
        cislo=int(input("Zadej cislo:"))
    except ValueError:
        print("Toto neni cislo")
    else:
        break
    finally:
        print("Cislo je {}".format(cislo) + "a toto je konec")
