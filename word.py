# builtin
import os
from random import randint
# pip
import requests


class Word:
    def __init__(self):
        self.source_word_count = self.get_range()
        self.used_words = []

    @staticmethod
    def get_path():
        abs_path = os.path.abspath(os.path.dirname('__file__'))
        return os.path.join(abs_path + '/resources/words.txt')

    def get_range(self):
        range_ = 0
        with open(self.get_path()) as source:
            while source.readline():
                range_ += 1

        return range_

    def get_random_word(self):
        index = randint(0, self.source_word_count - 1)

        while index in self.used_words:
            index = randint(0, self.source_word_count)
        else:
            self.used_words.append(index)

        with open(self.get_path()) as source:
            for i in range(index):
                source.readline()

            return source.readline().strip().upper()

    @staticmethod
    def get_definition(word):
        try:
            data_ = requests.get(url=f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        except requests.ConnectionError:
            print('Problem with connection')
        else:
            try:
                clean_data = data_.json()[0]["meanings"][0]["definitions"][0]
            except KeyError:
                print('Failed to translate.')
            else:
                definition = clean_data["definition"]
                return definition
