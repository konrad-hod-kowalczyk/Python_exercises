import pygame as pg
import sys
from objects import Rocket

class Game(object):
    def __init__(self):
        # Configuration
        self.tps_max = 60.0
        #initalization
        pg.init()
        self.screen = pg.display.set_mode((1280, 720))
        self.tps_clock=pg.time.Clock()
        self.tps_delta=0.0
        self.player=Rocket(self)
        while True:
            for event in pg.event.get():
                # Quitting
                if event.type == pg.QUIT:
                    sys.exit(0)
            # Ticking
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max
            #Rendering
            self.screen.fill((0, 0, 0))
            self.draw()
            pg.display.flip()
    def tick(self):
        # Input
        self.player.tick()

    def draw(self):
        # Drawing
        self.player.draw()
if __name__ == "__main__":
    Game()