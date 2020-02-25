from Vec2d import Vec2d
from Size import Size
import pygame


class Entity(object):
    def __init__(self, name="Entity"):
        self._name = name
        self._traits = {}
        self.pos = Vec2d(0, 0)
        self.vel = Vec2d(0, 0)
        self.size = Size(0, 0)
        self.sprite = None
        self.debug = True

    def addTrait(self, trait):
        self._traits[trait.NAME] = trait

    def getTrait(self, name):
        return self._traits[name]

    def removeTrait(self, name):
        t = self.getTrait(name)
        del(t)

    def on_update(self, deltaTime):
        for t in self._traits:
            self._traits[t].update(self, deltaTime)

    def on_render(self, deltaTime, buffer):
        if self.sprite != None:
            buffer.blit(self.sprite, self.pos)
        if self.debug:
            pygame.draw.rect(buffer, (0, 0, 255), pygame.Rect(
                self.pos.x, self.pos.y, self.size.width, self.size.height), 1)
