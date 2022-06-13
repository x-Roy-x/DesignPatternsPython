
from SOLID.OpenClosedPrinciple.open_closed import Color, Size
from SOLID.OpenClosedPrinciple.open_closed import Product
from SOLID.OpenClosedPrinciple.open_closed import ProductFilter, BetterProductFilter
from SOLID.OpenClosedPrinciple.open_closed import ColorSpecification, SizeSpecification, AndSpecification

if __name__ == "__main__":
    products = list()
    products.append(Product("apple", Color.RED, Size.MEDIUM))
    products.append(Product("pear", Color.GREEN, Size.LARGE))
    products.append(Product("strawberry", Color.RED, Size.SMALL))

    pf = ProductFilter()

    green_products = pf.get_by_color(products, Color.GREEN)
    for green_product in green_products:
        print(f"{green_product.name} is {Color.GREEN} \n")

    color = ColorSpecification(Color.RED)
    red_products = BetterProductFilter.filter(products, color)
    for red_product in red_products:
        print(f"{red_product.name} is {Color.RED} \n")

    # and_specification = AndSpecification([ColorSpecification(Color.RED), SizeSpecification(Size.SMALL)])
    and_specification = ColorSpecification(Color.RED) & SizeSpecification(Size.SMALL)
    red_products = BetterProductFilter.filter(products, and_specification)
    for red_product in red_products:
        print(f"{red_product.name} is {Color.RED} \n")






