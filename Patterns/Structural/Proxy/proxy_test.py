import abc


class PersonProxyInterface(abc.ABC):

    @abc.abstractmethod
    def drink(self):
        pass

    @abc.abstractmethod
    def drive(self):
        pass

    @abc.abstractmethod
    def drink_and_drive(self):
        pass


class Person(PersonProxyInterface):

    def __init__(self, age):
        self.age = age

    def drink(self):
        return 'drinking'

    def drive(self):
        return 'driving'

    def drink_and_drive(self):
        return 'driving while drunk'


class ResponsiblePerson(PersonProxyInterface):

    def __init__(self, age):
        self.person = Person(age)

    def drink(self):
        result = ""
        if self.person.age >= 18:
            result = self.person.drink()
        else:
            result = "too young"

        return result

    def drive(self):
        result = ""
        if self.person.age >= 16:
            result = self.person.drive()
        else:
            result = "too young"

        return result

    def drink_and_drive(self):
        return "dead"


def client_call(person):
    p_drive = person.drive()
    print(p_drive)
    p_drink = person.drink()
    print(p_drink)
    p_drive_drink = person.drink_and_drive()
    print(p_drive_drink)


if __name__ == '__main__':
    #person = Person(18)
    responsible_person = ResponsiblePerson(15)
    client_call(responsible_person)


