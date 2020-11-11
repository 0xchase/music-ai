from src.algorithms.abstract.generator import ClipGenerator
from src.song.clip import Clip
from src.song.note import Note
import random as pyrandom

class RandomClipGenerator(ClipGenerator):
    def __init__(self):
        print("Created random clip generator")

    def generate(self, length: int):
        clip = Clip(length)
        for i in range(0, length):
            clip.add_note(Note(pyrandom.choice(["C1", "D1", "E1", "F1", "G1", "A1", "B1"]), 1), 1)

        return clip


    def info(self):
        return "Generates a clip using random note values"

