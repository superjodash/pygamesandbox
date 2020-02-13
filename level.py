from configparser import ConfigParser


class Level(object):

    def load_file(self, filename="level.map"):
        self.map = []
        self.key = {}
        parser = ConfigParser()
        parser.read(filename)
        self.tileset = parser.get("level", "tileset")
        self.tilesize = eval(parser.get("level", "tilesize"))
        self.map = parser.get("level", "map").split("\n")
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.width = len(self.map[0])
        self.height = len(self.map)

    def get_tile_data(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}
        try:
            return self.key[char]
        except KeyError:
            return {}

    def get_tuple(self, x, y, key):
        v = self.get_tile_data(x, y)
        if v == {}:
            return None
        return eval(v[key])

    def get_bool(self, x, y, key):
        v = self.get_tile_data(x, y)
        if v == {}:
            return None
        return bool(v[key])

    def get_str(self, x, y, key):
        v = self.get_tile_data(x, y)
        if v == {}:
            return None
        return str(v[key])

    def get_int(self, x, y, key):
        v = self.get_tile_data(x, y)
        if v == {}:
            return None
        return int(v[key])

    def get_float(self, x, y, key):
        v = self.get_tile_data(x, y)
        if v == {}:
            return None
        return float(v[key])