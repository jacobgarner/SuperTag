import pygame
from settings import *
from window import *
from player import *


class Level:
    def __init__(self):
        # Level set up
        self.display_surface = pygame.display.get_surface()

        # Sprite group
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.setup_level()
        self.player_one = PlayerOne((0, 0), [self.visible_sprites, self.active_sprites], self.collision_sprites)
        self.player_two = PlayerTwo((870, 0), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def setup_level(self):
        for row_index, row in enumerate(LEVEL_LAYOUT):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                # if col == '1':
                #     PlayerOne((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                if col == 'G':
                    Terrain((x, y), [self.visible_sprites, self.collision_sprites], 'G')
                # if col == '2':
                #     PlayerTwo((x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)
                if col == 'B':
                    Terrain((x, y), [self.visible_sprites, self.collision_sprites], 'big_plat')
                if col == 'M':
                    Terrain((x, y), [self.visible_sprites, self.collision_sprites], 'med_plat')
                if col == 'L':
                    Terrain((x, y), [self.visible_sprites, self.collision_sprites], 'small_plat')

    def check_coll(self):
        if self.player_one.rect.colliderect(self.player_two.rect):
            self.player_one.rect.center = (0, 0)
            self.player_two.rect.center = (870, 0)
            if self.player_one.is_it:
                self.player_one.is_it = False
                self.player_two.is_it = True
            elif self.player_two.is_it:
                self.player_one.is_it = True
                self.player_two.is_it = False

    def border(self):
        if self.player_one.rect.right >= 900:
            self.player_one.rect.right = 900
        if self.player_one.rect.left <= 0:
            self.player_one.rect.left = 0
        if self.player_two.rect.right >= 900:
            self.player_two.rect.right = 900
        if self.player_two.rect.left <= 0:
            self.player_two.rect.left = 0

    # def display_score(self):
    #     score_surf = FONT.render(f'Time remaining: {self.player_one.check_is_it()}', False, (64, 64, 64))
    #     score_rect = score_surf.get_rect(topleft=(0, 0))
    #     WIN.blit(score_surf,score_rect)


    def run(self):
        # Run the game
        self.active_sprites.update()
        self.visible_sprites.draw(self.display_surface)
        self.check_coll()
        self.border()

