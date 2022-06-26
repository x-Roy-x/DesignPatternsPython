import abc
from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):

    @abc.abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):

    def consume(self):
        print("This tea is delicious")


class Coffee(HotDrink):

    def consume(self):
        print("This coffee is delicious")


class HotDrinkFactory(ABC):

    @abc.abstractmethod
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):

    @staticmethod
    def prepare(amount):
        print(f"Put in tea bag, boil water, pour {amount} ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):

    @staticmethod
    def prepare(amount):
        print(f"Put in coffee beans, boil water, pour {amount} ml, enjoy!")
        return Coffee()


def make_drink(type):
    drink = None

    if type == "tea":
        drink = TeaFactory.prepare(200)

    elif type == "coffee":
        drink = CoffeeFactory.prepare(100)

    return drink


if __name__ == "__main__":
    drink = make_drink("tea")
    drink.consume()
