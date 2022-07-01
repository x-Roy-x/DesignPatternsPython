class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw_point(self):
        print(f"-x: {self.x}\ty: {self.y}")


class LineToPointAdapter(list):

    def __init__(self, line):
        super().__init__()

        print(f"Generating points for line '[{line.start.x}, {line.start.y}]' -> '[{line.end.x}, {line.end.y}]'")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif bottom - top == 0:
            for x in range(left, right):
                self.append(Point(x, top))


class Line:

    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


def draw(rectangles):
    for rectangle in rectangles:
        for line in rectangle:
            adapter = LineToPointAdapter(line)

            for p in adapter:
                p.draw_point()


if __name__ == "__main__":
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]

    draw(rectangles)
