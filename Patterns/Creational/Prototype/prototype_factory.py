import copy


class Address:

    def __init__(self, suite, city, country):
        self.suite = suite
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.suite}, {self.city}, {self.country}"


class Employee:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


class EmployeeFactory:
    main_office_employee = Employee("", Address(0, '123 East Dr', "London"))
    aux_office_employee = Employee("", Address(0, '123B East Dr', "London"))

    @staticmethod
    def __new_employee(prototype, name, suite):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result

    def new_main_office_employee(self, name, suite):
        new_main_office_employee = self.__new_employee(self.main_office_employee, name, suite)
        return new_main_office_employee

    def new_aux_office_employee(self, name, suite):
        new_main_office_employee = self.__new_employee(self.aux_office_employee, name, suite)
        return  new_main_office_employee


if __name__ == "__main__":
    john = EmployeeFactory().new_main_office_employee("John", 101)
    jane = EmployeeFactory().new_aux_office_employee("Jane", 500)

    print(john)
    print(jane)
