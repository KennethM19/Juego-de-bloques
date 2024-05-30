class Scene:
    def __init__(self):
        self.next_scene = False
        self.play = True

    def read_events(self, events):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def change_scene(self, scene):
        self.next_scene = scene
