from __future__ import annotations
import abc


class EventManager(abc.ABC):

    @abc.abstractmethod
    def attach(self, listener: Listener):
        pass

    @abc.abstractmethod
    def detach(self, listener: Listener):
        pass

    @abc.abstractmethod
    def notify(self, data):
        pass


class Listener(abc.ABC):

    @abc.abstractmethod
    def receive_message(self, data):
        pass


class Shop:

    def __init__(self, shop_event_manager):
        self.shop_event_manager = shop_event_manager
        self.popular_goods = ["clothes", "food"]

    def notify(self):
        self.shop_event_manager.notify(self.popular_goods)


class ShopEventManager(EventManager):

    _buyers = []

    def attach(self, buyer: Listener):
        self._buyers.append(buyer)

    def detach(self, buyer: Listener):
        self._buyers.remove(buyer)

    def notify(self, data):
        for buyer in self._buyers:
            buyer.receive_message(data)


class Buyer(Listener):

    def __init__(self, name, favorite_things):
        self.name = name
        self._favorite_things = favorite_things
        self.messages = []

    def receive_message(self, data):
        for favorite_thing in self._favorite_things:
            if favorite_thing in data:
                print(f"Hi {self.name}.Today you can buy {favorite_thing} with big discount")


if __name__ == '__main__':
    shop_manager = ShopEventManager()
    shop = Shop(shop_manager)

    shop_manager.attach(Buyer("Roi", ["food"]))
    shop_manager.attach(Buyer("John", ["car"]))
    shop_manager.attach(Buyer("Li", ["clothes"]))

    shop.notify()

