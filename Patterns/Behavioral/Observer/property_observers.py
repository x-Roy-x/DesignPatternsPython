class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PrototypeObservable:

    def __init__(self):
        self.property_changed = Event()


class Person(PrototypeObservable):

    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if self._age != age:
            self._age = age
            self.property_changed("age", age)


class TrafficAuthority:

    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_changed)

    def person_changed(self, attribute_name, attribute_value):
        if attribute_name == "age":
            if attribute_value < 16:
                print("Sorry, you still can`t drive")
            else:
                print("Ok you can drive now")
                self.person.property_changed.remove(self.person_changed)


if __name__ == '__main__':
    person = Person()
    ta = TrafficAuthority(person)

    for age in range(14, 18):
        print(f"Setting age to {age}")
        person.age = age

