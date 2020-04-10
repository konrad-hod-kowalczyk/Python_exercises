import pygame as pg

class Col(object):
    def __init__(self,game):
        self.game=game
    def messenger(self,msg,color):
        font = pg.font.SysFont(None, 250)
        size = self.game.screen.get_size()
        text = font.render(msg, True, color)
        self.game.screen.blit(text, [size[0]/8,size[1]/3])