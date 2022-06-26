class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    id = 0

    def __init__(self):
        pass

    def create_person(self, name):
        p = Person(self.id, name)
        self.id += 1
        return p


if __name__ == "__main__":
    pf = PersonFactory()
    a = pf.create_person("Roi")
    b = pf.create_person("Adam")

    print(a.id)
    print(b.id)

