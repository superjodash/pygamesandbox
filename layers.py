from layer import Layer
from tilemap import Tilemap
import pygame
import pygame.locals as pg

class TestLevel(Layer):

    def __init__(self):
        self._tm = Tilemap("level.map", "assets/smb_tileset.png")
        self._tilesize = self._tm.get_tilesize()
        self.canvassize = (0,0)

    def on_render(self, time, buffer):
        canvas = pygame.Surface(self.canvassize, pg.SRCALPHA)
        for y in range(self._tm.Level.height):
            for x in range(self._tm.Level.width):
                dx, dy = self._tilesize[0] * x, self._tilesize[1] * y
                img = self._tm.get_tile(x, y)
                if img != None:
                    canvas.blit(img, (dx, dy))
        buffer.blit(canvas, (0,0))