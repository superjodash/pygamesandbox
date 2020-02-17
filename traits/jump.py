from trait import Trait
from Vec2d import Vec2d

class Jump(Trait):
    def __init__(self):
        super().__init__('jump')
        self.duration = 0.05
        self.velocity = 200
        self.engageTime = 0

    def start(self):
        self.engageTime = self.duration

    def cancel(self):
        self.engageTime = 0

    def update(self, entity, deltaTime):
        if self.engageTime > 0:
            entity.vel = Vec2d(entity.vel.x, -self.velocity)
            self.engageTime -= deltaTime
