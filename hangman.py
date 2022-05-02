from chance import ChanceError


class Hangman:
    def __init__(self, word, score, chance):
        self.word = word
        self.score = score
        self.chances = chance

        self.word_to_guess = ...
        self.hidden_word = ...
        self.aesthetic_underscore = ...
        self.left_to_guess = ...
        self.used_letters = ...
        self.missed = ...

    def start_game(self):
        self.score.reset_score()
        self.get_next_word()

    def get_next_word(self):
        self.chances.reset_chances()
        self.word_to_guess = self.word.get_random_word()
        self.hidden_word = ['_' if letter not in ('-', ' ') else letter for letter in self.word_to_guess]
        self.aesthetic_underscore = self.hidden_word.copy()
        self.left_to_guess = len(self.word_to_guess)
        self.used_letters = []
        self.missed = []

    def check(self, guess):
        self.used_letters.append(guess)
        occurrences = 0
        for pos, letter in enumerate(self.word_to_guess):
            if letter == guess:
                self.hidden_word[pos] = letter
                occurrences += 1
                self.left_to_guess -= 1

        if occurrences == 0:
            self.missed.append(guess)
            try:
                self.chances.decrease_chances()
            except ChanceError:
                self.game_over()
                return True

        if self.left_to_guess == 0:
            self.score.increase_score()
            self.get_next_word()

    def game_over(self):
        pass
