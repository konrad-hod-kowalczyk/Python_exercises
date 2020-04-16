import pygame as pg
import time

class Col(object):
    def __init__(self,game):
        self.game=game
    def messenger(self,msg,color):
        font = pg.font.SysFont(None, 250)
        size = self.game.screen.get_size()
        text = font.render(msg, True, color)
        self.game.screen.blit(text, [size[0]/8,size[1]/3])
        pg.display.update()
        f = open("highscore.txt", "r+")
        if(self.game.count>int(f.read())):
            f.seek(0,0)
            f.write(str(self.game.count))
        f.close()
        time.sleep(1)
        exit(0)
    def score(self,count):
        font = pg.font.SysFont(None, 100)
        size = self.game.screen.get_size()
        text = font.render(str(count), True, (0,255,0))
        self.game.screen.blit(text, [0, size[1]/3])
        f = open("highscore.txt", "r")
        font = pg.font.SysFont(None, 50)
        text = font.render("HS:" + f.read(), True, (0, 255, 0))
        f.close()
        self.game.screen.blit(text, [0, size[1] / 2])
