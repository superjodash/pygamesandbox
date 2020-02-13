from testapp import TestApp
from layers import TestLevel
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
    a.add_layer(TestLevel())
    a.run()


def testTmxLoader():
    map = Tilemap("assets/level_test.tmx")
    print(map)


if __name__ == "__main__":
    # runApp()
    # loadLevel()
    # testTiles()
    testTmxLoader()
