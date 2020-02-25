from compositor import Compositor
from Size import Size
from Grid import Grid

class Level(object):

    def __init__(self):
        self.comp = Compositor(self) # 
        self.entities = set()
        self.renderLayers = [] # Contains Grid[] layers for entire level; rendered in order (farthest -> nearest)
        self.grid = Grid() # Contains tile info for collision detection
        self.tile_size = Size(16, 16)
        self.level_size = Size()

    def on_update(self, deltaTime):
        for entity in self.entities:
            entity.on_update(deltaTime)

