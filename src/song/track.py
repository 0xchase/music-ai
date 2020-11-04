from termcolor import colored
from .clip import Clip

class Track:
    def __init__(self, name: str):
        self._name = name
        self._clips = []

    def name(self):
        return self._name

    def rename(self, name: str):
        self._name = name
    
    def add_clip(self, clip: Clip):
        self._clips.append(clip)

    def __str__(self):
        ret = colored("Track", "green") + ": " + self._name + "\n"

        for clip in self._clips:
            ret += "\t\t" + str(clip) + "\n"
        
        return ret