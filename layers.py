from layer import Layer, EntityLayer
from tilemap import Tilemap
import pygame
import pygame.locals as pg


class TestLevel(Layer):

    def __init__(self):
        self._tm = Tilemap("level.map", "assets/smb_tileset.png")
        self._tilesize = self._tm.get_tilesize()
        self.canvassize = (0, 0)  # gets set before first call

    def on_render(self, time, buffer):
        #canvas = pygame.Surface(self.canvassize, pg.SRCALPHA)
        # for layer in self._tm._layers:
        #     for t in layer.
        pass


class TextLayer(Layer):

    def __init__(self):
        self.canvassize = (0, 0)  # gets set before first call

    def on_render(self, time, buffer):
        basicfont = pygame.font.SysFont(None, 24)
        text = basicfont.render("text", True, (0, 0, 0))
        buffer.blit(text, (50, 50))


class BackgroundLayer(Layer):

    def __init__(self, rect, tileLayerIndex, tileMap):
        super().__init__()
        self.rect = rect
        self.tileLayerIndex = tileLayerIndex
        self.tileMap = tileMap
        self.tile_size = self.tileMap.map.tile_size
        self.dx = int(self.rect.width / self.tile_size.width)
        self.dy = int(self.rect.height / self.tile_size.height)

    def on_render(self, time, buffer):
        for y in range(self.dy):
            for x in range(self.dx):
                buffer.blit(
                    self.tileMap.image_at_index(
                        self.tileLayerIndex, x + self.rect.x, y + self.rect.y),
                    (x * self.tile_size.width, y * self.tile_size.height))


class ForegroundLayer(Layer):

    def __init__(self, rect, tileLayerIndex, tileMap):
        super(Layer, self).__init__()
        self.rect = rect
        self.tileLayerIndex = tileLayerIndex
        self.tileMap = tileMap
        self.tile_size = self.tileMap.map.tile_size
        self.dx = int(self.rect.width / self.tile_size.width)
        self.dy = int(self.rect.height / self.tile_size.height)

    def on_render(self, time, buffer):
        for y in range(self.dy):
            for x in range(self.dx):
                buffer.blit(
                    self.tileMap.image_at_index(
                        self.tileLayerIndex, x + self.rect.x, y + self.rect.y),
                    (x * self.tile_size.width, y * self.tile_size.height))


class BackgroundEntityLayer(EntityLayer):

    def __init__(self):
        super().__init__()

    def on_render(self, time, buffer):
        for e in self.entities:
            if e.sprite != None:
                buffer.blit(e.sprite, (e.pos.x * e.sprite.width,
                                       e.pos.y * e.sprite.height))
