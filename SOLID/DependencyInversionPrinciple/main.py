
from SOLID.DependencyInversionPrinciple.dependency_inversion import Person
from SOLID.DependencyInversionPrinciple.dependency_inversion import Relationships
from SOLID.DependencyInversionPrinciple.dependency_inversion import Research

if __name__ == "__main__":
    parent = Person("John")
    child1 = Person("Bill")
    child2 = Person("Matt")

    relationships = Relationships()
    relation1 = relationships.add_parent_and_child(parent, child1)
    relation2 = relationships.add_parent_and_child(parent, child2)

    Research(relationships, "John")
