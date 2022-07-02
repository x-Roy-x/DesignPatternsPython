import abc
from enum import Enum


class Action(Enum):
    ON = 0
    OFF = 1

class Controller:
    
    def __init__(self, device):
        self.device = device

    def on(self):
        pass

    def off(self):
        pass
    
class Phone(Controller):

    def __init__(self, device, password):
        super().__init__(device)
        self.password = password

    def on(self):
        print(f"Connect to {self.device.NAME} using phone")
        self.device.power_on(self.password)

    def off(self):
        print(f"Connect to {self.device.NAME} using phone")
        self.device.power_off(self.password)


class Remote(Controller):

    PASSWORD = "123"

    def __init__(self, device):
        super().__init__(device)

    def on(self):
        print(f"Connect to {self.device.NAME} using remote")
        self.device.power_on(self.PASSWORD)

    def off(self):
        print(f"Connect to {self.device.NAME} using remote")
        self.device.power_off(self.PASSWORD)


class Device(abc.ABC):

    NAME = ""

    @abc.abstractmethod
    def power_on(self, password):
        pass

    @abc.abstractmethod
    def power_off(self, password):
        pass


class TV(Device):
    NAME = "TV"
    PASSWORD = "123"

    def power_on(self, password):
        if self.PASSWORD == password:
            print("Power on action")

    def power_off(self, password):
        if self.PASSWORD == password:
            print("Power off action")


class Light(Device):
    NAME = "Light"
    PASSWORD = "123"

    def power_on(self, password):
        if self.PASSWORD == password:
            print("Power on action")

    def power_off(self, password):
        if self.PASSWORD == password:
            print("Power off action")


if __name__ == '__main__':
    light = Light()
    tv = TV()

    phone = Phone(light, "123")
    phone.off()

    remote = Remote(tv)
    remote.on()

