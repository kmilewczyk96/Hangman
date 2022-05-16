import sys
import pygame
from .gui import GUI


class GUIMenu(GUI):
    def __init__(self, title: str, menu_items: list):
        super().__init__()
        self.title = title.upper()
        self.menu_items = menu_items

    def run_menu(self):
        index = 0

        # Menu items positioning:
        h_start = self.height // 2 - \
            (self.size_h1 * len(self.menu_items) + self.size_h2 * (len(self.menu_items) - 2)) // 2
        gap = self.size_h1 + self.size_h2

        # Menu title:
        header = self.create_header(self.title)

        # Controls:
        footer = self.create_footer("Use UP/DOWN ARROW to navigate, press ENTER to select.")

        run = True
        while run:
            self.refresh()

            # Display menu title:
            self.WIN.blit(*header)

            # Display menu
            for pos, item in enumerate(self.menu_items):
                if index == pos:
                    menu_item = self.h1.render(f'- {item["name"].upper()} -', True, self.color_white)
                else:
                    menu_item = self.h1.render(item["name"].upper(), True, self.color_gray)

                menu_item_rect = menu_item.get_rect()
                menu_item_rect.midtop = (self.width // 2, h_start + pos * gap)
                self.WIN.blit(menu_item, menu_item_rect)

            # Display controls:
            self.WIN.blit(*footer)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and index < len(self.menu_items) - 1:
                        index += 1
                    if event.key == pygame.K_UP and index > 0:
                        index -= 1
                    if event.key == pygame.K_RETURN:
                        return index

            pygame.display.update()

