from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Specification:

    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification([self, other])


class ColorSpecification(Specification):

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    
    def __init__(self, specifications):
        self.specifications = specifications

    def is_satisfied(self, item):
        return all(map(
            lambda specification: specification.is_satisfied(item), self.specifications
        ))


class ProductFilter:

    def get_by_color(self, products, color):
        for product in products:
            if product.color == color:
                yield product

    # You can write more and more filters. Open for extension , close foe modification
    """
    def get_by_size(self, products, size):
        for product in products:
            if product.size == size:
                yield product

    def get_by_color_and_size(self, products, color, size):
        for product in products:
            if product.color == color and product.size == size:
                yield product

    """


class Filter(Specification):

    @staticmethod
    def filter(items, specification):
        pass


class BetterProductFilter(Filter):

    @staticmethod
    def filter(items, specification):
        for item in items:
            if specification.is_satisfied(item):
                yield item
