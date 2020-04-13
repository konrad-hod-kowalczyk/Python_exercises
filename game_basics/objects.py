import pygame as pg
import random
from pygame.math import Vector2
class Rocket(object):
    def __init__(self,game):
        self.game=game
        self.speed = 1.6
        self.gravity = 0.957

        self.size = self.game.screen.get_size()

        self.pos = Vector2(self.size[0]/2,self.size[1]/2)
        self.vel = Vector2(0,0)
        self.acc = Vector2(0,0)

    def add_force(self, force):
        self.acc += force
    def tick(self):
        #Input
        pressed = pg.key.get_pressed()
        if pressed[pg.K_w]:
            self.add_force(Vector2(0,-self.speed))
        if pressed[pg.K_s]:
            self.add_force(Vector2(0,self.speed))
        if pressed[pg.K_a]:
            self.add_force(Vector2(-self.speed,0))
        if pressed[pg.K_d]:
            self.add_force(Vector2(self.speed,0))
        #Physics
        self.vel *= 0.9
        self.acc -= Vector2(0,-self.gravity)
        self.vel +=self.acc
        if self.pos.y <= 100:
            if self.acc.y > 0:
                self.pos += self.vel
            self.pos.x += self.vel.x
        else:
            self.pos += self.vel
        self.acc *= 0
    def draw(self):
        #Triangle
        points = [Vector2(0,-10), Vector2(5,5), Vector2(-5,5)]
        #Rotate
        angle = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(angle) for p in points]
        #Fix
        points = [Vector2(p.x,p.y*-1) for p in points]
        #Position
        points = [self.pos+p*5 for p in points]
        #Drawing
        pg.draw.polygon(self.game.screen, (0,100,255),points)
class Obst(object):
    def __init__(self,game,x,y):
        self.game=game
        self.x=x
        self.y=y
        self.width = self.game.screen.get_size()[0]/12
        self.height = self.game.screen.get_size()[1]
    def draw(self):
        self.game.screen.blit(self.game.screen,pg.draw.rect(self.game.screen, (255, 255, 255), pg.Rect(0, 0, self.width, self.height)))
        self.game.screen.blit(self.game.screen, pg.draw.rect(self.game.screen, (255, 255, 255), pg.Rect(self.width*12-100, 0, self.width, self.height)))
class Lobst(object):
    def __init__(self,game,height):
        self.game=game
        self.r=random.randrange(0,2)
        if self.r==0:
            self.x=0
            self.width = random.random() * 1000 + 100
        else:
            self.x=1280
            self.width = -random.random() * 1000 - 100
        self.y=-50
        #self.width=random.random()*640+100
        self.height=height
        self.hitbox=pg.Rect(self.x,self.y,self.width,height)
    def draw(self):
        self.hitbox=(self.x,self.y,self.width,self.height)
        pg.draw.rect(self.game.screen,(255,255,255), self.hitbox)
        pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
