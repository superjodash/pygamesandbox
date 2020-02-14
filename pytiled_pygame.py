"""
Classes and utilities for loading pytiled (Tiled TMX) parsed files into pygame

    Load map
    Create pygame.sprite for each tile

"""
import os
import sys
import pygame
import pytiled_parser as pyt


class Tilemap(object):

    def __init__(self, tmxfile, assetdir=sys.path[0]):
        self._map = pyt.parse_tile_map(os.path.join(assetdir,tmxfile))
        self._tilesets = {}
        self._assetdir = assetdir
        for k in self._map.tile_sets:
            self._tilesets[k] = Tileset(self._map.tile_sets[k], self._assetdir)


class Tileset(object):
    def __init__(self, tileset, assetdir):
        self._imageCache = {}
        self._tileset = tileset
        self.usecache = True
        try:
            fp = os.path.join(assetdir, tileset.image.source)
            self._sheet = pygame.image.load(fp).convert_alpha()
        except pygame.error as message:
            print('Unable to load spritesheet image:', tileset.image.source)
            raise SystemExit(message)

    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        cached = self._imageCache.get(rect)
        if cached == None:
            image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
            image.blit(self._sheet, (0, 0), rect)
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey, pygame.RLEACCEL)
            if self.usecache:
                self._imageCache[rect] = image
            return image
        else:
            return cached

# use this to get a movable object on the screen
# this will have its own position, image, animation, etc
# class TileSprite(pygame.sprite.Sprite):
