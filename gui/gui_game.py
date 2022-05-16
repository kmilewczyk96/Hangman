import sys
import pygame
from .gui import GUI


class GUIGame(GUI):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def gui_game(self):
        # Controls:
        footer = self.create_footer("Press ESC to quit the game.")

        run = True
        while run:
            self.refresh()
            # Display guessed letters while keeping underscores
            underscore = self.h1.render(' '.join(self.context.aesthetic_underscore), True, self.color_white)
            word = self.h1.render(' '.join(self.context.hidden_word).upper(), True, self.color_white)
            underscore_rect = underscore.get_rect()
            underscore_rect.midbottom = (self.width // 2, self.height // 2)
            self.WIN.blit(word, underscore_rect)
            self.WIN.blit(underscore, underscore_rect)

            # Display chances left:
            chance = self.par.render(f"CHANCES: {self.context.chances.chances}", True, self.color_white)
            chance_rect = chance.get_rect()
            chance_rect.topleft = (self.size_par, self.size_par)
            self.WIN.blit(chance, chance_rect)

            # Display current score and streak in top right:
            score = self.par.render(f"SCORE: {self.context.score.current_score}", True, self.color_white)
            score_rect = score.get_rect()
            score_rect.topright = (self.width - self.size_par, self.size_par)
            streak = self.par.render(f"STREAK: {self.context.score.streak}", True, self.color_white)
            streak_rect = streak.get_rect()
            streak_rect.topright = (self.width - self.size_par, 2.5 * self.size_par)
            self.WIN.blit(score, score_rect)
            self.WIN.blit(streak, streak_rect)

            # Display used letters:
            used = self.h2.render(' '.join(self.context.missed), True, self.color_white)
            used_rect = used.get_rect()
            used_rect.bottomleft = (self.size_par, self.height - 2 * self.size_par)
            pygame.draw.line(
                surface=self.WIN,
                color=(227, 227, 227),
                start_pos=(0, used_rect.top - self.size_span),
                end_pos=(self.width, used_rect.top - self.size_span)
            )
            used_text = self.par.render('USED LETTERS', True, self.color_white)
            used_text_rect = used_text.get_rect()
            used_text_rect.midbottom = (self.width // 2, used_rect.top - self.size_span)
            pygame.draw.lines(
                surface=self.WIN,
                color=(227, 227, 227),
                closed=True,
                points=(
                    (used_text_rect.topleft[0] - self.size_span, used_text_rect.topleft[1]),
                    (used_text_rect.topright[0] + self.size_span, used_text_rect.topright[1]),
                    (used_text_rect.bottomright[0] + self.size_span, used_text_rect.bottomright[1]),
                    (used_text_rect.bottomleft[0] - self.size_span, used_text_rect.bottomleft[1])
                )
            )
            self.WIN.blit(used, used_rect)
            self.WIN.blit(used_text, used_text_rect)

            # Display controls:
            self.WIN.blit(*footer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in range(97, 123):
                        guess = pygame.key.name(event.key).upper()
                        if guess not in self.context.used_letters:
                            check = self.context.check(guess)
                            if check:
                                run = False

                    if event.key == pygame.K_ESCAPE:
                        run = False

            pygame.display.update()

    def gui_show_word(self):
        u2 = ['_' if letter.isalpha() else ' ' for letter in self.context.hidden_word]
        w2 = [letter.upper() if letter != '_' else ' ' for letter in self.context.hidden_word]

        # Display word to guess, shadow missing letters:
        underscore = self.h1.render(' '.join(self.context.aesthetic_underscore), True, self.color_gray)
        underscore2 = self.h1.render(' '.join(u2), True, self.color_white)
        word = self.h1.render(' '.join(self.context.word_to_guess.upper()), True, self.color_gray)
        word2 = self.h1.render(' '.join(w2), True, self.color_white)
        underscore_rect = underscore.get_rect()
        underscore_rect.midbottom = (self.width // 2, self.height // 2)

        # Controls:
        footer = self.create_footer("Press SPACE or ENTER to continue.")

        run = True
        while run:
            self.refresh()

            self.WIN.blit(underscore, underscore_rect)
            self.WIN.blit(underscore2, underscore_rect)
            self.WIN.blit(word, underscore_rect)
            self.WIN.blit(word2, underscore_rect)

            # Display controls:
            self.WIN.blit(*footer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        run = False

            pygame.display.update()
