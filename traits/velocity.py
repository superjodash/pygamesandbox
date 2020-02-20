from traits.trait import Trait
from Vec2d import Vec2d


class Velocity(Trait):

    def __init__(self):
        super().__init__("vel")

    def update(self, entity, deltaTime):
        entity.pos = Vec2d(entity.pos.x + entity.vel.x * deltaTime,
                           entity.pos.y + entity.vel.y * deltaTime)
