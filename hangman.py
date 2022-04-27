class Hangman:
    def __init__(self, word_engine, score_, chance_):
        self.word_engine = word_engine
        self.score = score_
        self.chances = chance_
        self.word_to_guess = self.word_engine.get_random_word()
        self.hidden_word = ['_' if letter not in ('-', ' ') else letter for letter in self.word_to_guess]
        self.left_to_guess = len(self.word_to_guess)
        self.used_letters = []
        self.missed = []
        self.ascii_alphabet = [i for i in range(97, 123)]

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
            self.chances.decrease_chances()

        if self.left_to_guess == 0:
            self.score.increase_score()
            # self.win()

    def win(self):
        print(f'{self.word_to_guess}: {self.word_engine.get_definition(self.word_to_guess)}')
        # return f'{self.word_to_guess}: {self.word_engine.get_definition(self.word_to_guess)}'
