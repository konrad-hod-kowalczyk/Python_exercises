import pygame as pg
import sys

screen = pg.display.set_mode((1280,720))
class visualisation():
    def __init__(self,pointstab,tab):
        self.lines=[]
        tab.append(1)
        self.lines.append(tab)
        for i in range(len(pointstab)):
            if i == 0:
                self.lines.append(pointstab[i].tuple)
            else:
                help = []
                for j in range(len(pointstab)):
                    parent=-1
                    for k in range(len(self.lines)):
                        if pointstab[j].number in self.lines[k]:
                            parent=k
                    if pointstab[i].number in pointstab[j].tuple and parent!=-1:
                        for k in range(len(pointstab[i].tuple)):
                            help.append(pointstab[i].tuple[k])
                self.lines.append(help)
        self.height=720/len(self.lines)
        print(self.lines)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
            for i in range(len(self.lines)):
                w=len(self.lines[i])
                for j in range(w):
                    pg.draw.circle(screen,(255,255,255),(int(1280/w),50),5)
                    w-=1
            pg.draw.line(screen,(255,255,255),(1280/2,10),(1280/3,100),1)
            pg.display.update()
