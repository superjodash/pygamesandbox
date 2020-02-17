import os, sys
from testapp import TestApp
from layers import *
import pygame
from pytiled_pygame import *
import pytiled_parser

"""
Mario
Screen: 320x240 (20x15 tiles)
Sprites: 8x8 and 8x16

"""


def runApp():
    #a = TestApp((320, 240))
    a = TestApp((640, 480))
    a.run()


def testTmxLoader():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    path = sys.path[0]
    assetdir = os.path.join(path, 'assets')
    map = Tilemap("level_test.tmx", assetdir)
    img = map.image_at(0, (0, 0, 16, 16))
    #print(map._map.__dict__)


if __name__ == "__main__":
    runApp()
    # loadLevel()
    # testTiles()
    #testTmxLoader()
