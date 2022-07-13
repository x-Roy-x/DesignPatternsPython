
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f"circle of radius {self.radius}"


class Square:
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f"square of side {self.side}"


class ColoredShape:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def resize(self, factor):
        r = getattr(self.shape, 'resize', None)

        if r is not None:
            self.shape.resize(factor)

    def __getattr__(self, item):
        return getattr(self.__dict__["shape"], item)

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __str__(self):
        return f"{self.shape} has the color {self.color}"


if __name__ == '__main__':
    circle = ColoredShape(Circle(5), "red")

    circle.resize(2)

    print(circle)

