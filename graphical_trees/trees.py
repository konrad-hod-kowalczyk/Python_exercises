import pygame as pg
import random
import math
from branches import branch
def initialisation(table,n,s):
    global points
    table.remove(n)
    print(table)
    help=[]
    h=s-1
    print(h)
    #rang=math.floor(random.random() * h)
    rang=2
    for i in range(rang):
        t=math.floor(random.random() * h)
        print(t)
        help.append(table[t])
        print(help)
        table.remove(table[t])
        print(table)
        h-=1
    points.append(branch(n,help))
    for i in range(len(help)):
        initialisation(table,help[i],h)
#size=math.floor(random.random() * 50)
size=5
tab=[]
for i in range(size):
    tab.append(i+1)
    #print(tab)
points=[]
initialisation(tab,tab[0],size)
print(points[0].number)
print(points[0].tuple)
