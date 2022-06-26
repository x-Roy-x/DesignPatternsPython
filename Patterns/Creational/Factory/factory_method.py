from enum import Enum
from math import *


class CoordinateSystem(Enum):

    CARTESIAN = 1
    POLAR = 2


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(x, y):
        x = x * cos(y)
        y = x * sin(y)
        return Point(x, y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    """
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * cos(b)
            self.y = a * sin(b)
    """


if __name__ == "__main__":
    p = Point.new_polar_point(2, 2)
    print(p)



