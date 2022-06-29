class CEO:

    __shred_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        self.__dict__ = self.__shred_state

    def __str__(self):
        return f"{self.name} is {self.age} years old"


class Monostate:

    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):

    def __init__(self):
        self.name = ""
        self.money_managed = 0

    def __str__(self):
        return f"{self.name} manages {self.money_managed}"


if __name__ == "__main__":
    coe1 = CEO()
    coe2 = CEO()

    print(coe1)
    print(coe2)
    coe2.name = "John"
    print(coe1)

    cfo1 = CFO()
    cfo2 = CFO()

    print(cfo1)
    print(cfo2)

    cfo1.name = "Steve"

    print(cfo1)
    print(cfo2)

