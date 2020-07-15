import pygame as pg
import sys

screen = pg.display.set_mode((1280,720))
class visualisation():
    def __init__(self,pointstab,tab):
        self.verses=[]
        tab.append(1)
        self.verses.append(tab)
        for i in range(len(pointstab)):
            if i == 0:
                self.verses.append(pointstab[i].tuple)
            else:
                help = []
                for j in range(len(pointstab)):
                    parent=-1
                    for k in range(len(self.verses)):
                        if pointstab[j].number in self.verses[k]:
                            parent=k
                    if pointstab[i].number in pointstab[j].tuple and parent!=-1:
                        for k in range(len(pointstab[i].tuple)):
                            help.append(pointstab[i].tuple[k])
                self.verses.append(help)
        self.height=720/len(self.verses)
        print(self.verses)
        points=[]
        h=50
        for i in range(len(self.verses)):
            w = len(self.verses[i])
            if w * 50 > 640:
                center = 1280 / 2 - (w * 50) % 640
            else:
                center = 1280 / 2
            for j in range(w):
                points.append((int(1280-w-center),int(h),self.verses[i][j]))
                w += 50
            h += self.height
        lines=[]
        for i in range(len(points)):
            index=-1
            for j in range(len(pointstab)):
                if points[i][2] == pointstab[j].number:
                    index=j
                    break
            for j in range(len(pointstab[index].tuple)):
                for k in range(len(points)):
                    if pointstab[index].tuple[j] == points[k][2]:
                        lines.append(((points[i][0],points[i][1]),(points[k][0],points[k][1])))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
            for i in range(len(points)):
                pg.draw.circle(screen, (255, 255, 255), (points[i][0], points[i][1]), 5)
            for i in range(len(lines)):
                pg.draw.line(screen,(255,255,255),lines[i][0],lines[i][1],1)
            pg.display.update()
