import pygame
from settings import *


class PlayerOne(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.is_it = True
        if self.is_it:
            self.image = pygame.image.load('SuperTagImages/player1.png').convert_alpha()
        elif not self.is_it:
            self.image = pygame.image.load('SuperTagImages/player1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.gravity = 0.8
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = 16
        self.collision_sprites = collision_sprites
        self.on_floor = False

        # player score
        self.start_time = 6000
        self.time_it = 6000


    def check_is_it(self):
        if self.is_it:
            self.start_time -= 1
            return(self.start_time//100)
        else:
            return (self.start_time//100)


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1

        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.on_floor:
            self.direction.y = -self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.check_is_it()


class PlayerTwo(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.is_it = False
        self.image = pygame.image.load('SuperTagImages/player2.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        # player movement
        self.gravity = 0.8
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.jump_speed = 16
        self.collision_sprites = collision_sprites
        self.on_floor = False
        self.start_time = 6000
        self.time_it = 0


    def check_is_it(self):
        if self.is_it:
            self.start_time -= 1
            return(self.start_time//100)
        else:
            return (self.start_time//100)


    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_floor:
            self.direction.y = -self.jump_speed

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left


    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()
        self.check_is_it()
