import random
import math
from branches import branch
def initialisation(n,rang):
    global points
    global table
    global banned
    table.remove(n)
    if rang<=0 or len(table)==0:
        return 0
    if rang>len(table):
        rang=len(table)
    #print("------------")
    #print("table=",table)
    help=[]
    h=len(table)
    #print("h=",h)
    #print("range=", rang)
    #rang=math.floor(random.random() * (h-1))
    tabtab=[]
    for i in range(len(table)):
        tabtab.append(table[i])
    for i in range(rang):
        if len(tabtab)==0:
            rang=len(help)
            break
        h -= 1
        #print("****")
        #print("h=", h)
        t=math.floor(random.random() * h)
        if tabtab[t] in banned:
            h+=1
            continue
        #print("t=",t)
        #print("table[t]=", tabtab[t])
        help.append(tabtab[t])
        #print("help=",help)
        banned.append(tabtab[t])
        tabtab.remove(tabtab[t])
        #print("table=",tabtab)
    points.append(branch(n,help))
    for i in range(len(help)):
        if i>=len(help):
            break
        r = math.floor(random.random() * (h - rang+2))+1
        #print("r=",r)
        #print("help=",help)
        #print("i=",i)
        #print("help[i]=", help[i])
        #print("table=",table)
        rang+=r
        #if help[i] not in table:
         #   help.remove(help[i])
         #   continue
        initialisation(help[i],r)
size=math.floor(random.random() * 50)+1
#size=5
table=[]
for i in range(size):
    table.append(i+1)
print(table)
points=[]
banned=[]
rr=math.floor(random.random()*(size/2))+1
#print("first range=",rr)
initialisation(table[0],rr)
#print("########################################")
for i in range(len(points)):
    print(points[i].number)
    print(points[i].tuple)
