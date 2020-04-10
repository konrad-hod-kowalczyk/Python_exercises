import pygame as pg
from pygame.math import Vector2
class Rocket(object):
    def __init__(self,game):
        self.game=game
        self.speed = 1.6
        self.gravity = 0.957

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]/2)
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
    def __init__(self,game):
        self.game=game
        self.size = self.game.screen.get_size()
    def draw(self):
        pg.draw.rect(self.game.screen, (255, 255, 255), pg.Rect(0, 0, self.size[0]/12, self.size[1]))
        pg.draw.rect(self.game.screen, (255, 255, 255), pg.Rect(self.size[0]-100, 0, self.size[0]/12, self.size[1]))
