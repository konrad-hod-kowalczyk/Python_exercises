import pygame as pg
import random
import math
from branches import branch
size=math.floor(random.random() * 50)
tab=[]
for i in range(size):
  tab.append(i+1)
points=[];
while True:
  help=[];
  h=size;
  rang=math.floor(random.random() * h)
