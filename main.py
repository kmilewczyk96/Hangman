import pygame

from word import Word
from score import Score
from chance import Chance
from hangman import Hangman

pygame.init()

# Display settings
width = 1280
height = int(width * 0.5625)
WIN = pygame.display.set_mode(
    size=(width, height),
    # flags=pygame.FULLSCREEN
)
pygame.display.set_caption("H A N _ _ A N")

# Time:
fps = 30
clock = pygame.time.Clock()

# Style:
background = pygame.image.load("resources/chalkboard.jpg").convert()
color_white = (227, 227, 227)
color_gray = (180, 180, 180)

# Font sizes:
size_h1 = width // 20
size_h2 = width // 25
size_par = width // 40
size_span = width // 60

# Font objects init:
h1 = pygame.font.SysFont("monospace", size_h1)
h2 = pygame.font.SysFont("monospace", size_h2)
par = pygame.font.SysFont("monospace", size_par)
span = pygame.font.SysFont("monospace", size_span)

# Hangman objects:
word_ = Word()
score_ = Score(level_multiplier=1.25)
chance_ = Chance(level_chances=9)

game_ = Hangman(word_, score_, chance_)

hidden = game_.hidden_word.copy()

run = True
while run:
    clock.tick(fps)
    WIN.blit(source=background, dest=(0, 0))

    # Display guessed letters while keeping underscores
    underscore = h1.render(' '.join(hidden), True, color_white)
    word = h1.render(' '.join(game_.hidden_word).upper(), True, color_white)
    underscore_rect = underscore.get_rect()
    underscore_rect.midbottom = (width // 2, height // 2)

    # Display chances left:
    chance = par.render(f"CHANCES: {game_.chances.chances}", True, color_white)
    chance_rect = chance.get_rect()
    chance_rect.topleft = (size_par, size_par)

    # Display current score and streak in top right:
    score = par.render(f"SCORE: {game_.score.current_score}", True, color_white)
    score_rect = score.get_rect()
    score_rect.topright = (width - size_par, size_par)
    streak = par.render(f"STREAK: {game_.score.streak}", True, color_white)
    streak_rect = streak.get_rect()
    streak_rect.topright = (width - size_par, 2.5 * size_par)

    # Display used letters:
    used = h2.render(' '.join(game_.missed), True, color_white)
    used_rect = used.get_rect()
    used_rect.bottomleft = (size_par, height - 2 * size_par)
    pygame.draw.line(
        surface=WIN,
        color=(227, 227, 227),
        start_pos=(0, used_rect.top - size_span),
        end_pos=(width, used_rect.top - size_span)
    )
    used_text = par.render('USED LETTERS', True, color_white)
    used_text_rect = used_text.get_rect()
    used_text_rect.midbottom = (width // 2, used_rect.top - size_span)
    pygame.draw.lines(
        surface=WIN,
        color=(227, 227, 227),
        closed=True,
        points=(
            (used_text_rect.topleft[0] - size_span, used_text_rect.topleft[1]),
            (used_text_rect.topright[0] + size_span, used_text_rect.topright[1]),
            (used_text_rect.bottomright[0] + size_span, used_text_rect.bottomright[1]),
            (used_text_rect.bottomleft[0] - size_span, used_text_rect.bottomleft[1])
        )
    )

    # Display controls:
    controls_footer = span.render("Press Esc to quit game.", True, color_gray)
    controls_footer_rect = controls_footer.get_rect()
    controls_footer_rect.midbottom = (width // 2, height)

    WIN.blit(word, underscore_rect)
    WIN.blit(underscore, underscore_rect)
    WIN.blit(chance, chance_rect)
    WIN.blit(score, score_rect)
    WIN.blit(streak, streak_rect)
    WIN.blit(used, used_rect)
    WIN.blit(used_text, used_text_rect)
    WIN.blit(controls_footer, controls_footer_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key in game_.ascii_alphabet:
                guess = pygame.key.name(event.key).upper()
                if guess not in game_.used_letters:
                    game_.check(guess)

    pygame.display.update()

pygame.quit()
