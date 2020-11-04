from .track import Track
from .clip import Clip
from termcolor import colored

class Session:
    def __init__(self, name: str):
        self._tracks: Track = []
        self._name = name
    
    def name(self) -> str:
        return self._name
    
    def rename(self, name: str):
        self._name = name

    def tracks(self) -> list:
        return self._tracks

    def get_track(self, name: str) -> Track:
        for track in self._tracks:
            if track.name() == name:
                return track

    def add_track(self, track: Track):
        self._tracks.append(track)

    def remove_track(self, num: int):
        del self._tracks[num]

    def __str__(self):
        ret = colored("Session", "green") + ": " + self._name + "\n"

        for track in self._tracks:
            ret += "\t" + str(track) + ""
        
        return ret
