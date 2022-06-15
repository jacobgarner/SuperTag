import pygame
from settings import *


class Terrain(pygame.sprite.Sprite):
    def __init__(self, pos, groups, type):
        super().__init__(groups)
        if type == 'big_plat':
            self.image = pygame.image.load('SuperTagImages/big plattform.PNG').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        elif type == 'med_plat':
            self.image = pygame.image.load('SuperTagImages/short plattform.PNG').convert_alpha()
            self.rect = self.image.get_rect(topleft=pos)
        elif type == 'small_plat':
            self.image = pygame.image.load('SuperTagImages/plat.png')
            self.rect = self.image.get_rect(topleft=pos)
        elif type == 'G':
            self.image = pygame.image.load('SuperTagImages/grass block.PNG').convert()
            self.rect = self.image.get_rect(topleft=pos)


