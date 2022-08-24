import abc


class Locker:

    def __init__(self):
        self._state = Lock(self)
        self.password = ""

    def change_state(self, state):
        self._state = state

    def open(self):
        self._state.unlock()

    def close(self):
        self._state.lock()

    def input_password(self):
        self.password = input("Enter password: ")


class State(abc.ABC):

    def __init__(self, locker):
        self.locker = locker

    @abc.abstractmethod
    def lock(self):
        pass

    @abc.abstractmethod
    def unlock(self):
        pass


class Lock(State):

    def lock(self):
        print("Locker is already locked")

    def unlock(self):
        if self.locker.password == "1234":
            print("Locker unlocked")
            self.locker.change_state(Unlock(self.locker))
        else:
            print("Wrong password")
            self.locker.password = ""


class Unlock(State):

    def lock(self):
        self.locker.password = ""
        print("Locker locked")
        self.locker.change_state(Lock(self.locker))

    def unlock(self):
        print("Locker is already unlocked")


if __name__ == '__main__':
    locker = Locker()

    locker.open()
    locker.close()
    locker.input_password()
    locker.open()
    locker.open()

