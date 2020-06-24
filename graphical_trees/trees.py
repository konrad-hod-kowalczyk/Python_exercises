import pygame as pg
import random
import math
from branches import branch
def initialisation(table,n,s):
    global points #???
    table.remove(n)
    help=[]
    h=s-1
    rang=math.floor(random.random() * h)
    for i in range(rang):
        t=math.floor(random.random() * h)
        help.append(table[t])
    points.append(branch(n,help))
    for i in range(len(help)):
        initialisation(table,help[i],h)
size=math.floor(random.random() * 50)
tab=[]
for i in range(size):
    tab.append(i+1)
    print(tab)
points=[]
initialisation(tab,tab[0],size)
print(points.num)
