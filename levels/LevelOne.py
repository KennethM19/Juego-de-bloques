import pygame

from elements.Ball import Ball
from elements.Player import Player
from elements.Scene import Scene
from elements.Walls import Walls

width = 640
height = 480
background_green = (0, 63, 0)
whiteColor = (255, 255, 255)


class LevelOne(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.ball = Ball()
        self.player = Player()
        self.walls = Walls(50)

        self.score = 0
        self.lives = 3
        self.waitStart = True

        pygame.key.set_repeat(30)

    def read_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.player.update()
                if self.waitStart and event.key == pygame.K_ESCAPE:
                    self.waitStart = False
                    if self.ball.rect.centerx < width / 2:
                        self.ball.speed = [3, -3]
                    else:
                        self.ball.speed = [3, -3]

    def update(self):
        if not self.waitStart:
            self.ball.update()
        else:
            self.ball.rect.midbottom = self.player.rect.midtop

        if pygame.sprite.collide_rect(self.ball, self.player):
            self.ball.speed = -self.ball.speed

        list = pygame.sprite.spritecollide(self.player, self.walls, False)
        if list:
            wall = list[0]
            centerx = self.ball.rect.centerx
            if centerx < wall.rect.left or centerx > wall.rect.right:
                self.ball.speed[0] = -self.ball.speed[0]
            else:
                self.ball.speed[1] = -self.ball.speed[1]
            self.walls.remove(wall)
            self.score += 1

        if self.ball.rect.bottom > width:
            self.lives -= 1
            self.waitStart = True

        if self.lives == 0:
            self.change_scene("GAME OVER")

    def draw(self, screen):
        screen.fill(background_green)
        self.show_score(screen)
        self.show_lives(screen)
        screen.blit(self.ball.image, self.ball.rect)
        screen.blit(self.player.image, self.player.rect)
        self.walls.draw(screen)

    def show_score(self, screen):
        font = pygame.font.SysFont('Consolas', 20)
        text = font.render(str(self.score).zfill(5), True, whiteColor)
        text_rect = text.get_rect()
        text_rect.topleft = [0, 0]
        screen.blit(text, text_rect)

    def show_lives(self, screen):
        font = pygame.font.SysFont('Consolas', 20)
        text = font.render("LIVES: " + str(self.lives).zfill(1), True, whiteColor)
        text_rect = text.get_rect()
        text_rect.topright = [width, 0]
        screen.blit(text, text_rect)
