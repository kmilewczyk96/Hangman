import json
import os


class Highscores:
    def __init__(self):
        self.highscores = self.get_highscores()

    @staticmethod
    def get_path():
        return os.path.abspath(os.path.dirname(__file__))

    def get_highscores(self):
        def sort_by_dict_value(e):
            return e["score"]

        try:
            with open(self.get_path() + "/highscores.json") as f:
                highscores = json.load(f)
                highscores.sort(key=sort_by_dict_value, reverse=True)

        except FileNotFoundError:
            highscores = [
                {"name": "DEF", "score": 22500},
                {"name": "DEF", "score": 425},
                {"name": "DEF", "score": 300},
                {"name": "DEF", "score": 200},
                {"name": "DEF", "score": 100}
            ]

        return highscores
