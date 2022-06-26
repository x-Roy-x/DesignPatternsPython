import abc
from enum import Enum


class City(Enum):

    LVIV = 1
    WARSZAWA = 2
    INSTANBUL = 2


coordinate = {
    City.LVIV: (1.24, 2.35),
    City.WARSZAWA: (3.54, 6.77),
    City.INSTANBUL: (5.1, 4.54),
}


class DeliveryVehicle:

    @abc.abstractmethod
    def __init__(self, start_point, end_point, cargo):
        pass

    @abc.abstractmethod
    def delivery(self):
        pass

    @abc.abstractmethod
    def get_price(self):
        pass


class DeliveryTrack(DeliveryVehicle):

    def __init__(self, start_point, end_point, cargo):
        self.start_point = start_point
        self.end_point = end_point
        self.cargo = cargo

    def delivery(self):
        return str(self)

    def get_price(self):
        return 0.5 * 2

    def __str__(self):
        return f"Track move. Start is in {self.start_point}, end is in {self.end_point}.\n Cargo: {self.cargo}"


class DeliveryShip(DeliveryVehicle):

    def __init__(self, start_point, end_point, cargo):
        self.start_point = start_point
        self.end_point = end_point
        self.cargo = cargo

    def delivery(self):
        return str(self)

    def get_price(self):
        distance = self.get_distance()
        return 5 * distance

    def get_distance(self):
        return pow(
            pow((self.end_point[0] - self.start_point[0]), 2) + pow((self.end_point[1] - self.start_point[1]), 2), 0.5
        )

    def __str__(self):
        return f"Ship started to move from {self.start_point}, it point is {self.end_point}.\n Cargo: {self.cargo}"


class DeliveryFactory:

    @abc.abstractmethod
    def factory_method(self):
        pass

    def get_information(self):
        delivery_vehicle = self.factory_method()

        base_info = delivery_vehicle.delivery()
        price = delivery_vehicle.get_price()

        return f"{base_info}\n Price : {price}"


class TrackFactory(DeliveryFactory):

    def __init__(self, loading_place, uploading_place, cargo):
        self.loading_place = loading_place
        self.uploading_place = uploading_place
        self.cargo = cargo

    def factory_method(self):
        return DeliveryTrack(self.loading_place, self.uploading_place, self.cargo)


class ShipFactory(DeliveryFactory):

    def __init__(self, loading_place, uploading_place, cargo):
        self.loading_place = coordinate[loading_place]
        self.uploading_place = coordinate[uploading_place]
        self.cargo = cargo

    def factory_method(self):
        return DeliveryShip(self.loading_place, self.uploading_place, self.cargo)


if __name__ == "__main__":
    tfi = TrackFactory(City.LVIV, City.WARSZAWA, "Sweets").get_information()
    print(tfi)

    tfi = ShipFactory(City.LVIV, City.INSTANBUL, "Car").get_information()
    print(tfi)

