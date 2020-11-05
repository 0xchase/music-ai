from termcolor import colored
import music21
from .measure import Measure

class Clip:
    def __init__(self, length: int, name: str = "Unnamed Clip"):
        self.name = name
        self.length = length
        self._measures = []
        for _ in range(0, length):
            self._measures.append(Measure())

    def append(self, n):
        self._measures.append(n)

    def __delitem__(self, key):
        del _measures[key]

    def __getitem__(self, key):
        return _measures[key]

    def __setitem__(self, key, value):
        _measures[key] = value

    def __str__(self):
        ret = ""
        for note in self._measures:
            ret += str(note) + ", "

        ret = ret.strip(", ")
        return colored("Clip", "magenta") + ": " + self.name + " (" + ret + ")"

