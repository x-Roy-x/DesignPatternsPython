class CarOwner:

    def __init__(self, owner, plates):
        self.owner = owner
        self.plates = plates

    def __eq__(self, other):
        return self.owner == other.owner and self.plates == other.plates


class CarOwnerFlyweight:
    car_owners = []

    def get_car_owner(self, owner, plates):
        required_car_owner = None
        new_car_owner = CarOwner(owner, plates)

        for car_owner in self.car_owners:
            if car_owner == new_car_owner:
                required_car_owner = car_owner
                break

        else:
            self.car_owners.append(new_car_owner)
            required_car_owner = new_car_owner

        return required_car_owner


class CarType:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.color == other.color


class CarTypeFlyweight:
    car_types = []

    def get_car_type(self, brand, model, color):
        required_car_type = None
        new_car_type = CarType(brand, model, color)

        for car_type in self.car_types:
            if car_type == new_car_type:
                required_car_type = car_type
                break

        else:
            self.car_types.append(new_car_type)
            required_car_type = new_car_type

        return required_car_type


class Car:

    def __init__(self, car_owner, car_type):
        self.car_owner = car_owner
        self.car_type = car_type

    def __eq__(self, other):
        return self.car_owner == other.car_owner and self.car_type == other.car_type


class CarFlyweight:
    cars = []

    def get_car(self, car_owner, car_type):
        required_car = None
        new_car = Car(car_owner, car_type)

        for car in self.cars:
            if car == new_car:
                required_car = car_type
                break
        else:
            self.cars.append(new_car)
            required_car = new_car

        return required_car

    def find_cars_by_type(self, car_type):
        required_cars = []

        for car in self.cars:
            if car_type == car.car_type:
                required_cars.append(car)

        return required_cars

    def find_cars_by_owner(self, car_owner):
        required_cars = []

        for car in self.cars:
            if car_owner == car.car_owner:
                required_cars.append(car)

        return required_cars


class CarAssistantFacade:

    def print_car_information(self, car):
        print(
            f"Owner: {car.car_owner.owner} with {car.car_owner.plates} plates.\n"\
            f"Car {car.car_type.brand} {car.car_type.model} with {car.car_type.color} color"
        )

    def add_car(self, brand, model, color, owner, plates):
        car_type = CarTypeFlyweight().get_car_type(brand, model, color)
        car_owner = CarOwnerFlyweight().get_car_owner(owner, plates)
        car = CarFlyweight().get_car(car_owner, car_type)
        self.print_car_information(car)

    def find_car_by_type(self, brand, model, color):
        car_type = CarTypeFlyweight().get_car_type(brand, model, color)
        cars = CarFlyweight().find_cars_by_type(car_type)

        for car in cars:
            self.print_car_information(car)

    def find_car_by_owner(self, owner, plates):
        car_owner = CarOwnerFlyweight().get_car_owner(owner, plates)
        cars = CarFlyweight().find_cars_by_owner(car_owner)

        for car in cars:
            self.print_car_information(car)


if __name__ == '__main__':

    CarAssistantFacade().add_car("BMW", "M5", "red", "James Doe", "CL234IR")
    CarAssistantFacade().add_car("BMW", "X1", "red", "James Doe", "CL234IR")
    CarAssistantFacade().add_car("BMW", "M5", "red", "Vitalii Roi ", "BC2341")
    CarAssistantFacade().add_car("BMW", "X1", "red", "Oleh Kozak", "BC3411")

    print("Find car ", "BMW", "X1", "red")
    CarAssistantFacade().find_car_by_type("BMW", "X1", "red")
