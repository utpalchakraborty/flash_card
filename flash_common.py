import json
import random


class WordData(object):

    words_db_file = './words.json'
    words_key = 'words'
    DONE_COUNT = 5

    def __init__(self):
        self._data = {}
        self._random_spanish_list = []
        self._load_db()

    @property
    def words_dict(self):
        return self._data["words"]

    def _load_db(self):
        with open(WordData.words_db_file) as data_file:
            self._data = json.load(data_file)
        self._random_spanish_list = \
            [key for key, value in self._data[WordData.words_key].items() if value['c'] < WordData.DONE_COUNT]

    def done_words(self):
        return {key for key, value in self._data[WordData.words_key].items() if value['c'] >= WordData.DONE_COUNT}

    def not_done_words(self):
        return {key: value['e']
                for key, value in self._data[WordData.words_key].items() if value['c'] < WordData.DONE_COUNT}

    def write_db(self):
        # update the
        with open(WordData.words_db_file, 'w') as data_file:
            data_file.write(json.dumps(self._data, indent=4, sort_keys=True))

    def modify_freq(self, spanish_word, amount):
        self._data[WordData.words_key][spanish_word]['c'] += amount

    def add_word(self, spanish, english):
        self._data[WordData.words_key][spanish] = {'e': english.lower(), 'c': 0}

    @property
    def num_words(self):
        return len(self._data[WordData.words_key])

    def get_english(self, spanish):
        return self._data[WordData.words_key][spanish]['e']

    def get_random(self):
        if len(self._random_spanish_list) == 0:
            return None, None
        spanish = random.choice(self._random_spanish_list)
        self._random_spanish_list.remove(spanish)
        return spanish, self.get_english(spanish)


