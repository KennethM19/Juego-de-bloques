import pygame.sprite

width = 640
height = 480


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/plataforma.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (width / 2, height - 20)
        self.speed = [0, 0]

    def update(self):
        self.rect.move_ip(self.speed)
