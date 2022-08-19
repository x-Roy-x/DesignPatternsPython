from unittest import TestCase


class Game:

    def __init__(self):
        self._rats = []

    @property
    def rat_numbers(self):
        return len(self._rats)

    def append(self, rat):
        self._rats.append(rat)

    def remove(self, rat):
        self._rats.remove(rat)


class Rat:
    def __init__(self, game):
        self.game = game
        self._attack = 1
        self.join_swarm()

    def join_swarm(self):
        self.game.append(self)

    @property
    def attack(self):
        attack = self.game.rat_numbers * self._attack
        return attack

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.game.remove(self)


if __name__ == '__main__':
    game = Game()
    rat = Rat(game)

    print(rat.attack)



