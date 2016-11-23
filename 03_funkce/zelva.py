from turtle import forward, left, right, shape, pendown, penup, exitonclick, setx, sety
import math


# n = int(input("Zadejte pocet obdelniku:"))
#
# for i in range(n):
#     print (i)
#     shape ("turtle")
#     for j in range(4):
#         forward(50)
#         left(90)
#     left(20)
#     # penup()
#     # forward(10)
#     # pendown()
#
# exitonclick()

#trojuhelnik
# for  i in range (3):
#     forward(100)
#     left(120)

#domecek
# n = int(input("Zadej pocet domecku ve vesnici:"))
# delka_steny=30
# for i in range(n):
#     forward(delka_steny)
#     left (135)
#     forward (math.sqrt(2)*delka_steny)
#     left (135)
#     forward(delka_steny)
#     left (135)
#     forward (math.sqrt(2)*delka_steny)
#     left (135)
#     forward(delka_steny)
#     right (135)
#     forward ((math.sqrt(2)*delka_steny)*0.5)
#     right (90)
#     forward ((math.sqrt(2)*delka_steny)*0.5)
#     right (45)
#     forward(delka_steny)
#
#     left (90)
#     penup()
#     forward(10)
#     pendown()

#petiuhelnik, sestiuhelnk, kolecko (n=180)
# n = int(input("Zadej kolika uhelnik chces:"))
# delka_steny=int(200/n)
# uhel=int(180-(180*(1-(2/n))))
# for i in range(n):
#     forward(delka_steny)
#     left(uhel)

#10 ornament
# n=100
# for i in range(1,n,5):
#     left (90)
#     forward (i)

#12 spirala
# opakovani = int(input("Zadej jak velkou spiralu chces:"))
# n=6
# delka_steny=int(200/n)
# uhel=int(180-(180*(1-(2/n))))
# for i in range(1,opakovani):
#     forward (i)
#     left (uhel)

#14,15
# for i in range(18):
#     for j in range(4):
#         forward(50)
#         left(90)
#     left(20)
# right (90)
# forward(200)

#exitonclick()

#16
# prvni=int(input("Zadej prvni cislo:"))
# druhe=int(input("Zadej druhe cislo:"))
# operace=input("Zadej operaci s cisly:")
#
# if operace == "+":
#     vysledek= prvni + druhe
# elif operace == "-":
#     vysledek= prvni - druhe
# elif operace == "*":
#     vysledek= prvni - druhe
# elif operace == "/":
#     vysledek= prvni / druhe
# else:
#     print ("Neznama operace.")
#
# print(vysledek)


#17
for i in range(4):
    cislo=int(input("Zadej cislo:"))
    if i == 0:
        vysledek=cislo
    if cislo < vysledek:
        vysledek=cislo
print (vysledek)
