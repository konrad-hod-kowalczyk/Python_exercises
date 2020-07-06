import pygame as pg
import sys

screen = pg.display.set_mode((1280,720))
class visualisation():
    def __init__(self,pointstab,tab):
        self.lines=[]
        self.lines.append(len(tab)+1)
        for i in range(len(pointstab)):
            if i==0:
                self.lines.append(pointstab[i].tuple)
            else:
                help=[];
                h=i;
                for j in range(len(pointstab)):
                    if pointstab[h].number in pointstab[j].tuple and pointstab[j].number==1:
                        help.append(pointstab[i].tuple)
                self.lines.append(help)
                
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
            pg.draw.line(screen,(255,255,255),(1280/2,10),(1280/3,100),1)
            pg.display.update()
