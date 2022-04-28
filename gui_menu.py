import pygame
from gui import GUI


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
        menu_title = self.h1.render(self.title, True, self.color_white)
        menu_title_rect = menu_title.get_rect()
        menu_title_rect.midtop = (self.width // 2, 0 + self.size_par)

        # Controls:
        controls_footer = self.span.render(
            "Use UP/DOWN ARROW to navigate, press ENTER to select.", True, self.color_gray
        )
        controls_footer_rect = controls_footer.get_rect()
        controls_footer_rect.midbottom = (self.width // 2, self.height)

        run = True
        while run:
            self.clock.tick(self.fps)
            self.WIN.blit(source=self.background, dest=(0, 0))

            # Display menu title:
            self.WIN.blit(menu_title, menu_title_rect)

            # Display menu
            for pos, item in enumerate(self.menu_items):
                menu_item = self.h1.render(
                    item['name'].upper(), True, self.color_white if index == pos else self.color_gray
                )
                menu_item_rect = menu_item.get_rect()
                menu_item_rect.midtop = (self.width // 2, h_start + pos * gap)
                self.WIN.blit(menu_item, menu_item_rect)

            # Display controls:
            self.WIN.blit(controls_footer, controls_footer_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN and index < len(self.menu_items) - 1:
                        index += 1
                    if event.key == pygame.K_UP and index > 0:
                        index -= 1
                    if event.key == pygame.K_RETURN:
                        self.menu_items[index]['action']()
                        index = 0

            try:
                pygame.display.update()
            except pygame.error:
                run = False
