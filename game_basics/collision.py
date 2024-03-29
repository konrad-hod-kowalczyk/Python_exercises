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
        elif x == 400:
            self.x = 4
    def messenger(self,msg,color):
        line=""
        font = pg.font.SysFont(None, 250)
        size = self.game.screen.get_size()
        text = font.render(msg, True, color)
        self.game.screen.blit(text, [size[0]/8,size[1]/3])
        pg.display.update()
        with open("highscore.txt", "r") as file:
            lines = file.readlines()
        if(self.game.count>int(lines[self.x-1])):
            lines[self.x-1]=str(self.game.count)+"\n"
        with open("highscore.txt", "w") as file:
            for line in lines:
                file.write(line)
        time.sleep(1)
        exit(0)
    def score(self,count):
        font = pg.font.SysFont(None, 100)
        size = self.game.screen.get_size()
        text = font.render(str(count), True, (0,255,0))
        self.game.screen.blit(text, [0, size[1]/3])
        font = pg.font.SysFont(None, 50)
        text = font.render("HS:" + self.line, True, (0, 255, 0))
        self.game.screen.blit(text, [0, size[1] / 2])
