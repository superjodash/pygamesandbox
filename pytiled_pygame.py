"""
Classes and utilities for loading pytiled (Tiled TMX) parsed files into pygame

    Load map
    Create pygame.sprite for each tile

"""
import os
import sys
import pygame
import math
import pytiled_parser as pyt


class Tilemap(object):

    def __init__(self, tmxfile, assetdir=sys.path[0]):
        self.map = pyt.parse_tilemap(os.path.join(assetdir,tmxfile))
        self.tilesets = {}
        self.layers = []
        for l in self.map.layers:
            self.layers.append(TileLayer(l))
        self.assetdir = assetdir
        for k in self.map.tile_sets:
            self.tilesets[k] = Tileset(self.map.tile_sets[k], self.assetdir)

    def tilesetselector(self, index):
        runningtc = 0
        for i in self.tilesets:
            runningtc += self.tilesets[i].tile_count
            if(index < runningtc):
                return self.tilesets[i]
        raise ValueError(index, "Invalid index range")

    def image_at(self, layerIndex, rectangle):
        spriteIx = self.layers[layerIndex].data_at(rectangle)
        tileset = self.tilesetselector(spriteIx)
        return tileset.image_at_index(spriteIx)


class TileLevel(object):

    def __init__(self):
        pass


class TileLayer(object):
    def __init__(self, layer):
        self.collision = layer.properties['Collision']
        self.name = layer.name
        self.data = layer.data

    def data_at(self, rectangle):
         rect = pygame.Rect(rectangle)
         return self._data[rect.y][rect.x]


class Tileset(object):
    def __init__(self, tileset, assetdir):
        self._imageCache = {}
        self.tileset = tileset
        self.tile_count = self.tileset.tile_count
        self.usecache = True
        try:
            fp = os.path.join(assetdir, tileset.image.source)
            self._sheet = pygame.image.load(fp).convert_alpha()
        except pygame.error as message:
            print('Unable to load spritesheet image:', tileset.image.source)
            raise SystemExit(message)

    def image_at_index(self, index):
        # assumes using tileset w/h
        w = self.tileset.max_tile_size.width
        h = self.tileset.max_tile_size.height
        y = math.floor(index / self.tileset.columns) * h
        x = (index % self.tileset.columns) * w
        return self.image_at([x, y, w, h])
        

    def image_at(self, rectangle, colorkey=None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        cached = self._imageCache.get(str(rectangle))
        if cached == None:
            image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
            image.blit(self._sheet, (0, 0), rect)
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0, 0))
                image.set_colorkey(colorkey, pygame.RLEACCEL)
            if self.usecache:
                self._imageCache[str(rectangle)] = image
            return image
        else:
            return cached

# use this to get a movable object on the screen
# this will have its own position, image, animation, etc
# class TileSprite(pygame.sprite.Sprite):
