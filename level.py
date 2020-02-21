from compositor import Compositor
from Grid import Grid

class Level(object):

    def __init__(self):
        self.comp = Compositor()
        self.entities = set()
        self.grid = Grid()

    def update(self, deltaTime):
        for entity in self.entities:
            entity.update(deltaTime)

