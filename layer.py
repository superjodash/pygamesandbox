class Layer(object):

    def __init__(self):
        pass

    def on_render(self, time, buffer):
        pass

    def on_cleanup(self):
        pass

class BackgroundLayer(Layer):

    def __init__(self, rect, tileLayerIndex, tileMap):
        super(Layer, self).__init__()
        self.rect = rect
        self.tileLayerIndex = tileLayerIndex
        self.tileMap = tileMap
        self.tile_size = (self.tileMap.map.tile_size.width, self.tileMap.map.tile_size.height)

    def on_render(self, time, buffer):
        yh = int(self.rect.height / self.tileMap.map.tile_size.height)
        xh = int(self.rect.width / self.tileMap.map.tile_size.width)
        for y in range(yh):
            for x in range(xh):
                buffer.blit(
                    self.tileMap.image_at_index(self.tileLayerIndex, x + self.rect.x, y + self.rect.y), 
                    (x * self.tile_size[0], y * self.tile_size[1]))
