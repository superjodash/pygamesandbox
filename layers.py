from layer import Layer
from tilemap import Tilemap
import pygame
import pygame.locals as pg

class TestLevel(Layer):

    def __init__(self):
        self._tm = Tilemap("level.map", "assets/smb_tileset.png")
        self._tilesize = self._tm.get_tilesize()
        self.canvassize = (0,0) # gets set before first call

    def on_render(self, time, buffer):
        canvas = pygame.Surface(self.canvassize, pg.SRCALPHA)
        # for layer in self._tm._layers:
        #     for t in layer.

class TextLayer(Layer):

    def __init__(self):
        self.canvassize = (0,0) # gets set before first call

    def on_render(self, time, buffer):
        basicfont = pygame.font.SysFont(None, 24)
        text = basicfont.render("text", True, (0, 0, 0))
        buffer.blit(text, (50, 50))