import pygame

from elements.Wall import Wall

width = 640
height = 480


class Walls(pygame.sprite.Group):
    def __init__(self, qntWall):
        pygame.sprite.Group.__init__(self)

        posx = 0
        posy = 20
        for i in range(qntWall):
            wall = Wall((posx, posy))
            self.add(wall)
            posx += wall.rect.width
            if posx >= width:
                posx = 0
                posy += wall.rect.height
