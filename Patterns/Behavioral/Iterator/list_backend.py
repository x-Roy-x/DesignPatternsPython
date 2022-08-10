

class Creature:

    _STRENGTH = 0
    _AGILITY = 1
    _INTELLIGENCE = 2

    def __init__(self):
        self.stats = [10, 10, 10]

    @property
    def strength(self):
        return self.stats[self._STRENGTH]

    @strength.setter
    def strength(self, value):
        self.stats[self._STRENGTH] = value

    @property
    def agility(self):
        return self.stats[self._AGILITY]

    @agility.setter
    def agility(self, value):
        self.stats[self._AGILITY] = value

    @property
    def intelligence(self):
        return self.stats[self._INTELLIGENCE]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[self._INTELLIGENCE] = value

    @property
    def stats_sum(self):
        return sum(self.stats)

    @property
    def max_stat(self):
        return max(self.stats)

    @property
    def average_stat(self):
        return self.stats_sum / len(self.stats)
