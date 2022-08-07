from enum import Enum, auto


class Type(Enum):
    INTEGER = auto()
    PLUS = auto()
    MINUS = auto()
    VARIABLE = auto()
    INVALID = auto()


class SeparateElement:

    def __init__(self, element_type, text):
        self.type = element_type
        self.text = text

    def __str__(self):
        return f"'{self.text}'"


class ExpressionProcessor:
    def __init__(self):
        self.variables = {"x": 1}

    @staticmethod
    def get_separate_elements(expression):
        separate_elements = []

        position = 0
        expression_length = len(expression)

        while position < expression_length:
            expression_element = expression[position]

            if expression_element == "+":
                separate_elements.append(SeparateElement(Type.PLUS, "+"))
            elif expression_element == "-":
                separate_elements.append(SeparateElement(Type.MINUS, "-"))
            elif expression_element.isalpha():
                separate_elements.append(SeparateElement(Type.VARIABLE, expression_element))

            elif expression_element.isdigit():
                number_elements = [expression_element]

                for digit_position in range(position + 1, expression_length):
                    digit_element = expression[digit_position]

                    if digit_element.isdigit():
                        number_elements.append(digit_element)
                        position += 1
                    else:
                        number = "".join(number_elements)
                        separate_elements.append(SeparateElement(Type.INTEGER, number))
                        break

            position += 1

        return separate_elements

    def get_expression(self, separate_elements):
        result = 0
        separate_elements_length = len(separate_elements)

        for position in range(0, separate_elements_length, 2):
            separate_element = separate_elements[position]

            if separate_element.type == Type.INTEGER:
                if position == 0:
                    result = int(separate_element.text)
                else:
                    action = separate_elements[position - 1]

                    if action.type == Type.PLUS:
                        result += int(separate_element.text)
                    elif action.type == Type.MINUS:
                        result -= int(separate_element.text)

            elif separate_element.type == Type.INVALID:
                return 0
            elif separate_element.type == Type.VARIABLE:
                variable_value = self.variables.get(separate_element.text, None)

                if variable_value is not None:
                    action = separate_elements[position - 1]

                    if action.type == Type.PLUS:
                        result += int(variable_value)
                    elif action.type == Type.MINUS:
                        result -= int(variable_value)

                else:
                    return 0

        return result

    def calculate(self, expression):
        separate_elements = self.get_separate_elements(expression)
        print(" ".join(map(str, separate_elements)))
        parsed_expression_value = self.get_expression(separate_elements)
        return parsed_expression_value


if __name__ == '__main__':
    result = ExpressionProcessor().calculate("10-2-x")
    print(result)
