import abc
from enum import Enum


class Event(list):

    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENCE = 2


class Query:

    def __init__(self, creature_name, what_to_query, default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value


class Game:

    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class CreatureModifier(abc.ABC):

    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass


class DoubleAttackModifier(CreatureModifier):

    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class Creature:

    def __init__(self, game, name, attack, defence):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defence = defence

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)

        return q.value

    @property
    def defence(self):
        q = Query(self.name, WhatToQuery.DEFENCE, self.initial_defence)
        self.game.perform_query(self, q)

        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defence})"


if __name__ == '__main__':
    game = Game()

    goblin = Creature(game, "Strong goblin", 2, 2)
    print(goblin)

    dam = DoubleAttackModifier(game, goblin)

    print(goblin)
