

class Compositor(object):

    def __init__(self, level):
        self.level = level
        self.layers = []

    def draw(self, buffer, camera):
        for layer in self.layers:
            layer(self.level, buffer, camera)