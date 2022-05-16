import json
import os
from gui.gui_highscores import GUIHighscores


class Highscores(GUIHighscores):
    def __init__(self):
        super().__init__(context=self)
        self.highscores = self.get_highscores()

    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def get_highscores(self):
        # def sort_by_dict_value(e):
        #     return e["score"]

        try:
            with open(self.get_path() + "/highscores.json") as f:
                highscores = json.load(f)
                highscores.sort(key=lambda e: e["score"], reverse=True)

        except FileNotFoundError:
            highscores = [
                {"name": "DEF", "score": 550},
                {"name": "DEF", "score": 425},
                {"name": "DEF", "score": 300},
                {"name": "DEF", "score": 200},
                {"name": "DEF", "score": 100}
            ]

        return highscores

    def check_if_highscore(self, score):
        for pos, record in enumerate(self.highscores):
            if score > record['score']:
                return pos

    def update_highscores(self, pos, name, score):
        self.highscores.pop()
        self.highscores.insert(pos, {"name": name, "score": score})

        with open(self.get_path() + "/highscores.json", 'w') as f:
            json.dump(self.highscores, f)

    def reset_highscores(self):
        try:
            os.remove(self.get_path() + '/highscores.json')
        except FileNotFoundError:
            pass
        else:
            self.highscores = self.get_highscores()

    def get_name(self):
        name_letters = self.gui_enter_name()
        return ''.join(name_letters)

    def display_highscores(self):
        self.gui_highscores()

