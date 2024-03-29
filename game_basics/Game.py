import pygame as pg
import os
import sys
from objects import Rocket
from objects import Obst
from objects import Lobst
from collision import Col
import random
from start import start
class Game(object):
    def __init__(self,x):
        # Configuration
        pg.mouse.set_visible(False)
        self.tps_max = 60.0
        #initalization
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.tps_clock=pg.time.Clock()
        self.tps_delta=0.0
        self.x=x
        self.w = random.random() * 540 + 100
        if self.x==400:
            pg.time.set_timer(pg.USEREVENT + 1,self.x)
            pg.time.set_timer(pg.USEREVENT,self.x*10)
            self.t=20
        else:
            pg.time.set_timer(pg.USEREVENT+1,random.randrange(self.x,self.x+1000))
            self.t=0
        self.player=Rocket(self)
        self.rames=Obst(self,0,0)
        self.physics=Col(self,self.x)
        self.obstacles = [Lobst(self,50,self.x,self.w)]
        pg.display.set_caption("Locket Rauncher")
        self.bg = pg.image.load(os.path.join("images","img2.jpg")).convert()
        self.bgX=0
        self.count=0
        self.bgX2=self.bg.get_height()
        self.count=0
        self.times=0
        while True:
            self.draw()
            if self.player.vel.y<0:
                self.bgX -= self.player.vel.y
                self.bgX2 -= self.player.vel.y
            if self.bgX > self.bg.get_height() * 1:
                self.bgX = -self.bg.get_height()
            if self.bgX2 > self.bg.get_height() * 1:
                self.bgX2 = -self.bg.get_height()
            for obstacle in self.obstacles:
                if self.player.vel.y < 0:
                    obstacle.y += 1.9-self.player.vel.y
                else:
                    obstacle.y += 1.9
                if(obstacle.collide(self.player.hitbox)):
                    self.physics.messenger("Game Over", (255, 0, 0))
                if obstacle.y > 700:
                    self.obstacles.pop(self.obstacles.index(obstacle))
                    self.count+=1
                    self.physics.score(self.count)
                    pg.display.update()
            for event in pg.event.get():
                # Quitting
                if event.type == pg.QUIT:
                    sys.exit(0)
                if event.type == pg.USEREVENT+1:
                    self.w=self.w-self.t
                    self.obstacles.append(Lobst(self, 50,self.x,self.w))
                if event.type == pg.USEREVENT:
                    self.t = self.t*-1
            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            #Rendering
            pg.display.update()
            if (self.player.pos.y > 720  or self.player.pos.x < 1280/12 or self.player.pos.x > 1180):
                self.physics.messenger("Game Over",(255,0,0))
    def tick(self):
        # Input
        self.player.tick()
    def draw(self):
        # Drawing
        self.screen.blit(self.bg, (0,self.bgX))
        self.screen.blit(self.bg, (0,self.bgX2))
        self.player.draw()
        self.rames.draw()
        for obstacle in  self.obstacles:
            obstacle.draw()
        self.physics.score(self.count)
h=start()
if __name__ == "__main__":
    Game(h)
