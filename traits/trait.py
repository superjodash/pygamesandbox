import warnings

class Trait(object):

    def __init__(self, name):
        self.NAME = name
        pass

    def update(self, entity, deltaTime):
        warnings.warn("Abstract trait method update called.")
        pass