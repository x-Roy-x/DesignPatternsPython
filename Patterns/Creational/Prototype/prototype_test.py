import copy


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


class Line:

    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def __str__(self):
        return f"Start - {self.start}\nEnd - {self.end}"

    def deep_copy(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    line1 = Line(Point(2, 2), Point(3, 3))
    line2 = line1.deep_copy()
    line2.start.x = 4

    print(line1)
    print(line2)

    line2.start.x = 2