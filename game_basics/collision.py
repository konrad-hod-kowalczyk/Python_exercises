import pygame as pg
import time

class Col(object):
    def __init__(self,game,x):
        self.game=game
        if x==1000:
            self.x=1
        elif x==500:
            self.x=2
        elif x==300:
            self.x=3
    def messenger(self,msg,color):
        line=""
        font = pg.font.SysFont(None, 250)
        size = self.game.screen.get_size()
        text = font.render(msg, True, color)
        self.game.screen.blit(text, [size[0]/8,size[1]/3])
        pg.display.update()
        f = open("highscore.txt", "r+")
        for i in range(0,self.x):
            line=""
            line=f.readline()
        if(self.game.count>int(line)):
            f.seek(self.x,1)
            f.write(str(self.game.count))
        f.close()
        time.sleep(1)
        exit(0)
    def score(self,count):
        line=""
        font = pg.font.SysFont(None, 100)
        size = self.game.screen.get_size()
        text = font.render(str(count), True, (0,255,0))
        self.game.screen.blit(text, [0, size[1]/3])
        f = open("highscore.txt", "r")
        for i in range(0,self.x):
            line=""
            line=f.readline()
        font = pg.font.SysFont(None, 50)
        text = font.render("HS:" + line, True, (0, 255, 0))
        f.close()
        self.game.screen.blit(text, [0, size[1] / 2])
