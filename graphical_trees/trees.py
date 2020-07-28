import random
import math
from branches import branch
from visualisation import visualisation
def initialisation(n,rang,max):
    global points #table for points and their connections
    global table #table of unused yet points
    global banned #table of used points
    table.remove(n) #removing current point
    if rang<=0 or len(table)==0 or len(banned)==max-1: #if non positive number was randomized or all points are banned, stop doing this function
        return 0
    if rang>len(table): #if randomized number is greater than length of the table 
        rang=len(table)
    help=[]
    h=len(table)
    tabtab=[]
    for i in range(len(table)): #copying the main table 
        tabtab.append(table[i])
    for i in range(rang):
        #if len(tabtab)==0: #if numbers in table end, DOES IT WORK?
            #rang=len(help)
            #break
        h -= 1 #substracting one from the length of the table
        t=math.floor(random.random() * h) #randomize index in the table
        if tabtab[t] in banned: #if number with this index is already being used, then search the table for first number that isn't
            t=-1
            for i in range(len(tabtab)):
                t+=1
                if tabtab[t] not in banned:
                    break
        if tabtab[t] in banned: #if every number is in banned, continue to the next iteration, DOES IT WORK?
            h-=1
            continue
        help.append(tabtab[t]) #append the number to iteration table, table containing points connected to the function one
        banned.append(tabtab[t]) #append the number to banned
        tabtab.remove(tabtab[t]) #remove from copy, DOES IT WORK?
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
