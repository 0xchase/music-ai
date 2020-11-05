from termcolor import colored
import music21

class Clip:
    def __init__(self, length: int, name: str = "Unnamed Clip"):
        self._name = name
        self._stream = music21.stream.Stream()

    def name(self):
        return self._name

    def append(self, n):
        self._stream.append(n)

    def __str__(self):
        ret = ""
        for note in self._stream:
            ret += str(note) + ", "
        return colored("Clip", "magenta") + ": " + self._name + " (" + ret + ")"

