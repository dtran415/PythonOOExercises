"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    
    def __init__(self, path):
        """ open file and parse words """
        self.dict = self.parse(path)
        print(f'{len(self.dict)} words read')

    def parse(self, path):
        """ open file and parse lines into words """
        res = None
        with open(path) as f:
            res = [line.strip() for line in f.readlines()]
        return res

    def random(self):
        """ choose a random word from the array of words created from the file """
        return random.choice(self.dict)