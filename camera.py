from Vec2d import Vec2d

class Camera(object):

    def __init__(self, width, height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.pos = Vec2d(0, 0)