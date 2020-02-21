

class Grid(object):
    
    def __init__(self):
        self.grid = {}
    
    def set(self, x, y, value):
        if self.grid.get(x) == None:
            self.grid[x] = {}
        self.grid[x][y] = value

    def get(self, x, y):
        ix  = self.grid[x]
        if ix != None:
            return ix[y]
        return None