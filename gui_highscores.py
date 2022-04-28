import json
import os
import pygame
from gui import GUI


class GUIHighscores(GUI):
    def __init__(self, highscores: list):
        super().__init__()
        self.highscores = highscores

    def display_highscores(self):
        # Highscore list items positioning:
        h_start = self.height // 2 - \
                  (self.size_h1 * len(self.highscores) + self.size_par * (len(self.highscores) - 2)) // 2
        gap = self.size_h1 + self.size_par

        # Highscores header:
        header = self.h1.render('- HI-SCORES -', True, self.color_white)
        header_rect = header.get_rect()
        header_rect.midtop = (self.width // 2, 0 + self.size_par)

        # Highscore list:
        records = []
        for pos, player in enumerate(self.highscores):
            menu_item = self.h1.render(
                f'{pos + 1}.{player["name"].upper()} {str(player["score"]).rjust(9)}', True, self.color_white
            )
            menu_item_rect = menu_item.get_rect()
            menu_item_rect.midtop = (self.width // 2, h_start + pos * gap)
            records.append((menu_item, menu_item_rect))

        # Controls:
        controls_footer = self.span.render(
            "Press SPACE/ENTER or ESCAPE to continue.", True, self.color_gray
        )
        controls_footer_rect = controls_footer.get_rect()
        controls_footer_rect.midbottom = (self.width // 2, self.height)

        run = True
        while run:
            self.clock.tick(self.fps)
            self.WIN.blit(source=self.background, dest=(0, 0))

            # Display highscores header:
            self.WIN.blit(header, header_rect)

            # Display highscores:
            for record in records:
                self.WIN.blit(*record)

            # Display controls:
            self.WIN.blit(controls_footer, controls_footer_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                        run = False

            pygame.display.update()

    def enter_name(self):
        name_letters = []

        # Request header:
        header = self.h1.render('- ENTER YOUR NAME -', True, self.color_white)
        header_rect = header.get_rect()
        header_rect.midtop = (self.width // 2, 0 + self.size_par)

        # Input field:
        underscore = self.h1.render('_ _ _', True, self.color_white)
        underscore_rect = underscore.get_rect()
        underscore_rect.midbottom = (self.width // 2, self.height // 2)

        # Controls:
        controls_footer = self.span.render(
            "Press BACKSPACE to erase last letter, press ENTER to proceed.", True, self.color_gray
        )
        controls_footer_rect = controls_footer.get_rect()
        controls_footer_rect.midbottom = (self.width // 2, self.height)

        run = True
        while run:
            self.clock.tick(self.fps)
            self.WIN.blit(source=self.background, dest=(0, 0))

            # Display request header:
            self.WIN.blit(header, header_rect)

            # Display input field:
            name = self.h1.render(' '.join(name_letters).upper(), True, self.color_white)
            self.WIN.blit(name, underscore_rect)
            self.WIN.blit(underscore, underscore_rect)

            # Display controls:
            self.WIN.blit(controls_footer, controls_footer_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name_letters) == 3:
                        run = False
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    if event.key in range(97, 123) and len(name_letters) < 3:
                        letter = pygame.key.name(event.key).upper()
                        name_letters.append(letter)
                    if event.key == pygame.K_BACKSPACE and name_letters:
                        name_letters.pop()

            pygame.display.update()

        self.display_highscores()
