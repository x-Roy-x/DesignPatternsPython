import random
import string


class User:
    
    def __init__(self, name):
        self.name = name


class User2:
    strings = []

    def __init__(self, full_name):
        self.names = [self.get_index(name_part) for name_part in full_name.split(" ")]

    def get_index(self, name_part):
        index = 0

        if name_part in self.strings:
            index = self.strings.index(name_part)
        else:
            self.strings.append(name_part)
            index = len(self.strings) - 1

        return index

    def __str__(self):
        return " ".join([self.strings[index] for index in self.names])


def random_string():
    chars = string.ascii_lowercase
    string_name = "".join([random.choice(chars) for x in range(8)])

    return string_name


if __name__ == '__main__':
    users = []

    first_names = [random_string() for x in range(100)]
    last_names = [random_string() for x in range(100)]

    for first_name in first_names:
        for last_name in last_names:
            users.append(User2(f"{first_name} {last_name}"))

    print(users[0])

