import sys
import time

import pygame

from elements.Scene import Scene

width = 640
height = 480
background_green = (0, 63, 0)
whiteColor = (255, 255, 255)


class EndGame(Scene):
    def update(self):
        self.play = False

    def draw(self, screen):
        font = pygame.font.SysFont('Arial', 60)
        text = font.render('GAME OVER', True, whiteColor)
        text_rect = text.get_rect()
        text_rect.center = (width / 2, height / 2)
        screen.blit(text, text_rect)
