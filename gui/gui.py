import pygame


class GUI:
    def __init__(self, width=1280, fullscreen=False):
        pygame.init()
        # Display and clock initialization:
        pygame.display.set_caption("H A N _ _ A N")
        self.width = width
        self.height = int(width * 0.5625)
        self.WIN = pygame.display.set_mode(
            size=(self.width, self.height),
            flags=pygame.FULLSCREEN if fullscreen else False
        )
        self.fps = 60
        self.clock = pygame.time.Clock()
        # Styles:
        self.background = pygame.image.load("resources/chalkboard.jpg")
        self.background = pygame.transform.scale(self.background, self.WIN.get_size())
        self.background.convert()
        self.color_white = (227, 227, 227)
        self.color_gray = (170, 170, 170)
        # Font sizes:
        self.size_h1 = width // 20
        self.size_h2 = width // 25
        self.size_par = width // 40
        self.size_span = width // 60
        # Font objects init:
        self.h1 = pygame.font.Font("resources/fonts/SourceCodePro-Regular.ttf", self.size_h1)
        self.h2 = pygame.font.Font("resources/fonts/SourceCodePro-Regular.ttf", self.size_h2)
        self.par = pygame.font.Font("resources/fonts/SourceCodePro-Regular.ttf", self.size_par)
        self.span = pygame.font.Font("resources/fonts/SourceCodePro-Regular.ttf", self.size_span)

    def refresh(self):
        self.clock.tick(self.fps)
        self.WIN.blit(source=self.background, dest=(0, 0))

    def create_header(self, text):
        header = self.h1.render(text, True, self.color_white)
        header_rect = header.get_rect()
        header_rect.midtop = (self.width // 2, self.size_par)

        return header, header_rect

    def create_footer(self, text):
        footer = self.span.render(text, True, self.color_gray)
        footer_rect = footer.get_rect()
        footer_rect.midbottom = (self.width // 2, self.height)

        return footer, footer_rect
