from compositor import Compositor

class Level(object):

    def __init__(self):
        self.comp = Compositor()
        self.entities = set()

    def update(self, deltaTime):
        for entity in self.entities:
            entity.update(deltaTime)

