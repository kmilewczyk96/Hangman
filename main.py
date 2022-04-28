import pygame

from gui_menu import GUIMenu
from gui_highscores import GUIHighscores
from gui_game import GUIGame

from word import Word
from score import Score
from highscores import Highscores
from chance import Chance
from hangman import Hangman

word_engine = Word()
score_engine = Score(1.25)
highscores_engine = Highscores()
chance_engine = Chance(12)

hangman_engine = Hangman(word_engine, score_engine, chance_engine)

game = GUIGame(game=hangman_engine)
highscores = GUIHighscores(highscores_engine.highscores)
main_menu = GUIMenu(
    title='- H A N G M A N - 2 -',
    menu_items=[
        {'name': 'start', 'action': game.start_game},
        {'name': 'hi-scores', 'action': highscores.display_highscores},
        {'name': 'test', 'action': highscores.enter_name},
        {'name': 'quit', 'action': pygame.quit}
    ]
)

if __name__ == '__main__':
    main_menu.run_menu()
