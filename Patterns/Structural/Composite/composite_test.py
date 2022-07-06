

class GeneralValue:

    def __init__(self, value):
        self._value = value

    def append(self, value):
        pass

    def remove(self, value):
        pass

    @property
    def sum(self):
        pass


class SingleValue(GeneralValue):

    @property
    def sum(self):
        return self._value


class ManyValues(GeneralValue):

    def __init__(self, value=0):
        self.values = []
        super().__init__(value)

    def append(self, value):
        self.values.append(value)

    def remove(self, value):
        self.values.remove(value)

    @property
    def sum(self):
        result = 0

        for value in self.values:
            if isinstance(value, int):
                result += value

            elif isinstance(value, GeneralValue):
                result += value.sum

        return result


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_values = ManyValues()

    other_values.append(22)
    other_values.append(33)

    all_values = ManyValues()

    all_values.append(single_value)
    all_values.append(other_values)

    print(all_values.sum)

