
class DoubleExpression:

    def __init__(self, value):
        self.value = value


class AdditionExpression:

    def __init__(self, left, right):
        self.left = left
        self.right = right


class ExpressionPrinter:

    @staticmethod
    def print(expression, buffer):
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))

        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")


if __name__ == '__main__':
    # 1 + (2 + 3)

    result = AdditionExpression(
        DoubleExpression(1),
        AdditionExpression(
            DoubleExpression(2),
            DoubleExpression(3)
        )
    )

    buffer = []

    ExpressionPrinter.print(result, buffer)

    print("".join(buffer))
