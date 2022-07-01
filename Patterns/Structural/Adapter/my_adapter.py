
class Circle:

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius


class Square:

    def __init__(self, side):
        self.side = side


class SquareToCircleAdapter(Square, Circle):

    def __init__(self, side):
        super().__init__(side)

    def get_radius(self):
        return pow((2 * pow(self.side, 2)), 1/2) / 2


def fill_round_hole(figure, required_radius):
    radius = figure.get_radius()

    if radius <= required_radius:
        print(f"You can fill round hole. You have {radius} radius and required is {required_radius}")
    else:
        print(f"You can`t fill round hole. You have {radius} radius but required is {required_radius}")


if __name__ == "__main__":
    sq = SquareToCircleAdapter(2)
    cr = Circle(3)

    fill_round_hole(sq, 3)
    fill_round_hole(cr, 3)