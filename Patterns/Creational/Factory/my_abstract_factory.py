import abc
from abc import ABC
from enum import Enum


class Upholstery(Enum):

    NET = 0
    SKIN = 1
    TEXTILE = 2


class Material(Enum):

    GLASS = 0
    WOOD = 1
    IRON = 2


class Chair(ABC):

    @abc.abstractmethod
    def __init__(self, upholstery, material):
        self.upholstery = upholstery
        self.material = material

    def __str__(self):
        return f"Chair: \n\tupholstery: {self.upholstery}\n\tmaterial: {self.material}"


class Sofa(ABC):

    @abc.abstractmethod
    def __init__(self, upholstery, material, place):
        self.upholstery = upholstery
        self.material = material
        self.place = place

    def __str__(self):
        return f"Sofa: \n\tupholstery: {self.upholstery}\n\tmaterial: {self.material}\n\tplace: {self.place}"


class Table(ABC):

    @abc.abstractmethod
    def __init__(self, covering, material, place):
        self.covering = covering
        self.material = material
        self.place = place

    def __str__(self):
        return f"Sofa: \n\tmaterial: {self.material}\n\tplace: {self.place}"


class FurnitureFactory(ABC):

    @staticmethod
    @abc.abstractmethod
    def create_chair(upholstery) -> Chair:
        pass

    @staticmethod
    @abc.abstractmethod
    def create_sofa(upholstery, place) -> Sofa:
        pass

    @staticmethod
    @abc.abstractmethod
    def create_table() -> Table:
        pass


class OfficeChair(Chair):

    def __init__(self, upholstery, material, wheels):
        self.upholstery = upholstery
        self.material = material
        self.wheels = wheels


class OfficeSofa(Sofa):

    def __init__(self, upholstery, material, place):
        self.upholstery = upholstery
        self.material = material
        self.place = place


class OfficeTable(Table):

    def __init__(self, covering, material, place, drawers):
        self.covering = covering
        self.material = material
        self.place = place
        self.drawers = drawers


class OfficeFurnitureFactory(FurnitureFactory):

    @staticmethod
    def create_chair(upholstery) -> Chair:
        return OfficeChair(upholstery, Material.IRON, True)

    @staticmethod
    def create_sofa(upholstery, place) -> Sofa:
        return OfficeSofa(upholstery, Material.IRON, place)

    @staticmethod
    def create_table() -> Table:
        return OfficeTable(Material.WOOD, Material.IRON, 1, True)


if __name__ == "__main__":
    off = OfficeFurnitureFactory.create_chair(Upholstery.NET)
    print(off)
