import random
import copy
from settings import *


class Cell:
    def __init__(self, x, y, options):
        self.x = x
        self.y = y
        self.options = options
        self.collapsed = False
        
    def draw(self, screen):
        if len(self.options) == 1:
            self.options[0].draw(screen, self.y * TILE, self.x * TILE)
            
    def entropy(self):
        return len(self.options)
    
    def update(self):
        self.collapsed = bool(self.entropy() == 1)
    
    def observe(self):
        try:
            self.options = [random.choice(self.options)]
            self.collapsed = True
        except:
            return
        
class Tile:
    def __init__(self, img):
        self.img = img
        self.index = -1
        self.edges = []
        self.up = []
        self.right = []
        self.down = []
        self.left = []
        
    def draw(self, screen, x, y):
        screen.blit(self.img, (x, y))
        
    def set_rules(self, tiles):
        for tile in tiles:
            # upper edge
            if self.edges[0] == tile.edges[2]:
                self.up.append(tile)
                
            # right edge
            if self.edges[1] == tile.edges[3]:
                self.right.append(tile)
                
            # bottom edge
            if self.edges[2] == tile.edges[0]:
                self.down.append(tile)
                
            # left edge
            if self.edges[3] == tile.edges[1]:
                self.left.append(tile)
                
class Grid:
    def __init__(self, options):
        self.grid = []
        self.options = options
        
    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                cell.draw(screen)
                
    def initiate(self):
        for i in range(COLS):
            self.grid.append([])
            for j in range(ROWS):
                cell = Cell(i, j, self.options)
                self.grid[i].append(cell)
                
    def heuristic_pick(self):
        grid_copy = [i for row in self.grid for i in row]
        grid_copy.sort(key = lambda x: x.entropy())
         
        filtered_grid = list(filter(lambda x: x.entropy() > 1, grid_copy))
        if filtered_grid == []:
            return None
         
        least_entropy_cell = filtered_grid[0]
        filtered_grid = list(filter(lambda x:x.entropy() == least_entropy_cell.entropy(), filtered_grid))
        pick = random.choice(filtered_grid)
        return pick
     
    def collapse(self):
        pick = self.heuristic_pick()
        if pick:
            self.grid[pick.x][pick.y].options
            self.grid[pick.x][pick.y].observe()
        else:
            return
        
        next_grid = copy.copy(self.grid)
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].collapsed:
                    next_grid[i][j] = self.grid[i][j]
                    
                else:
                    
                    cumulative_valid_options = self.options
                    
                    # check cell above
                    cell_above = self.grid[(i - 1) % COLS][j]
                    valid_options = []                         
                    for option in cell_above.options:
                        valid_options.extend(option.down)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check right cell
                    cell_right = self.grid[i][(j + 1) % ROWS]
                    valid_options = []                          
                    for option in cell_right.options:
                        valid_options.extend(option.left)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check down cell
                    cell_down = self.grid[(i + 1) % COLS][j]
                    valid_options = []                          
                    for option in cell_down.options:
                        valid_options.extend(option.up)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

                    # check left cell
                    cell_left = self.grid[i][(j - 1) % ROWS]
                    valid_options = []                         
                    for option in cell_left.options:
                        valid_options.extend(option.right)
                    cumulative_valid_options = [option for option in cumulative_valid_options if option in valid_options]

          
                    next_grid[i][j].options = cumulative_valid_options
                    next_grid[i][j].update()
                        
        self.grid = copy.copy(next_grid)
                        
        
            
            
            
