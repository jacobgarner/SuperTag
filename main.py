import pygame
from sys import exit

import main
from settings import *
from level import Level
from player import *

# Pygame set up
pygame.init()
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
RUNNING = True
pygame.display.set_caption('SuperTag')
level = Level()
sky_background = pygame.image.load('SuperTagImages/sky1.png').convert()


def check_winner():
    if level.player_one.check_is_it() <= 0 or level.player_two.check_is_it() <= 0:
        return False
    else:
        return True


def display_score_player_one():
    score_surf = FONT.render(f'Time remaining: {level.player_one.check_is_it()}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(topleft=(0, 0))
    WIN.blit(score_surf, score_rect)


def display_score_player_two():
    score_surf = FONT.render(f'Time remaining: {level.player_two.check_is_it()}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(topright=(900, 0))
    WIN.blit(score_surf, score_rect)


def restart_game():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and RUNNING == False:
                main.RUNNING = True
                level.player_one.start_time = 6000
                level.player_two.start_time = 6000
                clock.tick(60)
        if event.type == pygame.QUIT:
            exit()


while True:
    if RUNNING:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING = False
                exit()

        level.run()

        RUNNING = check_winner()
        # Drawing logic
        pygame.display.update()
        clock.tick(60)
        WIN.blit(sky_background, (-100, -300))
        display_score_player_one()
        display_score_player_two()

    else:

        if level.player_one.check_is_it() <= 0:
            WIN.fill((255, 255, 255))
            start_again = FONT.render('Press space to play again!', False, (0, 0, 0))
            start_again_rect = start_again.get_rect(center=(450,300))
            game_over = FONT.render(
                f'WINNER: PLAYER TWO WITH {level.player_two.check_is_it()} POINTS REMAINING!', False, (0, 0, 0))
            game_over_rect = game_over.get_rect(center=(450, 250))
            WIN.blit(game_over, game_over_rect)
            WIN.blit(start_again,start_again_rect)
            winner = level.player_two.image
            winner = pygame.transform.rotozoom(winner, 0, 5)
            winner_rect = winner.get_rect(center=(450, 150))
            WIN.blit(winner, winner_rect)





        else:
            WIN.fill((255, 255, 255))
            start_again = FONT.render('Press space to play again!', False, (0, 0, 0))
            start_again_rect = start_again.get_rect(center=(450, 300))
            game_over = FONT.render(
                f'WINNER: PLAYER ONE WITH {level.player_one.check_is_it()} POINTS REMAINING!', False, (0, 0, 0))
            game_over_rect = game_over.get_rect(center=(450, 250))
            WIN.blit(game_over, game_over_rect)
            WIN.blit(start_again, start_again_rect)
            winner = level.player_one.image
            winner = pygame.transform.rotozoom(winner, 0, 5)
            winner_rect = winner.get_rect(center=(450, 150))
            WIN.blit(winner, winner_rect)

        pygame.display.update()
        clock.tick(60)
        restart_game()
