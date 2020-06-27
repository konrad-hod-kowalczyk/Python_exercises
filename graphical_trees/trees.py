import pygame as pg
import random
import math
from branches import branch
def initialisation(table,n,s,rang):
    global points
    table.remove(n)
    if rang==0 or len(table)==0:
        return 0
    print("------------")
    print("table=",table)
    help=[]
    h=s
    print("h=",h)
    #rang=math.floor(random.random() * h)
    tabtab=[]
    for i in range(len(table)):
        tabtab.append(table[i])
    for i in range(rang):
        h -= 1
        print("h=", h)
        t=math.floor(random.random() * h)
        print("t=",t)
        print("table[t]=", tabtab[t])
        help.append(tabtab[t])
        print("help=",help)
        tabtab.remove(tabtab[t])
        print("table=",tabtab)
    points.append(branch(n,help))
    for i in range(len(help)):
        r = math.floor(random.random() * (h - rang + 1))
        print("r=",r)
        print("help=",help)
        print("help[i]=", help[i])
        print("table=",table)
        rang+=r
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
