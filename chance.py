class Chance:
    def __init__(self, level_chances):
        self.chances = level_chances

    def decrease_chances(self):
        self.chances -= 1
