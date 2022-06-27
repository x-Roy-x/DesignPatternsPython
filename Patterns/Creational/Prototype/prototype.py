import copy


class Address:
    
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Person:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


if __name__ == "__main__":
    address = Address("123 London Road", "London", "UK")
    john = Person("John", address)

    """

    print(john)

    jane = Person("Jane", address)

    jane.address.street = "123B London Road"

    print(john)
    print(jane)
    """

    jane = copy.deepcopy(john)
    jane.name = "Jane"
    jane.address.street = "123B London Road"

    print(john)
    print(jane)