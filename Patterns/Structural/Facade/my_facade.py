
class Perimeter:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Foundation(Perimeter):

    def __init__(self, length, width, depth, height, masonry_size):
        super().__init__(length, width)
        self.depth = depth
        self.height = height
        self.masonry_size = masonry_size

    def dig_foundation(self):
        print(f"Dig foundation {self.depth} depth")

    def make_casing(self):
        print(f"Make casing with {self.height} height")

    def get_concrete_volume(self):
        volume_forward = self.length * self.width * (self.depth + self.height)

        backward_length = self.length - 2 * self.masonry_size
        backward_width = self.width - 2 * self.masonry_size
        volume_backward = backward_length * backward_width * (self.depth + self.height)

        concrete_volume = volume_forward - volume_backward

        return concrete_volume

    def make_concrete(self):
        concrete_volume = self.get_concrete_volume()
        print(f"Make concrete with {concrete_volume} volume")


class Door(Perimeter):

    def __init__(self, length, width):
        super().__init__(length, width)


class Window(Perimeter):

    def __init__(self, length, width):
        super().__init__(length, width)


class Wall(Perimeter):

    def __init__(self, length, width, height, masonry_size):
        super().__init__(length, width)
        self.height = height
        self.masonry_size = masonry_size

        self.holes = []

    def add_window(self, length, width):
        self.holes.append(Window(length, width))

    def add_door(self, length, width):
        self.holes.append(Door(length, width))

    def get_hole_volume(self):
        hole_volume = 0

        for hole in self.holes:
            hole_volume += hole.length * hole.width * self.masonry_size

        return hole_volume

    def get_masonry_volume(self):
        hole_volume = self.get_hole_volume()

        volume_forward = self.length * self.width * self.height

        backward_length = self.length - 2 * self.masonry_size
        backward_width = self.width - 2 * self.masonry_size
        volume_backward = backward_length * backward_width * self.height

        masonry_volume = volume_forward - volume_backward

        masonry_volume = masonry_volume - hole_volume

        return masonry_volume

    def make_wall(self):
        brick_volume = self.get_masonry_volume()
        print(f"Make wall. Required brick: {brick_volume} volume")


class BuilderFacade:

    def __init__(self, foundation, wall):
        self.foundation = foundation
        self.wall = wall

    def get_concrete_volume(self):
        self.foundation.get_concrete_volume()

    def make_foundation(self):
        self.foundation.dig_foundation()
        self.foundation.make_casing()
        self.foundation.make_concrete()

    def add_window(self, length, width):
        self.wall.add_window(length, width)

    def add_door(self, length, width):
        self.wall.add_door(length, width)

    def make_wall(self):
        self.wall.make_wall()


if __name__ == '__main__':
    foundation = Foundation(5, 5, 0.7, 0.3, 0.5)
    wall = Wall(5, 5, 3, 0.5)

    builder = BuilderFacade(foundation, wall)

    builder.make_foundation()
    builder.get_concrete_volume()

    builder.add_window(1, 1)
    builder.add_window(2, 1)
    builder.add_door(1, 2)

    builder.make_wall()
