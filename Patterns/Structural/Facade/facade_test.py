from random import randint


class Generator:

    @staticmethod
    def generate(count):
        return [randint(1, 9) for x in range(count)]


class Splitter:

    @staticmethod
    def split(array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:

    @staticmethod
    def verify(arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:

    def __init__(self):
        self.generator = Generator()
        self.splitter = Splitter()
        self.verifier = Verifier

    def generate(self, size):
        is_the_same = False

        while not is_the_same:
            square = []

            for x in range(size):
                square.append(self.generator.generate(size))

            splitted_list = self.splitter.split(square)
            if self.verifier.verify(splitted_list):
                is_the_same = True

        return square


if __name__ == '__main__':
    magic_square_list = MagicSquareGenerator().generate(2)
    print(magic_square_list)
