class ChanceError(ValueError):
    pass


class Chance:
    def __init__(self, level_chances):
        self.base_chances = level_chances
        self.chances = self.base_chances

    def decrease_chances(self):
        self.chances -= 1
        if self.chances == 0:
            raise ChanceError

    def reset_chances(self):
        self.chances = self.base_chances

