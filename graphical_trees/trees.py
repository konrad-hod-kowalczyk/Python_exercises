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
        tabtab.remove(tabtab[t]) #remove from copy, just to lessen the numbers algorithm can choose from and numbers that must be checked if the randomized one is in banned
    points.append(branch(n,help)) #append to points branch class with given parent as first argument, and children as table in second argument
    r=[]
    for i in range(len(help)):
        if i>=len(help) or len(table)==0: #randomizing numbers for each of the children, meaning how many children they will have
            break
        h = len(table)
        r.append((math.floor(random.random() * (h-rang)))/5)
        rang+=r[i]
    print("rang=",rang)
    rang=sum(r) #rang becomes the sum of all grandchildren
    if rang==0:
        rang=1 #if it's zero, then make it one as dividing by zero is impossible
    for i in range(len(help)):
        initialisation(help[i],int(r[i]%rang),max) #call the function for each of the children with respective numbers of their children, and checking if it's not accidentally bigger than the sum of all 
size=math.floor(random.random() * 50)+1 #randomizing the size of the tree
table=[]
for i in range(size): #appending numbers from 1 to size of the tree
    table.append(i+1)
points=[] #creating global table for points and for banned numbers
banned=[]
rr=math.floor(random.random()*(size/5))+1 #randomizing number of children of first point
initialisation(table[0],rr,table[size-1])
for i in range(len(points)):
    print(points[i].number)
    print(points[i].tuple)
vis=visualisation(points,table) #visualizing the tree
