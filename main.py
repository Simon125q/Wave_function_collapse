import pygame
import sys
import random
from settings import *
from wave_collapse import Grid, Tile, Cell

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.pause = False
        self.initinal_setup()
        
    def initinal_setup(self):
        options = []
        for i in range(1, 6):
            img = load_image(f"./{i}.png")
            options.append(Tile(img))
        
        options[0].edges = [0, 0, 0, 0]
        options[1].edges = [1, 1, 0, 1]
        options[2].edges = [1, 1, 1, 0]
        options[3].edges = [0, 1, 1, 1]
        options[4].edges = [1, 0, 1, 1]
        
        for i, tile in enumerate(options):
            tile.index = i
            tile.set_rules(options)
            
        self.wave = Grid(options)
            
    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption("Wave function collapse")
        
    def draw(self):
        self.screen.fill("gray")
        self.wave.draw(self.screen)
        self.wave.collapse()
    
    def check_events(self):
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = not self.pause
    
    def run(self):
        self.wave.initiate()
        while True:
            self.check_events()
            if not self.pause:
                self.draw()
            self.update()
            
            
        
            
if __name__ == "__main__":
    game = Game()
    game.run()
