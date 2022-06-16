class Code:
    def __init__(self):
        self.class_name = None
        self.fields = {}

    def __str(self):
        code = ""
        fields = []
        if self.fields:
            start = ' def __init__(self):{0}'
            for name, value in self.fields.items():
                field = "\n    self.{0} = {1}".format(name, value)
                fields.append(field)
            code = start.format("".join(fields))
        else:
          code = " pass"

        return code

    def __str__(self):
        return "class {0}:\n {1}".format(self.class_name, self.__str())


class CodeBuilder:
    def __init__(self, root_name):
        self.code = Code()
        self.code.class_name = root_name

    def add_field(self, type, name):
        self.code.fields[type] = name
        return self

    def __str__(self):
        return str(self.code)

if __name__ == "__main__":
    cb = CodeBuilder("Person").add_field('name', '""').add_field('age', '0')

    print(cb)

    cb = CodeBuilder("Person")

    print(cb)
