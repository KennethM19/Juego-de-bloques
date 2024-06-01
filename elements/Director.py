import time

import pygame
from levels.LevelOne import LevelOne
from levels.EndGame import EndGame


class Director:
    def __init__(self, title = ""):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.scene = None
        self.scenes = {}

    def execute(self, initial_scene, fps=60):
        self.scene = self.scenes[initial_scene]
        play = True
        while play:
            self.clock.tick(fps)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    play = False

            self.scene.read_events(events)
            self.scene.update()
            self.scene.draw(self.screen)

            self.scene.choose_scene(self.scene.next_scene)

            if play:
                play = self.scene.play

            pygame.display.flip()

        time.sleep(3)

    def choose_scene(self, next_scene):
        if next_scene:
            if next_scene not in self.scenes:
                self.add_scene(next_scene)
            self.scene = self.scenes[next_scene]

    def add_scene(self, scene):
        dict_scene = {
            'LevelOne': LevelOne,
            'End Game': EndGame,
        }
        sceneClass = dict_scene.get(scene)
        if sceneClass:
            self.scenes[scene] = sceneClass()
