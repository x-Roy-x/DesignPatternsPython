import abc
import math


class Shape(abc.ABC):

    @abc.abstractmethod
    def accept(self, visitor):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def accept(self, visitor):
        visitor.square(self)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        visitor.circle(self)


class Visitor(abc.ABC):

    @abc.abstractmethod
    def square(self, square):
        pass

    @abc.abstractmethod
    def circle(self, circle):
        pass


class VisitorSquare(Visitor):

    def square(self, square):
        square_value = square.side * square.side
        print(f"Square square: {square_value}")

    def circle(self, circle):
        circle_value = math.pi * circle.radius * circle.radius
        print(f"Circle square: {circle_value}")


if __name__ == '__main__':

    shapes = [Square(2), Circle(2)]

    vs = VisitorSquare()

    for shape in shapes:
        shape.accept(vs)




