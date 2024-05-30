import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/muro.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = position
