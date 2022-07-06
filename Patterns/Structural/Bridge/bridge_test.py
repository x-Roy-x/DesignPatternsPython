from abc import ABC


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer
        self.name = None


class Triangle(Shape):

    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Triangle'
        self.renderer.set_name(self.name)

    def __str__(self):
        return self.renderer.what_to_render_as


class Square(Shape):

    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = 'Square'
        self.renderer.set_name(self.name)

    def __str__(self):
        return self.renderer.what_to_render_as


class Renderer(ABC):

    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):

    def __init__(self):
        super().__init__()

    @property
    def what_to_render_as(self):
        return f'Drawing {self.name} as lines'


class RasterRenderer(Renderer):

    def __init__(self):
        super().__init__()

    @property
    def what_to_render_as(self):
        return f'Drawing {self.name} as pixels'


if __name__ == '__main__':
    vector_renderer = VectorRenderer()
    raster_renderer = RasterRenderer()

    triangle = Triangle(vector_renderer)
    print(triangle)
