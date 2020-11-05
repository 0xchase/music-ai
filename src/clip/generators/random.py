from clip.abstract.generator import ClipGenerator
from music21 import *

class RandomClipGenerator(ClipGenerator):
    def __init__(self):
        print("Created random clip generator")

    def generate(self):
        print("Running random clip generator")
        s = stream.Stream()
        for i in range(0, 30):
            n = note.Note("C4")
            s.append(n)

        return s


    def info(self):
        return "Generates a clip using random note values"

