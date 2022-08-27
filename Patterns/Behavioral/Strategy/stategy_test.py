from abc import ABC


class DiscriminantStrategy(ABC):
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result_under_root = complex(b * b - 4 * a * c, 0)
        x1 = ((-b) + pow(result_under_root, 0.5)) / (2 * a)
        x2 = ((-b) - pow(result_under_root, 0.5)) / (2 * a)
        return x1, x2


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        result_under_root = b * b - 4 * a * c
        result_under_root = result_under_root if result_under_root >= 0 else float('nan')
        result_under_root = complex(result_under_root, 0)
        x1 = ((-b) + pow(result_under_root, 0.5)) / (2 * a)
        x2 = ((-b) - pow(result_under_root, 0.5)) / (2 * a)
        return x1, x2


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy

    def solve(self, a, b, c):
        return self.strategy.calculate_discriminant(a, b, c)


if __name__ == '__main__':
    strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 10, 16)
    print(results)
