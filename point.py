import math


class Point(object):

    # def __new__(cls, x, y):
        # return cls.__new__(name, coords)
        # return super(Point, cls).__new__(tuple, x, y)

    def __init__(self, *coords):
        super().__init__()
        assert isinstance(coords, tuple)
        assert len(coords) >= 2, "coords should be a multi-dimensional tuple"
        self.coords = coords  # tuple
        # for i, x in enumerate(coords):
        #     self[i] = x

    def __str__(self):
        return str(self.coords)

    def __repr__(self):
        return repr(self.coords)

    def norm(self):
        return math.sqrt(sum(x*x for x in self.coords))

    def __add__(self, other):
        return Point(*(sum(xs) for xs in zip(self.coords, other.coords)))

    def __mul__(self, scalar):
        return Point(*(x * scalar for x in self.coords))

    def __truediv__(self, scalar):
        return Point(*(x / scalar for x in self.coords))

    def __iter__(self):
        for x in self.coords: yield x

    def intify(self):
        return Point(*(int(x) for x in self.coords))
