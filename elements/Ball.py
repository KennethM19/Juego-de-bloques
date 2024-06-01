import pygame

width = 640
height = 480


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('images/balon.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speed = [3, 3]

    def update(self):
        self.rect.move_ip(self.speed)
        if self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= width or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]

