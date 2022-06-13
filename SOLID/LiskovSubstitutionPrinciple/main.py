
from SOLID.LiskovSubstitutionPrinciple.liskov_substitution import Rectangle
from SOLID.LiskovSubstitutionPrinciple.liskov_substitution import Square


def use_it(rc):
    height = 10
    w = rc.width
    rc.height = height
    expected = int(w * height)
    print(f"Expected ana area of {expected}, got {rc.area}")


if __name__ == "__main__":
    rc = Rectangle(2, 3)
    use_it(rc)

    sq = Square(5)
    use_it(sq)
