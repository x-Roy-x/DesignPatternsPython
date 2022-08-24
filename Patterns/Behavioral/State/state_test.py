import abc
import unittest


class CombinationLock:
    def __init__(self, combination):
        self.status = None
        self.combination = combination
        self.current_combination = []
        self._state = Lock(self)
        self._state.lock()

    def reset(self):
        self._state.lock()

    def enter_digit(self, digit):
        self.current_combination.append(digit)
        self._state.unlock()


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
        self.locker.status = "LOCKED"
        self.locker.current_combination = []

    def unlock(self):
        right_combination = "".join(map(str, self.locker.combination))
        current_combination = "".join(map(str, self.locker.current_combination))

        if current_combination == right_combination:
            self.locker.status = "OPEN"
        elif right_combination.startswith(current_combination):
            self.locker.status = current_combination
        else:
            self.locker.status = "ERROR"


class Unlock(State):

    def lock(self):
        self.locker.status = "LOCKED"
        self.locker.current_combination = []

    def unlock(self):
        print("Locker is already unlocked")


class FirstTestSuite(unittest.TestCase):
    def test_success(self):
        cl = CombinationLock([1, 2, 3, 4, 5])
        self.assertEqual('LOCKED', cl.status)
        cl.enter_digit(1)
        self.assertEqual('1', cl.status)
        cl.enter_digit(2)
        self.assertEqual('12', cl.status)
        cl.enter_digit(3)
        self.assertEqual('123', cl.status)
        cl.enter_digit(4)
        self.assertEqual('1234', cl.status)
        cl.enter_digit(5)
        self.assertEqual('OPEN', cl.status)
