import sys

from gui.gui_menu import GUIMenu
from gui.gui_highscores import GUIHighscores
from gui.gui_game import GUIGame

from word import Word
from score import Score
from highscores import Highscores
from chance import Chance
from hangman import Hangman

word_engine = Word()
score_engine = Score(1.25)
highscores_engine = Highscores()
chance_engine = Chance(2)

hangman_engine = Hangman(word_engine, score_engine, chance_engine)

game = GUIGame(game=hangman_engine)
highscores = GUIHighscores(highscores_engine.highscores)
main_menu = GUIMenu(
    title='- H A N G M A N - 2 -',
    menu_items=[
        {'name': 'Start', 'action': game.start_game},
        {'name': 'Highscores', 'action': highscores.display_highscores},
        {'name': 'Test', 'action': highscores.enter_name},
        {'name': 'Quit', 'action': sys.exit}
    ]
)

if __name__ == '__main__':
    main_menu.run_menu()
