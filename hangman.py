from gui.gui_game import GUIGame
from chance import ChanceError


class Hangman(GUIGame):
    def __init__(self, word, chance, score, highscores):
        super().__init__(context=self)
        self.word = word
        self.chances = chance
        self.score = score
        self.highscores = highscores

        self.word_to_guess = ...
        self.hidden_word = ...
        self.aesthetic_underscore = ...
        self.left_to_guess = ...
        self.used_letters = ...
        self.missed = ...

    def get_next_word(self):
        self.chances.reset_chances()
        self.word_to_guess = self.word.get_random_word()
        self.hidden_word = ['_' if letter not in ('-', ' ') else letter for letter in self.word_to_guess]
        self.aesthetic_underscore = self.hidden_word.copy()
        self.left_to_guess = self.hidden_word.count('_')
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
                return "GAME OVER"

        if self.left_to_guess == 0:
            self.score.increase_score()
            self.gui_show_word()
            self.get_next_word()

    def run_game(self):
        self.score.reset_score()
        self.get_next_word()

        self.gui_game()
        self.game_over()

    def game_over(self):
        self.gui_show_word()
        highscores_position = self.highscores.check_if_highscore(self.score.current_score)

        if highscores_position is not None:
            player_name = self.highscores.get_name()
            if player_name:
                self.highscores.update_highscores(
                    pos=highscores_position,
                    name=player_name,
                    score=self.score.current_score
                )

                self.highscores.gui_highscores()

