import abc
import enum


class Person:

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place


class Strategy(abc.ABC):

    def __init__(self, person):
        self.person = person

    @abc.abstractmethod
    def get_document(self):
        pass


class DriverLicense(Strategy):

    def get_document(self):
        if self.person.age > 18:
            print(f"{self.person.name} can drive")


class Passport(Strategy):

    def get_document(self):
        if self.person.age > 16 and self.person.place:
            print(f"{self.person.name}, {self.person.age} age old lives in {self.person.place}")


class DocumentType(enum.Enum):

    DRIVER_LICENSE = enum.auto()
    PASSPORT = enum.auto()


class DiaDocument:

    def __init__(self, person):
        self.person = person

    def get_document(self, document_type):
        document = None
        if document_type == DocumentType.DRIVER_LICENSE:
            document = DriverLicense(self.person)
        elif document == DocumentType.PASSPORT:
            document = Passport(self.person)

        document.get_document()


if __name__ == '__main__':
    person1 = Person("Roi", 22, "Lviv")
    DiaDocument(person1).get_document(DocumentType.DRIVER_LICENSE)

