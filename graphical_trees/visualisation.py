import pygame as pg
import sys

screen = pg.display.set_mode((1280,720))
class visualisation():
    def __init__(self,pointstab,tab):
        self.verses=[]
        tab.append(1)  #appending 1 to the top verse, as tree is always beginning with 1 in this program
        self.verses.append(tab)  #appending to verse table
        for i in range(len(pointstab)): #for elements in table do this
            if i == 0: #if i==0 meaning it's the first element of tree, append all points connected with it
                self.verses.append(pointstab[i].tuple)
            else:
                help = []
                for j in range(len(pointstab)): #for every element in table with points in the tree and their connections
                    parent=-1                    #set the parent to a non-existent one, number in table
                    for k in range(len(self.verses)):  #in already existing verses search for the parent
                        if pointstab[j].number in self.verses[k]:  #if the number is in existing verses then that's the parent
                            parent=k 
                    if pointstab[i].number in pointstab[j].tuple and parent!=-1: #if number of point in tree table is in tuple of another number and parent exists
                        for k in range(len(pointstab[i].tuple)):  #append every point in this tuple to help table 
                            help.append(pointstab[i].tuple[k])
                self.verses.append(help) #append help verses as new verse
        self.height=720/len(self.verses)
        print(self.verses)
        points=[] #table for coordinates on screen for every point
        h=10 #height for first point on the screen
        for i in range(len(self.verses)):
            w = len(self.verses[i]) # w standing for width is number of integrals in verse
            if w * 50 > 640: #if there is too many integrals to start from middle of screen, then make another center
                center = 1280 / 2 - (w * 50) % 640
            else: #else center is the middle of screen
                center = 1280 / 2
            for j in range(w): #appending width, height and number of point
                points.append((int(1280-w-center),int(h),self.verses[i][j]))
                w += 50
            h += self.height
        lines=[]
        for i in range(len(points)-1):
            index=-1
            for j in range(len(pointstab)):
                if points[i][2] == pointstab[j].number:
                    index=j
                    break
            if index==-1:
                continue
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
