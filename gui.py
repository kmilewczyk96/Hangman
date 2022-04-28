import pygame


class GUI:
    def __init__(self, width=1920, fullscreen=1):
        pygame.init()
        # Display and clock initialization:
        pygame.display.set_caption("H A N _ _ A N")
        self.width = width
        self.height = int(width * 0.5625)
        self.WIN = pygame.display.set_mode(
            size=(self.width, self.height),
            flags=pygame.FULLSCREEN if fullscreen else False
        )
        self.fps = 30
        self.clock = pygame.time.Clock()
        # Styles:
        self.background = pygame.image.load("resources/chalkboard.jpg").convert()
        self.color_white = (227, 227, 227)
        self.color_gray = (180, 180, 180)
        # Font sizes:
        self.size_h0 = width // 15
        self.size_h1 = width // 20
        self.size_h2 = width // 25
        self.size_par = width // 40
        self.size_span = width // 60
        # Font objects init:
        self.h0 = pygame.font.SysFont("monospace", self.size_h0)
        self.h1 = pygame.font.SysFont("monospace", self.size_h1)
        self.h2 = pygame.font.SysFont("monospace", self.size_h2)
        self.par = pygame.font.SysFont("monospace", self.size_par)
        self.span = pygame.font.SysFont("monospace", self.size_span)
