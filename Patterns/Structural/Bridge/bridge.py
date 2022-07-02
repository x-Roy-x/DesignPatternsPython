import abc


class Render(abc.ABC):

    @abc.abstractmethod
    def render_circle(self, radius):
        pass

    #render_square


class VectorRender(Render):

    def render_circle(self, radius):
        print(f"Drawing circle of radius {radius}")


class RasterRender(Render):

    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass

    def resize(self): pass


class Circle(Shape):

    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    vector_render = VectorRender()
    raster_render = RasterRender()

    circle = Circle(raster_render, 5)
    circle.draw()
