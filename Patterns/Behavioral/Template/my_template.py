import abc


class Order:
    
    def __init__(self, name, age, order):
        self.name = name
        self.age = age
        self.order = order

    def __str__(self):
        return f"{self.name} do order: {self.order}"
    

class ParseFile(abc.ABC):

    def __init__(self, file_path):
        self.file_path = file_path

    @abc.abstractmethod
    def get_data(self):
        pass

    @abc.abstractmethod
    def create_object(self, data):
        pass

    def get_filtered_data(self, data):
        return data

    def parse(self):
        data = self.get_data()
        object_data = self.create_object(data)
        return self.get_filtered_data(object_data)


class ParseCsv(ParseFile):

    def get_data(self):
        return {"name": "Roi", "age": 22, "order": "fish"}

    def create_object(self, data):
        return Order(**data)

    def get_filtered_data(self, data):
        filtered_data = None

        if data.age > 18:
            filtered_data = data

        return filtered_data


class ParseTxt(ParseFile):

    def get_data(self):
        return "name: Roi, age: 22, order: meat"

    def create_object(self, data):
        new_data = {}
        key_values = data.split(", ")
        for key_value in key_values:
            key, value = key_value.split(": ")
            new_data[key] = value

        return Order(**new_data)

    def get_filtered_data(self, data):
        filtered_data = None

        if int(data.age) > 18:
            filtered_data = data

        return filtered_data


if __name__ == '__main__':
    data = ParseCsv("").parse()
    print(data)

    data = ParseTxt("").parse()
    print(data)




