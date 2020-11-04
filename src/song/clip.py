from termcolor import colored

class Clip:
    def __init__(self, length: int, name: str = "Unnamed Clip"):
        self._name = name

    def name(self):
        return self._name

    def __str__(self):
        return colored("Clip", "magenta") + ": " + self._name
