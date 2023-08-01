import pygame

RES = WIDTH, HEIGHT = (1200, 900)
TILE = 64
COLS = WIDTH // TILE
ROWS = HEIGHT // TILE
FPS = 10

def load_image(path, padding = 0):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.scale(img, (TILE - padding, TILE - padding))
    
    return img

