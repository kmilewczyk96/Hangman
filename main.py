import sys

from gui import GUIMenu
from word import Word
from score import Score
from highscores import Highscores
from chance import Chance
from hangman import Hangman

# Game logic:
word_engine = Word()
score_engine = Score(1.25)
highscores_engine = Highscores()
chance_engine = Chance(15)
hangman_engine = Hangman(word_engine, chance_engine, score_engine, highscores_engine)

# GUIs:
main_menu = GUIMenu(
    title='- H A N G M A N - 2 -',
    menu_items=[
        {'name': 'Start', 'action': hangman_engine.run_game},
        {'name': 'Highscores', 'action': hangman_engine.highscores.display_highscores},
        {'name': 'Quit', 'action': sys.exit}
    ]
)


if __name__ == '__main__':
    while True:
        index = main_menu.run_menu()
        main_menu.menu_items[index].get('action')()

