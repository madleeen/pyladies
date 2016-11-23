from turtle import forward, left, right,pendown, penup, exitonclick
import math

#domecek

def nakresliDomecek(delka_steny):
    forward(delka_steny)
    left (135)
    forward (math.sqrt(2)*delka_steny)
    left (135)
    forward(delka_steny)
    left (135)
    forward (math.sqrt(2)*delka_steny)
    left (135)
    forward(delka_steny)
    right (135)
    forward ((math.sqrt(2)*delka_steny)*0.5)
    right (90)
    forward ((math.sqrt(2)*delka_steny)*0.5)
    right (45)
    forward(delka_steny)

    left (90)
    penup()
    forward(10)
    pendown()

velikost=0
while True:
    velikost=int(input("Zadej delku steny domecku:"))
    nakresliDomecek(velikost)
#exitonclick()
