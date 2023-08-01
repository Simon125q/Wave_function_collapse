import pygame
import sys
import random
from settings import *
from wave_collapse import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.pause = False
        
    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Wave function collapse")
        
    def draw(self):
        self.screen.fill("gray3")
    
    def check_events(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
    
    def run(self):
        while True:
            self.check_events()
            if not self.pause:
                self.draw()
            self.update()
            
            
        
            
if __name__ == "__main__":
    game = Game()
    game.run()
