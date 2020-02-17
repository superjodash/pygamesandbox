

class Compositor(object):

    def __init__(self):
        self.layers = []

    def draw(self, context, camera):
        for layer in self.layers:
            layer(context, camera)