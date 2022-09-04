import pygame

WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
RED = (240, 28, 74)
WHITE = (235, 235, 235)
BLACK = (0, 0, 0)
BLUE = (91, 176, 222)
GRAY = (160, 160, 160)

crown = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(crown, (crown.get_width()//14, crown.get_height()//14))