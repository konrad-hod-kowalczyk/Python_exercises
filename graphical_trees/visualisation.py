import pygame as pg
import sys

screen = pg.display.set_mode((1280,720))
class visualisation():
    def __init__(self,pointstab,tab):

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit(0)
            pg.draw.line(screen,(255,255,255),(1280/2,10),(1280/3,100),1)
            pg.display.update()
