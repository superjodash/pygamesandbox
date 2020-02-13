from testapp import TestApp
from level import Level
from tilemap import Tilemap
from layers import TestLevel


"""
Mario
Screen: 320x240 (20x15 tiles)
Sprites: 8x8 and 8x16

"""


def loadLevel():
    level = Level()
    level.load_file()
    for y in range(level.height):
        for x in range(level.width):
            print((x,y), level.get_tile(x, y))

def testTiles():
    tm = Tilemap("level.map", "assets/smb_tileset.png")
    for y in range(tm.Level.height):
        for x in range(tm.Level.width):
            print((x,y), tm.get_tile(x, y))

if __name__ == "__main__":
    #a = TestApp((320, 240))
    a = TestApp((640, 480))
    a.add_layer(TestLevel())
    a.run()
    #theApp.run()
    #loadLevel()
    #testTiles()
