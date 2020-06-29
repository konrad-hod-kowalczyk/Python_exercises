import pygame as pg
import random
import math
from branches import branch
def initialisation(n,s,rang):
    global points
    global table
    table.remove(n)
    if rang<=0 or len(table)==0:
        return 0
    print("------------")
    print("table=",table)
    help=[]
    h=len(table)
    print("h=",h)
    #rang=math.floor(random.random() * h)
    tabtab=[]
    for i in range(len(table)):
        tabtab.append(table[i])
    for i in range(rang):
        if len(tabtab)==0:
            rang=len(help)
            break
        h -= 1
        print("****")
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
        r = math.floor(random.random() * (h - rang + 2))
        print("r=",r)
        print("help=",help)
        print("help[i]=", help[i])
        print("table=",table)
        rang+=r
        if help[i] not in table:
            help.remove(help[i])
            continue
        initialisation(help[i],h,r)
#size=math.floor(random.random() * 50)
size=5
table=[]
for i in range(size):
    table.append(i+1)
    #print(tab)
points=[]
initialisation(table[0],size,4)
print("########################################")
for i in range(len(points)):
    print(points[i].number)
    print(points[i].tuple)
