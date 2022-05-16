from level import *


class Level:
    def __init__(self):
        self.levels = (Easy(), Normal(), Hard())
        self.chances = None
        self.multiplier = None

    def pick_level(self, index=1):
        self.chances = self.levels[index].chances
        self.multiplier = self.levels[index].multiplier

    def get_names(self):
        return [str(level) for level in self.levels]

