

class Compositor(object):

    def __init__(self):
        self.layers = []

    def draw(self, buffer, camera):
        for layer in self.layers:
            layer(buffer, camera)