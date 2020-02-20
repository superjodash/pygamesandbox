from Vec2d import Vec2d


class Entity(object):
    def __init__(self):
        self._name = "Entity"
        self._traits = {}
        self.pos = Vec2d(0, 0)
        self.vel = Vec2d(0, 0)
        self.sprite = None

    def addTrait(self, trait):
        self._traits[trait.NAME] = trait

    def getTrait(self, name):
        return self._traits[name]

    def removeTrait(self, name):
        t = self.getTrait(name)
        del(t)

    def update(self, deltaTime):
        for t in self._traits:
            self._traits[t].update(self, deltaTime)

    def on_render(self, deltaTime, buffer):
        if self.sprite != None:
            buffer.blit(self.sprite, self.pos)
