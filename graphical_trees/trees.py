import pygame as pg
import random
import math
from branches import branch
def initialisation():
  global points #???
  table.remove(n)
  help=[];
  h=size;
  rang=math.floor(random.random() * h)
  for i in range(rang):
    help.append(tab[math.floor(random.random() * h)])
  for i in len(help):
    initialisation(table,help[i])
size=math.floor(random.random() * 50)
tab=[]
for i in range(size):
  tab.append(i+1)
points=[];
