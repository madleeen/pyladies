
from turtle import forward, left, right, shape, pendown, penup, exitonclick, setx, sety
import math
#12 spirala
opakovani = int(input("Zadej jak velkou spiralu chces:"))
n=6
delka_steny=int(200/n)
uhel=int(180-(180*(1-(2/n))))
for i in range(1,opakovani):
    forward (i)
    left (uhel)
