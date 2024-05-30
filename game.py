import sys

import pygame

from elements.Ball import Ball
from elements.player import Player

width = 640
height = 480
background_green = (0, 63, 0)

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
ball = Ball()
player = Player()

pygame.key.set_repeat(30)
pygame.display.set_caption('JuegoBloques')

while True:
    clock.tick(60)

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                sys.exit()
            case pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.rect.left > 0:
                    player.speed = [-5, 0]
                    player.update()
                elif event.key == pygame.K_RIGHT and player.rect.right < width:
                    player.speed = [5, 0]
                    player.update()


    ball.update()
    screen.fill(background_green)
    screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
