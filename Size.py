
class Size(object):

    __slots__ = ("width", "height")

    def __init__(self, width_or_pair=None, height=None):
        if width_or_pair != None:
            if height == None:
                if hasattr(width_or_pair, "width") and hasattr(width_or_pair, "height"):
                    self.width = width_or_pair.width
                    self.height = width_or_pair.height
                else:
                    self.width = width_or_pair[0]
                    self.height = width_or_pair[1]
            else:
                self.width = width_or_pair
                self.height = height
        else:
            self.width = 0
            self.height = 0

    def __getitem__(self, i):
        if i == 0:
            return self.width
        elif i == 1:
            return self.height
        raise IndexError()

    def __iter__(self):
        yield self.width
        yield self.height

    def __len__(self):
        return 2

    def __setitem__(self, i, value):
        if i == 0:
            self.width = value
        elif i == 1:
            self.height = value
        else:
            raise IndexError()

    # String representaion (for debugging)
    def __repr__(self):
        return 'Size(%s, %s)' % (self.width, self.height)

    # Comparison
    def __eq__(self, other):
        if hasattr(other, "__getitem__") and len(other) == 2:
            return self.width == other[0] and self.height == other[1]
        else:
            return False

    def __ne__(self, other):
        if hasattr(other, "__getitem__") and len(other) == 2:
            return self.width != other[0] or self.height != other[1]
        else:
            return True

    def __nonzero__(self):
        return self.width != 0.0 or self.height != 0.0

    @staticmethod
    def zero():
        """A size of zero length"""
        return Size(0, 0)

    # Pickle
    def __reduce__(self):
        callable = Size
        args = (self.width, self.height)
        return (callable, args)
