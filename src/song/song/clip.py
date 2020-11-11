from termcolor import colored
from .note import Note

class Clip:
    def __init__(self, length: int, name: str = "Unnamed Clip"):
        self._name = name
        self._notes = {}

    def name(self):
        return self._name
    
    def add_note(self, note_name: str, beat, length):
        if not beat in self._notes.keys():
            self._notes[beat] = []
        
        self._notes[beat].append(Note(note_name, length))
    
    def get_notes(self):
        return self._notes

    def __str__(self):
        n = ""
        for beat in self._notes.keys():
            for note in self._notes[beat]:
                n += note.name + ", "

        return colored("Clip", "magenta") + ": " + self._name + " (" + n.strip(", ") + ")"
