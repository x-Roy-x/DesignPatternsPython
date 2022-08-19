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
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if self._age != age:

            old_can_vote = self.can_vote

            self._age = age
            self.property_changed("age", age)

            if self.can_vote != old_can_vote:
                self.property_changed("can_vote", self.can_vote)


def person_changed(attribute_name, attribute_value):
    if attribute_name == "can_vote":
        print(f"Voting ability changed to {attribute_value}")


if __name__ == '__main__':
    person = Person()
    person.property_changed.append(person_changed)

    for age in range(14, 20):
        print(f"Setting age to {age}")
        person.age = age

