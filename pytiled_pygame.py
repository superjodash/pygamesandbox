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
from spritesheet import Spritesheet


def loadTilemap(tmx_file, assetdir=sys.path[0]):
    map = pyt.parse_tile_map(os.path.join(assetdir, tmx_file))
    return Tilemap(map, assetdir)


def loadTileset(tsx_file, assetdir=sys.path[0]):
    map = pyt.parse_tile_set(os.path.join(assetdir, tsx_file))
    return Tileset(map, assetdir)


class Tilemap(object):

    def __init__(self, tilemap: pyt.objects.TileMap, assetdir):
        self.map = tilemap
        self.assetdir = assetdir
        self.tilesets = {}
        self.layers = []
        for l in self.map.layers:
            self.layers.append(TileLayer(l))
        for k in self.map.tile_sets:
            self.tilesets[k] = Tileset(self.map.tile_sets[k], self.assetdir)

    def tilesetselector(self, index):
        runningtc = 0
        for i in self.tilesets:
            runningtc += self.tilesets[i].tile_count
            if(index < runningtc):
                return self.tilesets[i]
        raise ValueError(index, "Invalid index range")

    def get_layer(self, name):
        for l in self.layers:
            if l.name == name:
                return l
        return None

    def id_at_index(self, layerIndex, x, y):
        return self.layers[layerIndex].data_at(x, y)

    def image_at_id(self, id):
        tileset = self.tilesetselector(id)
        return tileset.image_at_index(id)

    def image_at_index(self, layerIndex, x, y):
        spriteIx = self.layers[layerIndex].data_at(x, y)
        return self.image_at_id(spriteIx)

    def image_at(self, layerIndex, rectangle):
        spriteIx = self.layers[layerIndex].data_at(rectangle)
        return self.image_at_id(spriteIx)


class TileLevel(object):

    def __init__(self):
        pass


class TileLayer(object):
    def __init__(self, layer):
        self.collision = layer.properties['Collision']
        self.size = layer.size
        self.name = layer.name
        self.data = layer.data

    def data_at(self, x, y):
        return self.data[y][x]


class Tileset(object):
    def __init__(self, tileset, assetdir):
        self._imageCache = {}
        self.tileset = tileset
        self.tile_count = self.tileset.tile_count
        self.usecache = True

        fp = os.path.join(assetdir, tileset.image.source)
        self._spriteSheet = Spritesheet(fp)

    def image_at_index(self, index):
        rawIndex = index - 1
        # assumes using tileset w/h
        w = self.tileset.max_tile_size.width
        h = self.tileset.max_tile_size.height
        y = math.floor(rawIndex / self.tileset.columns) * h
        x = (rawIndex % self.tileset.columns) * w
        return self.image_at([x, y, w, h])

    def image_at(self, rectangle, colorkey=None):
        return self._spriteSheet.image_at(rectangle)

# use this to get a movable object on the screen
# this will have its own position, image, animation, etc
# class TileSprite(pygame.sprite.Sprite):
