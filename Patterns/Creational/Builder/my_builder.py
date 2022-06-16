class Car:

    def __init__(self):
        self.name = None
        self.engine = None
        self.wheels = 4
        self.doors = 4
        self.cistern = None
        self.automatic_parking = False

    def __str__(self):
        return f"{self.name} has: {self.engine}"


class CarBuilder:

    def __init__(self):
        self._car = Car()

    def take_car(self):
        return self._car

    def set_name(self, name):
        self._car.name = name
        return self

    def set_engine(self, engine):
        self._car.engine = engine
        return self

    def set_wheels(self, wheels):
        self._car.wheels = wheels
        return self

    def set_doors(self, doors):
        self._car.doors = doors
        return self

    def set_cistern(self, cistern):
        self._car.cistern = cistern
        return self

    def set_automatic_parking(self, automatic_parking):
        self._car.automatic_parking = automatic_parking
        return self


class CarDirector:

    def __init__(self):
        self.cars = []

    def take_electronic_car(self):
        cb = CarBuilder()
        take_c = cb \
            .set_name("Tesla") \
            .set_engine("Electric motor") \
            .set_doors(2) \
            .set_automatic_parking(True) \
            .take_car()

        self.cars.append(take_c)
        return take_c

    def take_truck_car(self):
        cb = CarBuilder()
        take_c = cb \
            .set_name("Truck") \
            .set_engine("Petrol motor") \
            .set_wheels(8) \
            .set_cistern(200)\
            .take_car()

        self.cars.append(take_c)
        return take_c

    def take_custom_car(self, name, engine):
        cb = CarBuilder()
        take_c = cb \
            .set_name(name) \
            .set_engine(engine) \
            .set_cistern(50)\
            .take_car()

        self.cars.append(take_c)
        return take_c


if __name__ == "__main__":
    a = CarDirector()

    ec = a.take_electronic_car()
    print(ec)

    cc = a.take_custom_car("Lada", "Gas engine")
    print(cc)
