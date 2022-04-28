import pygame
from gui import GUI


class GUIGame(GUI):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.hidden = self.game.hidden_word.copy()

    def start_game(self):
        run = True
        while run:
            self.clock.tick(self.fps)
            self.WIN.blit(source=self.background, dest=(0, 0))

            # Display guessed letters while keeping underscores
            underscore = self.h1.render(' '.join(self.hidden), True, self.color_white)
            word = self.h1.render(' '.join(self.game.hidden_word).upper(), True, self.color_white)
            underscore_rect = underscore.get_rect()
            underscore_rect.midbottom = (self.width // 2, self.height // 2)

            # Display chances left:
            chance = self.par.render(f"CHANCES: {self.game.chances.chances}", True, self.color_white)
            chance_rect = chance.get_rect()
            chance_rect.topleft = (self.size_par, self.size_par)

            # Display current score and streak in top right:
            score = self.par.render(f"SCORE: {self.game.score.current_score}", True, self.color_white)
            score_rect = score.get_rect()
            score_rect.topright = (self.width - self.size_par, self.size_par)
            streak = self.par.render(f"STREAK: {self.game.score.streak}", True, self.color_white)
            streak_rect = streak.get_rect()
            streak_rect.topright = (self.width - self.size_par, 2.5 * self.size_par)

            # Display used letters:
            used = self.h2.render(' '.join(self.game.missed), True, self.color_white)
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

            # Display controls:
            controls_footer = self.span.render("Press Esc to quit game.", True, self.color_gray)
            controls_footer_rect = controls_footer.get_rect()
            controls_footer_rect.midbottom = (self.width // 2, self.height)

            self.WIN.blit(word, underscore_rect)
            self.WIN.blit(underscore, underscore_rect)
            self.WIN.blit(chance, chance_rect)
            self.WIN.blit(score, score_rect)
            self.WIN.blit(streak, streak_rect)
            self.WIN.blit(used, used_rect)
            self.WIN.blit(used_text, used_text_rect)
            self.WIN.blit(controls_footer, controls_footer_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in self.game.ascii_alphabet:
                        guess = pygame.key.name(event.key).upper()
                        if guess not in self.game.used_letters:
                            self.game.check(guess)

                    if event.key == pygame.K_ESCAPE:
                        run = False

            pygame.display.update()
