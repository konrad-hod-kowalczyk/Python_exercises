import pygame as pg
import random
import math
from branches import branch
def initialisation(table,n,s,rang):
    global points
    table.remove(n)
    if rang==0:
        points.append(branch(n,[0]))
        return 0
    print(table)
    help=[]
    h=s
    print(h)
    #rang=math.floor(random.random() * h)
    tabtab=table
    for i in range(rang):
        h -= 1
        print("h=", h)
        t=math.floor(random.random() * h)
        print("t=",t)
        print("table[t]=", tabtab[t])
        help.append(table[t])
        print("help=",help)
        tabtab.remove(tabtab[t])
        print("table=",table)
    points.append(branch(n,help))
    for i in range(len(help)):
        r = math.floor(random.random() * (h - rang + 2))
        print(r)
        rang-=r
        initialisation(table,help[i],h,r)
#size=math.floor(random.random() * 50)
size=5
tab=[]
for i in range(size):
    tab.append(i+1)
    #print(tab)
points=[]
initialisation(tab,tab[0],size,2)
print(points[0].number)
print(points[0].tuple)
