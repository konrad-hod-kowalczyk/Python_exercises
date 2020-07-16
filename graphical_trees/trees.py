import random
import math
from branches import branch
from visualisation import visualisation
def initialisation(n,rang,max):
    global points
    global table
    global banned
    table.remove(n)
    if rang<=0 or len(table)==0 or len(banned)==max-1:
        return 0
    if rang>len(table):
        rang=len(table)
    help=[]
    h=len(table)
    tabtab=[]
    for i in range(len(table)):
        tabtab.append(table[i])
    for i in range(rang):
        if len(tabtab)==0:
            rang=len(help)
            break
        h -= 1
        t=math.floor(random.random() * h)
        if tabtab[t] in banned:
            t=-1
            for i in range(len(tabtab)):
                t+=1
                if tabtab[t] not in banned:
                    break
        if tabtab[t] in banned:
            h-=1
            continue
        help.append(tabtab[t])
        banned.append(tabtab[t])
        tabtab.remove(tabtab[t])
    points.append(branch(n,help))
    r=[]
    for i in range(len(help)):
        if i>=len(help) or len(table)==0:
            break
        h = len(table)
        r.append((math.floor(random.random() * (h-rang)))/5)
        rang+=r[i]
    print("rang=",rang)
    rang=sum(r)
    if rang==0:
        rang=1
    for i in range(len(help)):
        initialisation(help[i],int(r[i]%rang),max)
size=math.floor(random.random() * 50)+1
#size=10
table=[]
for i in range(size):
    table.append(i+1)
print(table)
points=[]
banned=[]
rr=math.floor(random.random()*(size/5))+1
initialisation(table[0],rr,table[size-1])
for i in range(len(points)):
    print(points[i].number)
    print(points[i].tuple)
vis=visualisation(points,table)
