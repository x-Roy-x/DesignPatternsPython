import abc
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:

    @abc.abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low-level

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )

        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):

        for relation in self.relations:
            if relation[0].name == name and relation[1] == Relationship.PARENT:
                yield relation[2].name


class Research:  # high level should not depend upon low level.

    #def __init__(self, relationships):
    #    relations = relationships.relations
    #
    #    for relation in relations:
    #        if relation[0].name == "John" and relation[1] == Relationship.PARENT:
    #            print(f"John has a child called {relation[2].name}")

    def __init__(self, browser, name):
        for child in browser.find_all_children_of(name):
            print(f"{name} has a child called {child}")
