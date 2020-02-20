class Layer(object):

    def __init__(self):
        pass

    def on_render(self, time, buffer):
        pass

    def on_cleanup(self):
        pass


class EntityLayer(Layer):

    def __init__(self):
        super().__init__()
        self.entities = []

    def addEntity(self, entity):
        self.entities.append(entity)

    def on_render(self, time, buffer):
        pass

    def on_cleanup(self):
        pass
