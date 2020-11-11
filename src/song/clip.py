from termcolor import colored
import music21
from .note import Note

class Clip:
    def __init__(self, length: int, name: str = "Unnamed Clip"):
        self.name = name
        self.length = length
        self._notes = {}

    def add_note(self, note: Note, beat: int):
        if not beat in self._notes.keys():
            self._notes[beat] = []
        
        self._notes[beat].append(note)

    def __delitem__(self, key):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __str__(self):
        ret = ""
        for beat in self._notes.keys():
            for note in self._notes[beat]:
                ret += note.name + ", "

        ret = ret.strip(", ")
        return colored("Clip", "magenta") + ": " + self.name + " (" + ret + ")"

