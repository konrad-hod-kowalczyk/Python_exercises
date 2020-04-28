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
        self.points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]
        self.hitbox = (self.points)
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
        points = [Vector2(0, -10), Vector2(5, 5), Vector2(-5, 5)]
        #Rotate
        angle = self.vel.angle_to(Vector2(0,1))
        points = [p.rotate(angle) for p in points]
        #Fix
        points = [Vector2(p.x,p.y*-1) for p in points]
        #Position
        points = [self.pos+p*5 for p in points]
        #Drawing
        self.hitbox = (points)
        pg.draw.polygon(self.game.screen, (0,100,255),points)
        pg.draw.polygon(self.game.screen, (255, 0, 0), self.hitbox,2)
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
    def __init__(self,game,height,h,w):
        self.h=h
        self.game=game
        if self.h==400:
            self.x=0
            self.width=w
        else:
            self.r=random.randrange(0,2)
            if self.r==0:
                self.x=0
                self.width = random.random() * 1000 + 100
            else:
                self.x=1280
                self.width = -random.random() * 1000 - 100
        self.y=-50
        self.height=height
        self.type=1
        self.hitbox=pg.Rect(self.x,self.y,self.width,height)
    def draw(self):
        if self.h==400:
            self.hitbox = (0, self.y, abs(self.width), self.height)
            pg.draw.rect(self.game.screen, (255, 255, 255), self.hitbox)
            pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
            self.hitbox = (1280, self.y, -abs(1280-150-self.width), self.height)
            pg.draw.rect(self.game.screen, (255, 255, 255), self.hitbox)
            pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
            self.type = 3
        else:
            if abs(self.width) < 1280/5+1280/4:
                if abs(self.width) < 1280 / 8:
                    self.width = self.width*2
                self.hitbox = (0, self.y, abs(self.width), self.height)
                pg.draw.rect(self.game.screen, (255, 255, 255), self.hitbox)
                pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
                self.hitbox = (1280, self.y, -abs(self.width), self.height)
                pg.draw.rect(self.game.screen, (255, 255, 255), self.hitbox)
                pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
                self.type=2
            else:
                self.hitbox = (self.x, self.y, self.width, self.height)
                pg.draw.rect(self.game.screen,(255,255,255), self.hitbox)
                pg.draw.rect(self.game.screen, (255, 0, 0), self.hitbox, 2)
    def collide(self,rect):
        if self.type==1:
            if self.hitbox[2] > 0:
                if rect[0][0] < self.hitbox[0]+self.hitbox[2] or rect[1][0] < self.hitbox[0]+self.hitbox[2] or rect[2][0] < self.hitbox[0]+self.hitbox[2]:
                    if rect[0][1] < self.hitbox[1]+self.hitbox[3] and rect[0][1] > self.hitbox[1] or rect[1][1] < self.hitbox[1]+self.hitbox[3] and rect[1][1] > self.hitbox[1] or rect[2][1] < self.hitbox[1]+self.hitbox[3] and rect[2][1] > self.hitbox[1]:
                        return True
            else:
                if rect[0][0] > self.hitbox[0]+self.hitbox[2] or rect[1][0] > self.hitbox[0]+self.hitbox[2] or rect[2][0] > self.hitbox[0]+self.hitbox[2]:
                    if rect[0][1] < self.hitbox[1]+self.hitbox[3] and rect[0][1] > self.hitbox[1] or rect[1][1] < self.hitbox[1]+self.hitbox[3] and rect[1][1] > self.hitbox[1] or rect[2][1] < self.hitbox[1]+self.hitbox[3] and rect[2][1] > self.hitbox[1]:
                        return True
        elif self.type==2:
            if rect[0][0] <  abs(self.hitbox[2]) or rect[1][0] < abs(self.hitbox[2]) or rect[2][0] <  abs(self.hitbox[2]) or rect[0][0] > self.hitbox[0]+self.hitbox[2] or rect[1][0] > self.hitbox[0]+self.hitbox[2] or rect[2][0] > self.hitbox[0]+self.hitbox[2]:
                if rect[0][1] < self.hitbox[1] + self.hitbox[3] and rect[0][1] > self.hitbox[1] or rect[1][1] < self.hitbox[1] + self.hitbox[3] and rect[1][1] > self.hitbox[1] or rect[2][1] < self.hitbox[1] + self.hitbox[3] and rect[2][1] > self.hitbox[1]:
                    return True
        else:
            if rect[0][0]  > abs(self.hitbox[0]+self.hitbox[2]) or rect[1][0]  > abs(self.hitbox[0]+self.hitbox[2]) or rect[2][0]  > abs(self.hitbox[0]+self.hitbox[2]) or rect[0][0] < abs(self.hitbox[0]-150+self.hitbox[2]) or rect[1][0] < abs(self.hitbox[0]-150+self.hitbox[2]) or rect[2][0] < abs(self.hitbox[0]-150+self.hitbox[2]):
                if rect[0][1] < self.hitbox[1]+self.hitbox[3] and rect[0][1] > self.hitbox[1]  or rect[1][1] < self.hitbox[1] + self.hitbox[3] and rect[1][1] > self.hitbox[1] or rect[2][1] < self.hitbox[1] + self.hitbox[3] and rect[2][1] > self.hitbox[1]:
                    return True
        return False
