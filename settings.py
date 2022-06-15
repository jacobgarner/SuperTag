import pygame

pygame.init()
LEVEL_LAYOUT = [
    '                  ',
    '                  ',
    '  B        B      ',
    '                  ',
    '                  ',
    'L      M         L',
    '   L          L   ',
    '1                2',
    'G  G   G   G  G  G',
    '                  ',
]

SCREEN_WIDTH, SCREEN_HEIGHT = 900, 500
TILE_SIZE = 50
PLAYER_SIZE = 30
BIG_PLAT_WIDTH = 50
MED_PLAT_SIZE = 242
SMALL_PLAT_SIZE = 0
FONT = pygame.font.Font('SuperTagImages/font/Pixeltype.ttf', 50)
