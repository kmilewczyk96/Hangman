import sys
import pygame
from .gui import GUI


class GUIHighscores(GUI):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def gui_highscores(self):
        # Highscore list items positioning:
        h_start = self.height // 2 - \
                  (self.size_h1 * len(self.context.highscores) + self.size_par * (len(self.context.highscores) - 2)) // 2
        gap = self.size_h1 + self.size_par

        # Highscores header:
        header = self.create_header("- HIGHSCORES -")

        # Highscore list:
        records = []
        for pos, player in enumerate(self.context.highscores):
            menu_item = self.h1.render(
                f'{pos + 1}.{player["name"].upper()} {str(player["score"]).rjust(9)}', True, self.color_white
            )
            menu_item_rect = menu_item.get_rect()
            menu_item_rect.midtop = (self.width // 2, h_start + pos * gap)
            records.append((menu_item, menu_item_rect))

        # Controls:
        footer = self.create_footer("Press SPACE/ENTER or ESCAPE to continue.")

        run = True
        while run:
            self.refresh()

            # Display highscores header:
            self.WIN.blit(*header)

            # Display highscores:
            for record in records:
                self.WIN.blit(*record)

            # Display controls:
            self.WIN.blit(*footer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE):
                        run = False

            pygame.display.update()

    def gui_enter_name(self):
        name_letters = []

        # Request header:
        header = self.create_header("- ENTER YOUR NAME -")

        # Input field:
        underscore = self.h1.render('_ _ _', True, self.color_white)
        underscore_rect = underscore.get_rect()
        underscore_rect.midbottom = (self.width // 2, self.height // 2)

        # Controls:
        footer = self.create_footer("Press BACKSPACE to erase last letter, press ENTER to proceed.")

        run = True
        while run:
            self.refresh()

            # Display request header:
            self.WIN.blit(*header)

            # Display input field:
            name = self.h1.render(' '.join(name_letters).upper(), True, self.color_white)
            self.WIN.blit(name, underscore_rect)
            self.WIN.blit(underscore, underscore_rect)

            # Display controls:
            self.WIN.blit(*footer)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name_letters) == 3:
                        return name_letters
                    if event.key == pygame.K_ESCAPE:
                        pass
                    if event.key in range(97, 123) and len(name_letters) < 3:
                        letter = pygame.key.name(event.key).upper()
                        name_letters.append(letter)
                    if event.key == pygame.K_BACKSPACE and name_letters:
                        name_letters.pop()

            pygame.display.update()
