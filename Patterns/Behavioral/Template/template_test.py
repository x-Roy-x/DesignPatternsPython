import abc


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(abc.ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        winner_index = -1

        creature1 = self.creatures[c1_index]
        creature2 = self.creatures[c2_index]

        self.hit(creature1, creature2)
        self.hit(creature2, creature1)

        if not((creature1.health <= 0 and creature2.health <= 0) or (creature1.health > 0 and creature2.health > 0)):
            if creature1.health <= 0:
                winner_index = c2_index
            else:
                winner_index = c1_index

        return winner_index

    @abc.abstractmethod
    def hit(self, attacker, defender):
        pass


class TemporaryDamageCardGame(CardGame):

    def hit(self, attacker, defender):
        start_health = defender.health
        defender.health -= attacker.attack

        if defender.health > 0:
            defender.health = start_health


class PermanentDamageCardGame(CardGame):

    def hit(self, attacker, defender):
        defender.health -= attacker.attack


if __name__ == '__main__':
    c1 = Creature(1, 2)
    c2 = Creature(1, 3)
    game = PermanentDamageCardGame([c1, c2])

    index = game.combat(0, 1)
    index = game.combat(0, 1)
