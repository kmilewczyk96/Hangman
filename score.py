class Score:
    def __init__(self, level_multiplier):
        self.multiplier = level_multiplier
        self.current_score = 0
        self.streak = 0

    def increase_score(self):
        self.current_score += int(100 * self.multiplier)
        self.streak += 1

    def reset_score(self):
        self.current_score = 0
        self.streak = 0

