from level import Level
from spritesheet import Spritesheet

class Tilemap(object):

    def __init__(self, levelfile, spritesheetfile):
        self.Level = Level()
        self.Level.load_file(levelfile)
        self.Spritesheet = Spritesheet(spritesheetfile)

    def get_tilesize(self):
        return self.Level.tilesize

    def get_tile(self, x, y):
        t = self.Level.get_tuple(x,y,"tile")
        if t != None and t[0] != -1:
            return self.Spritesheet.image_at(t)
        return None