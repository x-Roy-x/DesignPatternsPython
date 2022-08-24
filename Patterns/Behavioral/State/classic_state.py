import abc


class Switch:

    def __init__(self):
        self.state = OffState()

    def on(self):
        self.state.on(self)

    def of(self):
        self.state.off(self)


class State(abc.ABC):

    def on(self, switch):
        print("Light is already on")

    def off(self, switch):
        print("Light is already off")


class OnState(State):

    def __init__(self):
        print("Light turned on")

    def off(self, switch):
        print("Turning light off ...")
        switch.state = OffState()


class OffState(State):

    def __init__(self):
        print("Light turned off")

    def on(self, switch):
        print("Turning light on ...")
        switch.state = OnState()


if __name__ == '__main__':
    switch = Switch()

    switch.on()

    switch.of()
    switch.of()


